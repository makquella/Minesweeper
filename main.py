import argparse
from logic import Board
from ui import GameUI

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Minesweeper Game")
    parser.add_argument("--difficulty", "-d", choices=["easy", "medium", "hard"], default="easy",
                        help="Рівень складності гри (easy/medium/hard)")
    parser.add_argument("--width", type=int, default=800,
                        help="Ширина вікна (пікселів, за замовчуванням 800)")
    parser.add_argument("--height", type=int, default=600,
                        help="Висота вікна (пікселів, за замовчуванням 600)")
    args = parser.parse_args()

    # TODO: настроїти параметри поля в залежності від складності
    board = Board()
    game = GameUI(board, width=args.width, height=args.height)
    game.run()
