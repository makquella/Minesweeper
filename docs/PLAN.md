# План проекту

## Аналіз обраної гри та діаграма випадків використання

**Актор:**
- **Гравець** — користувач, що взаємодіє з грою через GUI.

**Випадки використання (Use Cases):**

| Випадок         | Опис                                                                 |
|-----------------|----------------------------------------------------------------------|
| **Start Game**  | Почати нову гру: генерується поле, обнуляються таймер і лічильник мін. |
| **Reveal Cell** | Відкрити клітинку: якщо це міна — поразка; якщо цифра — показати число; якщо порожня — рекурсивне відкриття сусідів. |
| **Toggle Flag** | Поставити або зняти прапорець на вибраній клітинці (для позначення мін). |
| **Restart Game**| Перезапустити гру з тими ж налаштуваннями складності (натиск R). |
| **Quit Game**   | Вийти з гри (натиск Q) та закрити вікно. |
| **Win Game**    | Виграти гру: всі безпечні клітинки відкриті. |
| **Lose Game**   | Програти гру: гравець відкрив клітинку з міною. |

```mermaid
flowchart LR
  subgraph UseCases[Випадки використання]
    UC1[(Start Game)]
    UC2[(Reveal Cell)]
    UC3[(Toggle Flag)]
    UC4[(Restart Game)]
    UC5[(Quit Game)]
    UC6[(Win Game)]
    UC7[(Lose Game)]
  end
  Player((Гравець))
  Player --> UC1
  Player --> UC2
  Player --> UC3
  Player --> UC4
  Player --> UC5
  UC2 --> UC6
  UC2 --> UC7
```

## Проєктування гри: діаграми діяльності та класів

### Діаграма діяльності: основний цикл гри

```mermaid
flowchart TD
  Start([Start]) --> Generate["Generate Field"]
  Generate --> Display["Draw Grid"]
  Display --> UserAction{"Player Action?"}
  UserAction -- "Reveal Cell" --> Reveal["Board.reveal()"]
  UserAction -- "Toggle Flag" --> Flag["Board.toggle_flag()"]
  UserAction -- "Restart / Quit" --> Exit["_restart() / quit"]
  Reveal --> CheckMine{"Cell is Mine?"}
  CheckMine -- Yes --> Lose["Lose Game"]
  CheckMine -- No --> CheckWin{"All Safe Opened?"}
  CheckWin -- Yes --> Win["Win Game"]
  CheckWin -- No --> Display
  Flag --> Display
  Lose --> End([End])
  Win --> End([End])
```

### Діаграма діяльності: сценарій перезапуску

```mermaid
flowchart LR
  RestartKey[/Press R/] --> Restart["GameUI._restart()"]
  Restart --> Generate
  Generate --> ResetTimer["start_ticks reset"]
  ResetTimer --> DrawGrid["Draw new field"]
  DrawGrid --> Play["Playing"]
```

### Діаграма класів

```mermaid
classDiagram
  class Board {
    - int width
    - int height
    - int mines
    - List[List[str]] grid
    - List[List[bool]] revealed
    - List[List[bool]] flagged
    - bool game_over
    + __init__(width, height, mines)
    + _generate()
    + _count_adjacent(row, col) int
    + reveal(row, col)
    + toggle_flag(row, col)
    + check_win() bool
  }

  class GameUI {
    - Board board
    - Surface screen
    - Font font
    - Font header_font
    - int start_ticks
    + __init__(board, width=None, height=None)
    + run()
    + _restart()
    + _draw()
    + _draw_message(text)
  }

  class Main {
    + main(): None
  }

  Player --> Main : invokes
  Main --> Board
  Main --> GameUI
  GameUI --> Board : uses
```
