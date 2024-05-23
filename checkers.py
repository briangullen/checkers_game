from numpy import random, ndarray


def build_board(given_size: int) -> ndarray:
    size = given_size
    staring_board = random.choice(['red', 'black', 'empty'], (size, size))
    return staring_board


def get_count(board_name, color):
    if color == 'red':
        total_color = board_name == 'red'
    if color == 'black':
        total_color = board_name == 'black'
    if color == 'empty':
        total_color = board_name == 'empty'
    return total_color.sum()


if __name__ == '__main.py__':
    print('Running checkers.py directly')
