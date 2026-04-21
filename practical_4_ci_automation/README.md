[![Python CI](https://github.com/<username>/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/<username>/<repo>/actions/workflows/ci.yml)

# Практическая работа №4

Автоматизация проверок качества кода (CI).

## Что настроено
- GitHub Actions workflow: `.github/workflows/ci.yml`
- Локальный pre-push hook: `.githooks/pre-push`
- Опциональный `.gitlab-ci.yml`

## Локальные проверки
```bash
black --check src tests
flake8 src/
pytest tests/ -v
```

## Установка pre-push hook
```bash
git config core.hooksPath .githooks
```
