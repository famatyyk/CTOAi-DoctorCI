---
name: ctoai-doctor-ci
description: GitHub Action that runs a static C++/Lua/Python security & quality audit on every pull request using CTOAi Project Doctor. Use when you want automated PR audits, CI annotations for high-risk findings (unsafe functions, missing tests, load/os.execute in Lua), and a 0-100 Project Health score. Legal, read-only, no process injection.
---

# CTOAi Doctor CI

A GitHub Action that runs a **static, read-only** code audit on every pull request.
It reuses [CTOAi-Project-Doctor](https://github.com/famatyyk/CTOAi-Project-Doctor)
to detect risky patterns and compute a **Project Health** score (0–100).

## What it checks
- C/C++: raw `new`, `strcpy`/`strcat`/`gets`/`sprintf`, missing `target_compile_features` in CMake
- Lua: `load`, `os.execute`, `socket` (mod-audit patterns)
- Python/JS/TS: leaked secrets, missing tests, missing README
- Outputs `::error` annotations for high-severity findings directly in the PR diff view

## Safety
This action **never** modifies your code, injects into processes, or runs untrusted
binaries. It only parses source text. Suitable for compliance-friendly CI.

## Usage
```yaml
# .github/workflows/doctor.yml
name: Doctor CI
on: [pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: famatyyk/CTOAi-DoctorCI@main
        with:
          target: "."
          fail_on_high: "0"   # set "1" to block PRs with high-risk findings
```

## Outputs
- `health_score` — Project Health 0–100
- `high_risk` — count of high-severity findings

## Pricing
Subscription: **29 €/month** (part of the CTOAi Tools ecosystem).
Landing: https://ctoai-funnel.fly.dev/

## Links
- Action repo: https://github.com/famatyyk/CTOAi-DoctorCI
- Doctor engine: https://github.com/famatyyk/CTOAi-Project-Doctor
