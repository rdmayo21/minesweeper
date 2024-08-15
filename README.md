# Minesweeper Game

This is a Python implementation of the classic Minesweeper game with a graphical user interface using PyQt5.

## Features

- Customizable game board (10x10 grid with 15 mines by default)
- Left-click to reveal cells
- Right-click to flag/unflag cells
- Automatic revealing of adjacent empty cells
- Win and lose conditions with appropriate messages

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install PyQt5
```

## How to Run

Run the game by executing the `minesweeper_gui.py` file:

```
python minesweeper_gui.py
```

## Files

- `minesweeper.py`: Contains the core game logic for Minesweeper.
- `minesweeper_gui.py`: Implements the graphical user interface using PyQt5.

## How to Play

1. Left-click on a cell to reveal it.
2. Right-click on a cell to flag it as a potential mine.
3. Try to reveal all non-mine cells to win the game.
4. If you reveal a mine, the game is over.

Enjoy playing Minesweeper!
