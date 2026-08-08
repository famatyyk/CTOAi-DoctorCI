# CTOAi Doctor CI

GitHub Action: statyczny audyt C++ / Lua / Python na każdym PR.

## Co robi
- Instaluje [CTOAi-Project-Doctor](https://github.com/famatyyk/CTOAi-Project-Doctor)
- Analizuje repozytorium (read-only, bez modyfikacji)
- Wykrywa: `strcpy`, surowe `new`, brak `target_compile_features` (CMake),
  `load` / `os.execute` w Lua, wycieki sekretów
- Wypisuje `Project Health 0–100` i annotation `::error` dla HIGH
- Opcjonalnie: `fail_on_high=1` przerywa PR przy problemach HIGH

## Bezpieczeństwo
Action NIE modyfikuje Twojego kodu ani nie wstrzykuje nic do procesów.
Tylko statyczna analiza plików tekstowych.

## Użycie (`.github/workflows/doctor.yml`)

```yaml
name: CTOAi Doctor
on: [pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: famatyyk/CTOAi-DoctorCI@main
        with:
          target: "."
          fail_on_high: "0"
```

## Cena
Subskrypcja CI: **29 € / mies.** (w ramach ekosystemu CTOAi Tools).
Więcej: https://ctoai-funnel.fly.dev/
