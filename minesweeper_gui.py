import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from minesweeper import Minesweeper

class MinesweeperGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.game = Minesweeper(10, 10, 15)
        self.buttons = []
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(central_widget)

        for y in range(self.game.height):
            row = []
            for x in range(self.game.width):
                button = QPushButton()
                button.setFixedSize(30, 30)
                button.setContextMenuPolicy(Qt.CustomContextMenu)
                button.customContextMenuRequested.connect(lambda pos, x=x, y=y: self.flag_cell(x, y))
                button.clicked.connect(lambda _, x=x, y=y: self.reveal_cell(x, y))
                grid_layout.addWidget(button, y, x)
                row.append(button)
            self.buttons.append(row)

    def reveal_cell(self, x, y):
        if not self.game.reveal_cell(x, y):
            self.game_over()
        else:
            self.update_board()
            if self.game.check_win():
                self.game_won()

    def flag_cell(self, x, y):
        self.game.flag_cell(x, y)
        self.update_board()

    def update_board(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                visible, flagged, value = self.game.get_cell_state(x, y)
                button = self.buttons[y][x]
                if flagged:
                    button.setText("🚩")
                elif visible:
                    if value == -1:
                        button.setText("💣")
                    elif value == 0:
                        button.setText("")
                    else:
                        button.setText(str(value))
                else:
                    button.setText("")

    def game_over(self):
        self.game.reveal_all()
        self.update_board()
        QMessageBox.information(self, "Game Over", "You hit a mine! Game Over.")
        self.reset_game()

    def game_won(self):
        QMessageBox.information(self, "Congratulations", "You won the game!")
        self.reset_game()

    def reset_game(self):
        self.game = Minesweeper(10, 10, 15)
        self.update_board()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinesweeperGUI()
    window.show()
    sys.exit(app.exec_())
