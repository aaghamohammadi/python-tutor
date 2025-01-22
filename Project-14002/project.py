"""
MineSweeper Game - CLI Version

Developed as part of the Fundamentals of Programming course
Under the supervision of Prof. Alireza Aghamohammadi (@aaghamohammadi on GitHub)
by Amin Hashemi (@minhashemi on GitHub)

Spring 2021, Sharif University of Technology
"""

# libraries
import csv
import pandas as pd
import sys
import random
from enum import Enum
import pyfiglet
from tabulate import tabulate
import base64

# classes - done
class GameStatus(Enum):
    PLAYING = 0
    LOSE = 1
    WIN = 2


class MineBoard(object):
    score = 0

    def __init__(self, w, h, k):
        # Create a new board with size w x h
        self.w = w
        self.h = h
        self.board = [[0 for i in range(w)] for j in range(h)]
        self.allocateMines(w, h, k)
        self.status = GameStatus.PLAYING
        self.cellsToOpen = w * h - k

    def allocateMines(self, w, h, numOfMines):
        allocIndexes = self.getRandomPos(w * h, numOfMines)
        for i in allocIndexes:
            self.setMine(int(i / w), i % h)
            self.setAdjacentMines(int(i / w), i % h)

    def printLayout(self):
        print(" " * 7 + "".join(map(lambda x: "{:^7d}".format(x + 1), range(self.w))))
        print(" " * 7 + "-" * (self.w * 7))
        for (i, row) in enumerate(self.board):
            print(
                "{:^7d}".format(i + 1)
                + "|"
                + " |".join(list(map(lambda x: "{:^5s}".format(self.display(x)), row)))
                + " | "
            )
            print(" " * 7 + "-" * (self.w * 7))

    def click(self, row, col):
        value = self.reveal(row, col)
        if value:
            self.cellsToOpen -= 1
            MineBoard.score += 10
            if self.cellsToOpen == 0:
                self.status = GameStatus.WIN
            if self.hasMine(row, col):
                self.status = GameStatus.LOSE
            elif self.isBlank(row, col):
                for dr in range(row - 1, row + 2):
                    for dc in range(col - 1, col + 2):
                        self.click(dr, dc)

    def flag(self, row, col):
        if self.isValidCell(row, col) and self.isHidden(row, col):
            self.toggleFlag(row, col)

    def isValidCell(self, row, col):
        return row >= 0 and row < self.h and col >= 0 and col < self.w

    def getRandomPos(self, n, k):
        res = []
        remains = [i for i in range(n)]
        while k > 0:
            r = random.randint(0, len(remains) - 1)
            res.append(r)
            del remains[r]
            k -= 1
        return res

    # Convention for cell values:
    #    - 0 : Hidden Blank
    #    - 10 : Revealed Blank
    #    - -1 : Hidden Bomb
    #    - 9 : Revealed Bomb
    #    - 1 ~ 8 : number of adjacent bomb (hidden)
    #    - 11 ~ 18 : adjacent bomb (revealed)
    #    - x + 100 : Flagged
    #

    def setMine(self, row, col):
        self.board[row][col] = -1

    def setAdjacentMines(self, row, col):
        for dr in range(row - 1, row + 2):
            for dc in range(col - 1, col + 2):
                if self.isValidCell(dr, dc) and not self.hasMine(dr, dc):
                    self.board[dr][dc] += 1

    def toggleFlag(self, row, col):
        if self.isFlagged(row, col):
            self.board[row][col] -= 100
        else:
            self.board[row][col] += 100

    # Open a cell and return its value
    def reveal(self, row, col):
        if not self.isValidCell(row, col) or not self.isHidden(row, col):
            return None
        if self.isFlagged(row, col):
            self.toggleFlag(row, col)
        self.board[row][col] += 10
        return self.board[row][col]

    def isHidden(self, row, col):
        return self.board[row][col] < 9

    def hasMine(self, row, col):
        return self.board[row][col] % 10 == 9

    def isBlank(self, row, col):
        return self.board[row][col] % 10 == 0

    def isOver(self):
        return self.winGame() or self.loseGame()

    def loseGame(self):
        return self.status == GameStatus.LOSE

    def winGame(self):
        return self.status == GameStatus.WIN

    def isFlagged(self, row, col):
        return self.board[row][col] > 90

    def revealAll(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.reveal(i, j)

    def display(self, ip):
        if ip > 90:
            return "F"
        elif ip == 9:
            return "x"
        elif ip == 10:
            return "."
        elif ip > 10:
            return str(ip - 10)
        return "*"


# functions
#   play function - done
def play():
    print("Select game level")
    print("[B]eginner, [I]ntermediate, [A]dvanced")
    lvl = input("Select game level: ").strip().upper()
    if lvl == "B":
        size = 10
        mine = random.randint(int(0.1 * (size**2)), int(0.3 * (size**2)))
        game = MineBoard(size, size, mine)
    elif lvl == "I":
        size = 15
        mine = random.randint(int(0.1 * (size**2)), int(0.3 * (size**2)))
        game = MineBoard(size, size, mine)
    elif lvl == "A":
        size = 25
        mine = random.randint(int(0.1 * (size**2)), int(0.3 * (size**2)))
        game = MineBoard(size, size, mine)
    else:
        print("I didn't Understand! Try again...")
        play()

    while not game.isOver():
        game.printLayout()
        command = nextCommand()
        if command == "Q":
            main()
        splits = command.split(" ")
        row = int(splits[0]) - 1
        col = int(splits[1]) - 1
        if command[-1] == "F":
            game.flag(row, col)
        else:
            game.click(row, col)

    game.revealAll()
    game.printLayout()
    if game.loseGame():
        print("Game Over 😵")

    elif game.winGame():
        print("You won! Congradulations 🤩")


def nextCommand():
    return (
        input(
            "Commands : \n<row> <col> : open cell\n<row> <col> F : flag cell\nq : quit\n"
        )
        .strip()
        .upper()
    )


#   main page - done
def main():
    print(pyfiglet.figlet_format("MineSweeper", font="speed"))
    print("Open as many cells as you can without hitting a bomb 💣")
    print("=====================")
    print("1.Login")
    print("2.Sign Up")
    print("3.Score Board")
    print("4.Exit")
    print("=====================")
    mainOptions()


#   main options - done
def mainOptions():
    try:
        choice = int(input("Please enter user choice : "))
        if choice == 1:
            print("\n===================================================\n")
            login()
            print("\n===================================================\n")
            mainOptions()
        elif choice == 2:
            print("\n===================================================\n")
            signup()
            print("\n===================================================\n")
            mainOptions()
        elif choice == 3:
            print("\n===================================================\n")
            scoreboard()
            print("\n===================================================\n")
            mainOptions()
        elif choice == 4:
            sys.exit()
        else:
            print("\nInvalid Choice. Please enter valid choice")
            print("\n===================================================\n")
            main()
            print("\n===================================================\n")
            mainOptions()
    except ValueError:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        main()
        print("\n===================================================\n")
        mainOptions()


#   username get and check if it is in former users. - done
def usrnmget():
    with open("userdb.csv") as file:

        userdb = csv.DictReader(file)
        usr = input("Enter Username: ")
        for user in userdb:
            if usr == user["username"]:
                print("sorry! Username already taken. What would you like to do next?")
                print("=====================")
                print("1.Login")
                print("2.Try Again")
                print("3.Main Menu")
                print("=====================")
                choice = int(input())
                if choice == 1:
                    login()
                elif choice == 2:
                    signup()
                elif choice == 3:
                    main()
                else:
                    print(
                        "Oops! I didn't understand. So I will take you back to main menu :)"
                    )
                    main()
        if usr:
            return usr
        else:
            print("Empty Username! Try again")
            usrnmget()


#   sign up function - done
def signup():
    try:
        file = open("userdb.csv")
        file.close()

    except FileNotFoundError:
        with open("userdb.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "score"])
    print("=====================")
    print("1.Enter Credentials")
    print("2.Main Menu")
    print("=====================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = usrnmget()
        password = input("Enter Password: ").encode("utf-8")
        encoded_pass = base64.b64encode(password)
        with open("userdb.csv", "a") as db:
            writer = csv.DictWriter(db, fieldnames=["username", "password", "score"])
            writer.writerow(
                {"username": username, "password": encoded_pass, "score": 0.0}
            )
        print("Congratulations! You registered successfully.")
        main()
    elif choice == 2:
        main()
    else:
        print("Oops! I don't understand. Try again...")
        signup()


#   login page -
def login():
    print("=====================")
    print("1.Enter Credentials")
    print("2.Sign Up")
    print("3.Main Menu")
    print("=====================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        try:
            df = pd.read_csv("userdb.csv")
            username = input("Enter Username: ")
            if ind := list(df.index[df["username"] == username]):
                password = input("Enter Your Password: ").encode("utf-8")
                encoded_password = base64.b64encode(password)
                if str(encoded_password) == list(df.iloc[ind, 1])[0]:

                    play()
                    df.loc[ind[0], "score"] += MineBoard.score - 10
                    df.to_csv("userdb.csv", index=False)
                    MineBoard.score = 0
                    scoreboard()

                else:
                    print("Wrong Password. What would you like to do next?")
                    print("=====================")
                    print("1.Try Again")
                    print("2.Sign Up")
                    print("=====================")
                    choice = int(input())
                    if choice == 1:
                        login()
                    elif choice == 2:
                        signup()
                    else:
                        print(
                            "Oops! I didn't understand. So I will take you back to main menu :)"
                        )
            else:
                print("sorry! User not found. What would you like to do next?")
                print("=====================")
                print("1.Try Again")
                print("2.Sign Up")
                print("=====================")
                choice = int(input())
                if choice == 1:
                    login()
                elif choice == 2:
                    signup()
                else:
                    print(
                        "Oops! I didn't understand. So I will take you back to main menu :)"
                    )
        except FileNotFoundError:
            print("Sorry! No user Found. Sign up first")
            main()
    elif choice == 2:
        signup()
    elif choice == 3:
        main()
    else:
        print("Oops! I didn't understand. So I will take you back to main menu :)")
        main()


#   score board - done
def scoreboard():
    try:
        df = pd.read_csv("userdb.csv")
        df.sort_values(
            ["score", "username"],
            axis=0,
            ascending=[False, True],
            inplace=True,
            na_position="last",
        )
        df.to_csv(
            path_or_buf="userdb.csv",
            sep=",",
            na_rep="",
            float_format=None,
            columns=None,
            header=True,
            index=False,
            index_label=None,
            mode="w",
            encoding=None,
            compression="infer",
            quoting=None,
            quotechar='"',
            line_terminator=None,
            chunksize=None,
            date_format=None,
            doublequote=True,
            escapechar=None,
            decimal=".",
            errors="strict",
            storage_options=None,
        )
        df = pd.read_csv("userdb.csv")
        df = df[["username", "score"]]
        df.index += 1
        print(tabulate(df, headers=["Rank", "Username", "Score"], tablefmt="pretty"))
        print("Select your next Choice:")
        print("1.Main Menu")
        print("2.Exit")
        choice = int(input())
        if choice == 1:
            main()
        elif choice == 2:
            sys.exit()
    except FileNotFoundError:
        print("No user found! Do some progress first...")
        main()


if __name__ == "__main__":
    main()