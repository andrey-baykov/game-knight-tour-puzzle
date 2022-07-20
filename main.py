class Game:
    """

    Matrix (x, y): x - horizontal, y - vertical
    Moves (x, y)
    Matrix[y][x] !!!!

    """

    def __init__(self, board_dimension):
        self.matrix = []
        self.board_dimension = {'x': 0, 'y': 0}
        self.cell_size = 0
        self.last_move = tuple()
        self.possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        self.board_dimension['x'] = board_dimension[0]
        self.board_dimension['y'] = board_dimension[1]
        self.cell_size = len(str(self.board_dimension['x'] * self.board_dimension['y']))
        line = ["_" * self.cell_size for x in range(self.board_dimension['x'])]
        for _ in range(self.board_dimension['y']):
            self.matrix.append(line.copy())

    def set_position(self, position, symbol='X') -> None:
        x, y = position
        self.matrix[y][x] = " " * (self.cell_size - 1) + symbol
        # self.last_move = position

    def is_position_clear(self, position) -> bool:
        x, y = position
        if self.matrix[y][x] == "_" * self.cell_size:
            return True
        return False

    def print_current_field(self) -> None:
        m = self.matrix

        print(f" " + "-" * (self.board_dimension['x'] * (self.cell_size + 1) + 3))
        for x in range(self.board_dimension['y'], 0, -1):
            line = x
            x = " " * (len(str(self.board_dimension['y'])) - len(str(x))) + str(x)
            cells_str = " ".join([cell for cell in m[line - 1]])
            print(f"{x}| " + cells_str + " |")

        print(f" " + "-" * (self.board_dimension['x'] * (self.cell_size + 1) + 3))
        last_str = " ".join(
            [" " * (self.cell_size - len(str(x + 1))) + str(x + 1) for x in range(self.board_dimension['x'])])
        print(f"   {last_str}")

    def check_possible_move(self, position, depth):
        start_x = position[0]
        start_y = position[1]
        for move in self.possible_moves:
            new_x = start_x + move[0]
            new_y = start_y + move[1]
            if 0 <= new_x <= (self.board_dimension['x'] - 1) and 0 <= new_y <= (self.board_dimension['y'] - 1):
                pos = [new_x, new_y]
                symbol = self.check_count_of_possible_move(pos, depth)
                self.set_position(pos, str(symbol))

    def check_count_of_possible_move(self, position, iterations) -> int:
        output = 0
        if iterations == 0:
            return output
        start_x = position[0]
        start_y = position[1]
        for move in self.possible_moves:
            new_x = start_x + move[0]
            new_y = start_y + move[1]
            if 0 <= new_x <= (self.board_dimension['x'] - 1) and 0 <= new_y <= (self.board_dimension['y'] - 1):
                if self.matrix[new_y][new_x].find('X') == -1 and self.matrix[new_y][new_x].find('*') == -1:
                    output += 1
        return output


def get_position_indexes(position) -> tuple:
    x = position[0] - 1
    y = position[1] - 1
    output = [x, y]
    return tuple(output)


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


def verify_input(input_string, board_dimensions) -> bool:
    try:
        test_input = [int(x) for x in input_string.split()]
    except ValueError:
        print("Invalid dimensions!")
        return False
    if len(test_input) != 2:
        print("Invalid dimensions!")
        return False
    if 1 <= test_input[0] <= board_dimensions[0] and 1 <= test_input[1] <= board_dimensions[1]:
        return True
    print("Invalid dimensions!")
    return False


def main():
    start_set = False
    board = False
    user_input = None
    board_size = None
    while not board:
        input_board_size = input("Enter your board dimensions: ")
        board = verify_board_size(input_board_size)
        if board:
            board_size = tuple([int(x) for x in input_board_size.split()])
    game = Game(board_size)
    while not start_set:
        user_input = input("Enter the knight's starting position: ")
        start_set = verify_input(user_input, board_size)
    start = get_position_indexes(tuple([int(x) for x in user_input.split()]))
    game.set_position(start)
    game.last_move = start
    game.check_possible_move(game.last_move, 1)
    game.print_current_field()


if __name__ == '__main__':
    main()
