import argparse

from logic import Board
from ui import GameUI


def main():
    parser = argparse.ArgumentParser(
        description="Minesweeper Game"
    )
    parser.add_argument(
        "--difficulty",
        "-d",
        choices=["easy", "medium", "hard"],
        default="easy",
        help="Рівень складності гри (easy/medium/hard)"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="Ширина вікна (пікселів) або None для розрахунку по клітинках"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=None,
        help="Висота вікна (пікселів) або None для розрахунку по клітинках"
    )
    args = parser.parse_args()

    # --- НОВЫЙ БЛОК: выбор параметров по сложности ---
    DIFFICULTIES = {
        'easy':   {'width': 9,  'height': 9,  'mines': 10},
        'medium': {'width': 16, 'height': 16, 'mines': 40},
        'hard':   {'width': 30, 'height': 16, 'mines': 99},
    }
    cfg = DIFFICULTIES[args.difficulty]

    board = Board(width=cfg['width'],
                  height=cfg['height'],
                  mines=cfg['mines'])
    # ----------------------------------------------

    game = GameUI(board,
                  width=args.width,
                  height=args.height)
    game.run()


if __name__ == "__main__":
    main()
