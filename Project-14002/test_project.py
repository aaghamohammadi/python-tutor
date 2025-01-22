# run using pytest test_project.py via terminal.

from project import MineBoard

def test_display():
    mine = MineBoard(10, 10, 20)
    assert mine.display(9) == "x"
    assert mine.display(100) == "F"
    assert mine.display(10) == "."
    assert mine.display(2) == "*"

def test_GameStat():
    mine = MineBoard(15, 15, 75)
    assert mine.winGame() == False
    assert mine.loseGame() == False

def test_isOver():
    mine = MineBoard(25, 25, 100)
    assert mine.isOver() == False

def test_isValidCell():
    mine = MineBoard(5, 5, 10)
    assert mine.isValidCell(4, 3) == True
    assert mine.isValidCell(14, 3) == False