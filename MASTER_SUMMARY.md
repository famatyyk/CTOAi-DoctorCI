# CTOAi Ecosystem — MASTER SUMMARY (stan na 2026-08-09)

Zcentralizowany dokument ekosystemu. Asystent prowadzi, user nie klika.

## PRODUKTY (8 w funnelze ctoai-funnel.fly.dev)
| # | Nazwa | Repo | Cena | Status |
|---|-------|------|------|--------|
| 1 | Project Doctor (audyt statyczny) | famatyyk/CTOAi-Project-Doctor | 19/29€ | LIVE |
| 2 | Lua Script Hub | famatyyk/CTOAi-LuaHub | 19€ | LIVE |
| 3 | WinAPI Toolkit | famatyyk/CTOAi-WinToolkit | 29€ | LIVE |
| 4 | CTF Pack | famatyyk/CTOAi-CTFGen | 19€ | LIVE |
| 5 | Anti-Cheat Lab (detection-only) | famatyyk/CTOAi-ACLab | 29€ | LIVE |
| 6 | Memory Scanner (własna pamięć) | famatyyk/CTOAi-MemScan | 29€ | LIVE |
| 7 | Game Mod Audit | famatyyk/CTOAi-ModAudit | 19€ | LIVE |
| 8 | Doctor CI (GitHub Action) | famatyyk/CTOAi-DoctorCI | 29€ | LIVE + beta PR green |

## DOKONCZONE W TYM WORKFLOW
- **A (beta CI):** PR #1 w CTOAi-DoctorCI merged, CI green (3 success runs), `entry.py` instalacja przez `git+https`, `Dockerfile` poprawiony, `doctor.yml` workflow. ✓
- **C (cross-post):**
  - Dev.to artykuł ecosystem LIVE: https://dev.to/famatyyk/7-legalnych-narzedzi-c-lua-windows-ktore-zbudowalem-zamiast-cheatow-4de0
  - SkillsLLM: `SKILL.md` gotowy w repo, ale **BLOCKED** — wymagają ≥100⭐ (mamy 0). Submit przez UI (OAuth) niemożliwy teraz.
  - Hashnode / Mirror: artykuł w `CTOAi-DoctorCI/CROSSPOST.md` — czeka na Twoje konto/wallet.
- **B (screenshot):** `landing_preview.png` w README `CTOAi-DoctorCI` + raw GitHub link. Dev.to obrazek **BLOCKED** — token `.devto_token` wygasł (401 PUT).

## LANDING (ctoai-funnel.fly.dev)
- Linear-style redesign (8 kart, 3+3+2 symetria), deploy live.
- Funnel: whitelist 14 kategorii, ci=29€ dodane.
- Leady: /data/leads.db (Fly), API /api/lead.

## BLOKADY (wymagają akcji usera)
1. **SkillsLLM 100⭐** — nie do przejścia bez społeczności. Opcje: (a) zostawić, (b) zdobyć gwiazdki, (c) pominąć.
2. **Dev.to token** — `.devto_token` wygasł. Po odświeżeniu dopatchuję obrazek do artykułu.
3. **Hashnode/Mirror** — wymagają Twojego konta.

## PLIKI / KREDENCJAŁY (NIGDY W CZACIE)
- `CTOAi-Funnel/.devto_token` — [WYGASŁY]
- `CTOAi-DoctorCI/.skillsllm_token` — [ZAPISANY, gitignored]
- GitHub: GCM (famatyyk)
- Fly: CTOComapnyAi@proton.me

## CO DALEJ (do przemyślenia)
- Czy gonić za 100⭐ na SkillsLLM, czy skupić się na sprzedaży (leady)?
- Czy odświeżyć Dev.to token i dopatchować obrazek?
- Nowy kierunek: np. automatyczny newsletter z auditami, lub SaaS dashboard dla leadów.
