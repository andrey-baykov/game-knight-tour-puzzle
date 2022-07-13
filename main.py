class Game:
    '''
    Matrix (x, y): x - horizontal, y - vertical
    Moves (x, y)
    '''
    matrix = []
    board_dimension = None
    cell_size = 0
    last_move = tuple()
    possible_moves = [(2, 1),
                      (1, 2),
                      (-1, 2),
                      (-2, 1),
                      (-2, -1),
                      (-1, -2),
                      (1, -2),
                      (2, -1)
                      ]

    def __init__(self, board_dimension):
        self.board_dimension = board_dimension
        self.cell_size = len(str(board_dimension[0] * board_dimension[1]))
        line = ["_" * self.cell_size for x in range(self.board_dimension[0])]
        for _ in range(self.board_dimension[1]):
            self.matrix.append(line.copy())

    def set_position(self, position) -> None:
        if self.is_position_clear(position):
            x, y = position
            self.matrix[y - 1][x - 1] = " " * (self.cell_size - 1) + "X"
            self.last_move = position

    def is_position_clear(self, position) -> bool:
        x, y = position
        if self.matrix[y - 1][x - 1] == "_" * self.cell_size:
            return True
        return False

    def print_current_field(self) -> None:
        m = self.matrix

        print(f" " + "-" * (self.board_dimension[0] * (self.cell_size + 1) + 3))
        for x in range(self.board_dimension[1], 0, -1):
            line = x
            x = " " * (len(str(self.board_dimension[1])) - len(str(x))) + str(x)
            cells_str = " ".join([cell for cell in m[line - 1]])
            print(f"{x}| " + cells_str + " |")

        print(f" " + "-" * (self.board_dimension[0] * (self.cell_size + 1) + 3))
        last_str = " ".join(
            [" " * (self.cell_size - len(str(x + 1))) + str(x + 1) for x in range(self.board_dimension[0])])
        print(f"   {last_str}")

    def check_possible_move(self):
        start_x = self.last_move[0] - 1
        start_y = self.last_move[1] - 1
        for move in self.possible_moves:
            new_x = start_x + move[0]
            new_y = start_y + move[1]
            if 0 <= new_x <= (self.board_dimension[1] - 1) and 0 <= new_y <= (self.board_dimension[0] - 1):
                self.matrix[new_x][new_y] = " " * (self.cell_size - 1) + "O"


def verify_input(input_string) -> bool:
    try:
        test_input = [int(x) for x in input_string.split()]
    except ValueError:
        print("Invalid dimensions!")
        return False
    if len(test_input) != 2:
        print("Invalid dimensions!")
        return False
    if 1 <= test_input[0] <= game.board_dimension[0] and 1 <= test_input[1] <= game.board_dimension[1]:
        return True
    print("Invalid dimensions!")
    return False


def verify_board_size(input_string) -> bool:
    try:
        test_input = [int(x) for x in input_string.split()]
    except ValueError:
        print("Invalid dimensions!")
        return False
    if len(test_input) != 2:
        print("Invalid dimensions!")
        return False
    if test_input[0] > 0 and test_input[1] > 0:
        return True
    print("Invalid dimensions!")
    return False


start_set = False
board = False
user_input = None
board_size = None
while not board:
    board_size = input("Enter your board dimensions: ")
    board = verify_board_size(board_size)
game = Game(tuple([int(x) for x in board_size.split()]))
while not start_set:
    user_input = input("Enter the knight's starting position: ")
    start_set = verify_input(user_input)
start = tuple([int(x) for x in user_input.split()])
game.set_position(start)
game.check_possible_move()
game.print_current_field()
