# Minesweeper

Класичний «Сапер» на Python з використанням Pygame.

## Опис

Гравець відкриває клітини поля, уникаючи мін. Мета – відкрити всі порожні клітини.

## Вимоги

- Python 3.10+
- pygame

## Встановлення

```bash
git clone https://github.com/ВашЛогин/minesweeper-pygame.git
cd minesweeper-pygame
python -m venv venv
source venv/bin/activate   # або venv\Scripts\activate на Windows
pip install -r requirements.txt
```

## Запуск

```bash
python main.py --difficulty easy --width 800 --height 600
```

## Структура проекту

- `logic.py` – логіка гри (генерація поля, підрахунок мін тощо)
- `ui.py` – графічний інтерфейс на Pygame
- `main.py` – точка запуску з argparse
- `tests/` – юніт-тести
- `docs/PLAN.md` – етап планування (опис, діаграми)
- `.github/workflows/ci.yml` – налаштування GitHub Actions
- `.gitignore` – правила ігнорування

## Ліцензія

MIT
