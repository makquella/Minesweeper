# План проекту

##Аналіз обраної гри та діаграма випадків використання

**Актор:**
- **Гравець** — користувач, що взаємодіє з грою через GUI.

**Випадки використання (Use Cases):**

| Випадок         | Опис                                                                 |
|-----------------|----------------------------------------------------------------------|
| **Start Game**  | Почати нову гру: генерується поле, обнуляються таймер і лічильник мін.|  
| **Reveal Cell** | Відкрити клітинку: якщо це міна — поразка; якщо цифра — показати число; якщо порожня — рекурсивне відкриття сусідів.|  
| **Toggle Flag** | Поставити або зняти прапорець на вибраній клітинці (для позначення мін).|  
| **Restart Game**| Перезапустити гру з тими ж налаштуваннями складності (R).            |  
| **Quit Game**   | Вийти з гри (Q) та закрити вікно.                                     |  
| **Win Game**    | Виграти гру: всі безпечні клітинки відкриті.                          |  
| **Lose Game**   | Програти гру: гравець відкрив клітинку з міною.                       |  

```mermaid
usecaseDiagram
  actor Player as "Гравець"
  Player --> (Start Game)
  Player --> (Reveal Cell)
  Player --> (Toggle Flag)
  Player --> (Restart Game)
  Player --> (Quit Game)
  (Reveal Cell) --> (Win Game)
  (Reveal Cell) --> (Lose Game)
flowchart TD
  Start([Start]) --> Generate["Generate Field"]
  Generate --> Display["Draw Grid"]
  Display --> UserAction{"Player Action?"}
  UserAction -- "Reveal Cell" --> Reveal["Board.reveal()"]
  UserAction -- "Toggle Flag" --> Flag["Board.toggle_flag()"]
  UserAction -- "Restart (R) / Quit (Q)" --> Exit["_restart() / quit"]
  Reveal --> CheckMine{"Cell is Mine?"}
  CheckMine -- Yes --> Lose["Lose Game"]
  CheckMine -- No --> CheckWin{"All Safe Opened?"}
  CheckWin -- Yes --> Win["Win Game"]
  CheckWin -- No --> DrawAgain["Draw Grid"] --> Display
  Flag --> Display
  Lose --> End([End])
  Win --> End([End])
flowchart LR
  RestartKey[/Press R/] --> _restart["GameUI._restart()"]
  _restart --> Generate
  Generate --> ResetTimer["start_ticks reset"]
  ResetTimer --> DrawGrid["Draw new field"]
  DrawGrid --> EndRestart([Playing])
classDiagram
  class Board {
    - int width
    - int height
    - int mines
    - List[List[str]] grid
    - List[List[bool]] revealed
    - List[List[bool]] flagged
    - int game_over?
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
    - Font font, header_font
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
