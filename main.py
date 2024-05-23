import checkers


# Checks if running as main and calls game
def check_main():
    if __name__ != 'main':
        game()


# Asks user for input and returns variable to be used in game
def get_input():
    while True:
        board_size = int(input('What size would you like the board to be? (4-16): '))
        if 4 <= board_size <= 16:
            break
        else:
            print("Sorry that number isn't from 4-16. Please try again.")
            continue
    return board_size


# Function to run main game
def game():
    new_board = checkers.build_board(get_input())
    print(new_board)
    total_red = checkers.get_count(new_board, "red")
    print(f'The total number of red squares is: {total_red}')
    total_black = checkers.get_count(new_board, "black")
    print(f'The total number of black squares is: {total_black}')
    total_emtpy = checkers.get_count(new_board, "empty")
    print(f'The total number of emtpy squares is: {total_emtpy}')


# Function defines order in which game executes
def main():
    check_main()


# Calls main function to run program
main()
