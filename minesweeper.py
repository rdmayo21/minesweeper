import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        """
        Initialize the Minesweeper game.
        :param width: Width of the game board
        :param height: Height of the game board
        :param num_mines: Number of mines to place on the board
        """
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = None
        self.visible = None
        self.flagged = None
        self.create_board()

    def create_board(self):
        """
        Create the game board with mines and numbers.
        """
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.visible = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.flagged = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        """
        Randomly place mines on the board.
        """
        mines_placed = 0
        while mines_placed < self.num_mines:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.board[y][x] != -1:
                self.board[y][x] = -1
                mines_placed += 1

    def calculate_numbers(self):
        """
        Calculate the numbers for each cell based on adjacent mines.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1:
                    count = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < self.height and 0 <= nx < self.width and self.board[ny][nx] == -1:
                                count += 1
                    self.board[y][x] = count

    def reveal_cell(self, x, y):
        """
        Reveal a cell on the board.
        :param x: X-coordinate of the cell
        :param y: Y-coordinate of the cell
        :return: True if the game should continue, False if a mine was revealed
        """
        if self.board[y][x] == -1:
            return False
        
        self.visible[y][x] = True
        if self.board[y][x] == 0:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width and not self.visible[ny][nx]:
                        self.reveal_cell(nx, ny)
        return True

    def flag_cell(self, x, y):
        """
        Flag or unflag a cell on the board.
        :param x: X-coordinate of the cell
        :param y: Y-coordinate of the cell
        """
        if not self.visible[y][x]:
            self.flagged[y][x] = not self.flagged[y][x]

    def check_win(self):
        """
        Check if the player has won the game.
        :return: True if the player has won, False otherwise
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1 and not self.visible[y][x]:
                    return False
        return True

    def print_board(self):
        """
        Print the current state of the game board.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.flagged[y][x]:
                    print('F', end=' ')
                elif not self.visible[y][x]:
                    print('.', end=' ')
                elif self.board[y][x] == -1:
                    print('*', end=' ')
                elif self.board[y][x] == 0:
                    print(' ', end=' ')
                else:
                    print(self.board[y][x], end=' ')
            print()

def play_game():
    """
    Main function to play the Minesweeper game.
    """
    width, height, num_mines = 10, 10, 15
    game = Minesweeper(width, height, num_mines)
    
    while True:
        game.print_board()
        action = input("Enter action (r/f) and coordinates (x y): ").split()
        if len(action) != 3:
            print("Invalid input. Please try again.")
            continue
        
        act, x, y = action[0].lower(), int(action[1]), int(action[2])
        
        if act == 'r':
            if not game.reveal_cell(x, y):
                print("Game Over! You hit a mine.")
                game.print_board()
                break
            if game.check_win():
                print("Congratulations! You won!")
                game.print_board()
                break
        elif act == 'f':
            game.flag_cell(x, y)
        else:
            print("Invalid action. Use 'r' to reveal or 'f' to flag/unflag.")

if __name__ == "__main__":
    play_game()
