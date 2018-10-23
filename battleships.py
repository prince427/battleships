import random


class Board:

    board = []
    for x in range(0,5):
        board.append(["o"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))
    print_board(board)

newBoard = Board()


class Player:

    def __init__(self, name, guess_row, guess_col):
        self.name = name
        self.guess_row = guess_row
        self.guess_col = guess_col


class Ships:
    ship_row = random.randint(0, 5)
    ship_col = random.randint(0, 5)

    def __init__(self, ship_row, ship_col):
        self.ship_row = ship_row
        self.ship_col = ship_col


player1 = Player("Nazim", 3, 3)
player2 = Player("John", 3, 3)
ship1 = Ships(random.randint(0, 5), random.randint(0, 5))
ship2 = Ships(random.randint(0, 5), random.randint(0, 5))

print("Hello and welcome to battleships!")

