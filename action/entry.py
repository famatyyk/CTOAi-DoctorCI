"""CTOAi Doctor CI — entrypoint GitHub Action.

Instaluje CTOAi-Project-Doctor z GitHub i uruchamia statyczny audyt
na repozytorium wskazanym przez input. Wynik: raport + annotation
w GitHub UI (jeśli wykryto problemy wysokiego ryzyka).

Legalne: read-only analiza plików, brak modyfikacji repo ani injection.
"""

import os
import sys
import subprocess
import json
import urllib.request
import tempfile


def install_doctor():
    """Pobierz CTOAi-Project-Doctor jako paczke (git clone + pip install -e).
    Pomijane gdy CTOAi_DOCTOR_SKIP_INSTALL=1 (dev/test z lokalnym clone)."""
    if os.environ.get("CTOAi_DOCTOR_SKIP_INSTALL") == "1":
        print("Instalacja pominieta (CTOAi_DOCTOR_SKIP_INSTALL=1)")
        return None
    tmp = tempfile.mkdtemp(prefix="doctor_")
    url = "https://github.com/famatyyk/CTOAi-Project-Doctor.git"
    subprocess.run(["git", "clone", "--depth", "1", url, tmp],
                   check=True, capture_output=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", tmp, "-q"],
                   check=True, capture_output=True)
    return tmp


def run_audit(target_dir: str) -> dict:
    from project_doctor import analyzer
    from pathlib import Path
    result = analyzer.analyze_repository(Path(target_dir).resolve(strict=False), max_files=2000)
    d = result.as_dict()
    findings = d.get("findings", [])
    score = d.get("score", {})
    # score moze byc int lub dict (np. {"health": 42})
    if isinstance(score, dict):
        health = score.get("health", score.get("total", 100))
    else:
        health = score
    high = [f for f in findings if f.get("severity") == "high"]
    return {
        "score": health,
        "total_findings": len(findings),
        "high_risk": len(high),
        "categories": sorted({f.get("category") for f in findings}),
        "high_samples": high[:5],
    }


def main():
    target = os.environ.get("INPUT_TARGET", ".")
    fail_on = int(os.environ.get("INPUT_FAIL_ON_HIGH", "0"))

    print("::group::Instalacja CTOAi-Project-Doctor")
    install_doctor()
    print("::endgroup::")

    print("::group::Audyt repozytorium")
    out = run_audit(target)
    print("::endgroup::")

    print(f"Project Health: {out['score']}/100")
    print(f"Znalezione: {out['total_findings']} (wysokie ryzyko: {out['high_risk']})")
    for f in out["high_samples"]:
        msg = f.get("title", "problem")
        rule = f.get("rule_id", "?")
        # GitHub annotation (bez sciezki bezwzglednej - bezpiecznie)
        print(f"::error ::[{rule}] {msg}")

    # zapisz podsumowanie jako output
    with open(os.environ.get("GITHUB_OUTPUT", "/dev/stdout"), "a", encoding="utf-8") as gh:
        gh.write(f"health_score={out['score']}\n")
        gh.write(f"high_risk={out['high_risk']}\n")

    if fail_on and out["high_risk"] > 0:
        print(f"FAIL: wykryto {out['high_risk']} problemow wysokiego ryzyka")
        sys.exit(1)
    print("OK: audyt zakonczony")


if __name__ == "__main__":
    main()
