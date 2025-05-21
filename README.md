# Minesweeper

Класичний «Сапер» на Python з використанням Pygame.

## Опис

Гравець відкриває клітини поля, уникаючи мін. Мета – відкрити всі небезпечні клітинки, не підірвавшись.

## Особливості

- **Три рівні складності**:
  - `easy` (9×9, 10 мін)
  - `medium` (16×16, 40 мін)
  - `hard` (30×16, 99 мін)
- **Таймер** у верхній панелі показує, скільки секунд пройшло з початку гри.
- **Лічильник мін** відображає кількість мін, що залишилися (мінус встановлені вами прапорці).
- **Управління**:
  - **Лівий клік** – відкрити клітинку
  - **Правий клік** – поставити/зняти прапорець
  - **R** – перезапустити поточну гру
  - **Q** – вийти з гри

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


# за умовчанням запускається easy
python main.py

# вказати рівень складності (easy|medium|hard)
python main.py --difficulty medium

# додатково можна задати розмір вікна
python main.py --difficulty hard --width 1024 --height 800


## Тестування локально

```bash
python -m pip install -r requirements.txt
python -m flake8 .
python -m pytest          # або pytest -m "not slow