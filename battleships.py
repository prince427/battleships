import random

class Board:
    boardArray = []
    for x in range(0, 5):
        boardArray.append(["o"] * 5)

    def print_board(self, boardArray):
        for row in boardArray:
            print(" ".join(row))


player1Board = Board()
player2Board = Board()

class Player:

    def __init__(self, name, guess_row, guess_col):
        self.name = name
        self.guess_row = guess_row
        self.guess_col = guess_col


class Ships:
    def __init__(self, ship_row, ship_col):
        self.ship_row = ship_row
        self.ship_col = ship_col

def player1_turn():
    for turn in range(4):
        player1.guess_row = int(input("Guess Row"))
        player1.guess_col = int(input("Guess Col"))

        if (player1.guess_col == Ships.ship_col and player1.guess_row == Ships.ship_row):
            print("Congratulations! You sunk my battleship")
            break
        if (player1.guess_col == Ships.ship_col and player1.guess_row == Ships.ship_row):
            print("Congratulations! You sunk my battleship")
            break
        else:
            print("You missed my battleship")
            player2Board.boardArray[player1.guess_row][player1.guess_col] = ("X")

        print("Turn " + str(turn + 1) + " out of 4.")
        player2Board.print_board(player2Board.boardArray)

        if turn >= 3:
            print("Game over")
            break



player1 = Player("Nazim", 0, 0)
player2 = Player("Tom", 0, 0)


player1_patrol1 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_patrol2 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_battle1 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_battle2 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_sub1 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_destroyer1 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))
player1_carrier1 = Ships(random.randint(0, len(player2Board.boardArray) - 1), random.randint(0, len(player2Board.boardArray) - 1))

print("Hello and welcome to battleships!")

player1_turn()









