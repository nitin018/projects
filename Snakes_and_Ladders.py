"""
    Snakes and ladders
"""
import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6

def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid

def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c

def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)

user_input = input("Board Size and Seed:")
user_input = user_input.split()
seed = int(user_input[1])
size = int(user_input[0])



def printing_the_grid():
    map_list_storage = generate_random_map(size, seed)
    the_grid = []
    generate_random_map(size, seed)
    the_grid = make_grid(size)
    for z in range(size):
        fill_grid_square(the_grid, size, z, str(z) +"\n" + map_list_storage[z]) # displays index in each box
    for i in range(len(the_grid)):
        print(''.join(the_grid[i]))
        

def math_commands():
    position = 0
    score = 0
    get_map_list = []
    get_map_list = generate_random_map(size, seed)
    while get_map_list[position] != 'hlt':
        dice_simulation = roll_dice()
        position = (position + dice_simulation) % size
        word_split = get_map_list[position].split()
        print("Pos: " + str(position) + " Score: " + str(score) +  ", instruction " + get_map_list[position] + " Rolled: " + str(dice_simulation))
        if word_split[0] == 'jmp':
            position = int(word_split[1])
            if word_split[0] == 'mul':
                score *= int(word_split[1])
            elif word_split[0] == 'add':
                score += int(word_split[1])
            elif word_split[0] == 'sub':
                score -= int(word_split[1])
            print("Pos: " + str(position) + " Score: " + str(score) +  ", instruction " + get_map_list[position] + " Rolled: " + str(dice_simulation))

        elif word_split[0] == 'mul':
            score *= int(word_split[1])
        elif word_split[0] == 'add':
            score += int(word_split[1])
        elif word_split[0] == 'sub':
            score -= int(word_split[1])
    print("Final Pos: " + str(position) +" Final Score: " + str(score) + " , Instruction " + str(get_map_list[position]))


def play_again():
        global size
        global seed
        play_again_input = input("The game ended do you want to play again (yes or no):")
        if play_again_input == "yes":
            user_input = input("Board Size and Seed:")
            user_input = user_input.split()
            seed = int(user_input[1])
            size = int(user_input[0])
            play_game(printing_the_grid())
    

def play_game(game_map):
    math_commands()
    play_again()

if __name__ == '__main__':
    play_game(printing_the_grid())
