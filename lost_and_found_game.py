"""
File:    lost_and_found.py
Description: This program is a game, in which the user needs to reach the X. To do that they must go through doors (some of which have
keys that need to be searched for.) They also can find hidden doors called secrets.
"""

 
import json
 
 
USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'x'
DOOR = 'd'
SECRET = 's'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'
PLAYER = '\u1330'
 
 
def play_game():
    # Declaring x and y positions for map
    xpos = 0
    ypos = 0
    def load_map(map_file_name):
        """
        param: takes in the map you want to test
        return: returns usable the map after it is read
        """
        with open(map_file_name) as map_file:
            the_map = json.loads(map_file.read())
 
        return the_map
   
    #taking in user input
    map_file_name = input('What map do you want to load? ')
    the_game_map = load_map(map_file_name)


    def display_map(the_grid):
        """
        param: Takes in the map that you want to use
        output: Prints out the map in grid format, and prints player movement, and handles game functions, such as doors, secrets etc.
        """
        xpos = 0
        ypos = 0
        inventory = []
        # Prints out map, and player movement
        while the_grid[ypos][xpos]['symbol'] != EXIT:
            for row in range(len(the_grid)):
                for col in range(len(the_grid[row])):
                    if col == xpos and row == ypos:
                        print(PLAYER, end=' ')
                    elif the_grid[row][col]['symbol'] == SECRET:
                        print(WALL, end=' ')
                    elif the_grid[row][col]['items']:
                        print(ITEMS, end=' ')
                    elif the_grid[row][col]['symbol'] == FLOOR:
                        print(FLOOR, end=' ')
                    else:
                        print(the_grid[row][col]['symbol'], end=' ')
                print()

            print("x pos is " + str(xpos) + " y pos is " + str(ypos))
            # Adding collected items to list, and removing i's            
            if the_grid[ypos][xpos]['items']:
                if the_grid[ypos][xpos]['items'] not in inventory:
                    inventory.append(the_grid[ypos][xpos]['items'])
                the_grid[ypos][xpos]['items'] = []
            print("Your inventory is: " + str(inventory))
            # Taking in user input for movement
            move = input("Enter Move (wasd) (e to activate doors or secrets):")
            # Function for opening doors and secrets when e is pressed
            if move == 'e':
            # Opening doors that have key requirements
                if (ypos > 0) and the_grid[ypos -1][xpos]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos-1][xpos]:
                        if the_grid[ypos-1][xpos]['requires'] in inventory:
                            if the_grid[ypos-1][xpos]['symbol'] == DOOR:
                                the_grid[ypos -1][xpos]['symbol'] = FLOOR
                        else:
                            print("You dont have the key")

                if (ypos < (len(the_grid) -1)) and the_grid[ypos +1][xpos]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos+1][xpos]:
                        if the_grid[ypos+1][xpos]['requires'] in inventory:
                            if the_grid[ypos+1][xpos]['symbol'] == DOOR:
                                the_grid[ypos +1][xpos]['symbol'] = FLOOR
                        else:
                            print("You dont have the key")

                if (xpos > 0) and the_grid[ypos][xpos -1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos][xpos-1]:
                        if the_grid[ypos][xpos-1]['requires'] in inventory:
                            if the_grid[ypos][xpos-1]['symbol'] == DOOR:
                                the_grid[ypos][xpos -1]['symbol'] = FLOOR
                        else:
                            print("You dont have the key")
                
                if (xpos < (len(the_grid[row]) -1)) and the_grid[ypos][xpos +1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos][xpos+1]:
                        if the_grid[ypos][xpos+1]['requires'] in inventory:
                            if the_grid[ypos][xpos+1]['symbol'] == DOOR:
                                the_grid[ypos][xpos +1]['symbol'] = FLOOR
                        else:
                            print("You dont have the key")
                
                if (ypos > 0) and (xpos < (len(the_grid[row]) -1)) and the_grid[ypos-1][xpos +1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos-1][xpos+1]:
                        if the_grid[ypos-1][xpos+1]['requires'] in inventory:
                            if the_grid[ypos-1][xpos+1]['symbol'] == DOOR:
                                the_grid[ypos-1][xpos +1]['symbol'] = FLOOR
                            else:
                                print("You dont have the key")
                
                if (ypos < (len(the_grid) -1)) and (xpos > 0) and the_grid[ypos+1][xpos -1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos+1][xpos-1]:
                        if the_grid[ypos+1][xpos-1]['requires'] in inventory:
                            if the_grid[ypos+1][xpos -1]['symbol'] == DOOR:
                                the_grid[ypos+1][xpos -1]['symbol'] = FLOOR
                            else:
                                print("You dont have the key")
                
                if (ypos > 0) and (xpos > 0) and the_grid[ypos-1][xpos -1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos-1][xpos-1]:
                        if the_grid[ypos-1][xpos-1]['requires'] in inventory:
                            if the_grid[ypos-1][xpos-1]['symbol'] == DOOR:
                                the_grid[ypos-1][xpos -1]['symbol'] = FLOOR
                        else:
                            print("You dont have the key")
                
                if (ypos < (len(the_grid) -1)) and (xpos < (len(the_grid[row]) -1)) and the_grid[ypos+1][xpos +1]['symbol'] != EXIT:
                    if 'requires' in the_grid[ypos+1][xpos+1]:
                        if the_grid[ypos+1][xpos+1]['requires'] in inventory:
                            if the_grid[ypos+1][xpos+1]['symbol'] == DOOR:
                                the_grid[ypos+1][xpos +1]['symbol'] = FLOOR
                            else:
                                print("You dont have the key")

                # Opening doors that do not have key requirements
                if (ypos > 0) and the_grid[ypos -1][xpos]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos-1][xpos]:
                        if the_grid[ypos-1][xpos]['symbol'] == DOOR:
                            the_grid[ypos -1][xpos]['symbol'] = FLOOR
                
                if (ypos < (len(the_grid) -1)) and the_grid[ypos +1][xpos]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos+1][xpos]:
                        if the_grid[ypos+1][xpos]['symbol'] == DOOR:
                            the_grid[ypos +1][xpos]['symbol'] = FLOOR
                
                if (xpos > 0) and the_grid[ypos][xpos -1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos][xpos-1]:
                        if the_grid[ypos][xpos-1]['symbol'] == DOOR:
                            the_grid[ypos][xpos -1]['symbol'] = FLOOR
                
                if (xpos < (len(the_grid[row]) -1)) and the_grid[ypos][xpos +1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos][xpos+1]:
                        if the_grid[ypos][xpos+1]['symbol'] == DOOR:
                            the_grid[ypos][xpos +1]['symbol'] = FLOOR
                
                if (ypos > 0) and (xpos < (len(the_grid[row]) -1)) and the_grid[ypos-1][xpos +1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos-1][xpos+1]:
                        if the_grid[ypos-1][xpos+1]['symbol'] == DOOR:
                            the_grid[ypos-1][xpos +1]['symbol'] = FLOOR
                
                if (xpos > 0) and (ypos < (len(the_grid) -1)) and the_grid[ypos+1][xpos -1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos+1][xpos-1]:
                        if the_grid[ypos+1][xpos -1]['symbol'] == DOOR:
                            the_grid[ypos+1][xpos -1]['symbol'] = FLOOR
                
                if (xpos > 0) and (ypos > 0) and the_grid[ypos-1][xpos -1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos-1][xpos-1]:
                        if the_grid[ypos-1][xpos-1]['symbol'] == DOOR:
                            the_grid[ypos-1][xpos -1]['symbol'] = FLOOR
                
                if (xpos < (len(the_grid[row]) -1)) and (ypos < (len(the_grid) -1)) and the_grid[ypos+1][xpos +1]['symbol'] != EXIT:
                    if 'requires' not in the_grid[ypos+1][xpos+1]:
                        if the_grid[ypos+1][xpos+1]['symbol'] == DOOR:
                            the_grid[ypos+1][xpos +1]['symbol'] = FLOOR
                # Opening secrets
                if (ypos > 0) and the_grid[ypos -1][xpos]['symbol'] != EXIT:
                    if the_grid[ypos-1][xpos]['symbol'] == SECRET:
                        the_grid[ypos -1][xpos]['symbol'] = FLOOR
                if (ypos < (len(the_grid) -1)) and the_grid[ypos +1][xpos]['symbol'] != EXIT:
                    if the_grid[ypos+1][xpos]['symbol'] == SECRET:
                        the_grid[ypos +1][xpos]['symbol'] = FLOOR
                if (xpos > 0) and the_grid[ypos][xpos -1]['symbol'] != EXIT:
                    if the_grid[ypos][xpos-1]['symbol'] == SECRET:
                        the_grid[ypos][xpos -1]['symbol'] = FLOOR
                if (xpos < (len(the_grid[row]) -1)) and the_grid[ypos][xpos +1]['symbol'] != EXIT:
                    if the_grid[ypos][xpos+1]['symbol'] == SECRET:
                        the_grid[ypos][xpos +1]['symbol'] = FLOOR
                if (ypos > 0) and (xpos < (len(the_grid[row]) -1)) and the_grid[ypos-1][xpos +1]['symbol'] != EXIT:
                    if the_grid[ypos-1][xpos+1]['symbol'] == SECRET:
                        the_grid[ypos-1][xpos +1]['symbol'] = FLOOR
                if (xpos > 0) and (ypos < (len(the_grid) -1)) and the_grid[ypos+1][xpos -1]['symbol'] != EXIT:
                    if the_grid[ypos+1][xpos-1]['symbol'] == SECRET:
                        the_grid[ypos+1][xpos -1]['symbol'] = FLOOR
                if (xpos > 0) and (ypos > 0) and the_grid[ypos-1][xpos -1]['symbol'] != EXIT:
                    if the_grid[ypos-1][xpos-1]['symbol'] == SECRET:
                        the_grid[ypos-1][xpos -1]['symbol'] = FLOOR
                if (xpos < (len(the_grid[row]) -1)) and (ypos < (len(the_grid) -1)) and the_grid[ypos+1][xpos +1]['symbol'] != EXIT:
                    if the_grid[ypos+1][xpos+1]['symbol'] == SECRET:
                        the_grid[ypos+1][xpos+1]['symbol'] = FLOOR
            # Up player movement
            elif move == 'w' and (ypos > 0):
                if the_grid[ypos -1][xpos]['symbol'] != WALL and the_grid[ypos-1][xpos]['symbol'] != DOOR and the_grid[ypos-1][xpos]['symbol'] != SECRET:
                    ypos = ypos -1
            # Down player movement   
            elif move == 's' and (ypos < (len(the_grid) -1)):
                if the_grid[ypos +1][xpos]['symbol']  != WALL and the_grid[ypos +1][xpos]['symbol'] != DOOR and the_grid[ypos +1][xpos]['symbol'] != SECRET:
                    ypos = ypos +1
            # left player movement   
            elif move == 'a' and (xpos > 0):
                if the_grid[ypos][xpos -1]['symbol']  != WALL and the_grid[ypos][xpos -1]['symbol'] != DOOR and the_grid[ypos][xpos -1]['symbol'] != SECRET:
                    xpos = xpos -1
            # right player movement    
            elif move == 'd' and (xpos < (len(the_grid[row]) -1)):
                if the_grid[ypos][xpos +1]['symbol']  != WALL and the_grid[ypos][xpos +1]['symbol'] != DOOR and the_grid[ypos][xpos +1]['symbol'] != SECRET:
                    xpos = xpos +1
        # statement that is printed when player gets to X
        print("You win.")
    #Calls the inner function
    display_map(the_game_map)

 
if __name__ == '__main__':
    # Calling the function in main method
    play_game()
