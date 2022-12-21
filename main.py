# This a game where to object is to match uppercase and
# lowercase letters hidden behind numbered cards. The
# player chooses a pair of numbers to try and guess
# upper and lowercase matches.

# The inspiration and purpose for this program was to
# help my grand kids with the alphabet and the numbers.

# The terminal should be be maximized for better
# readability and alignment.


# Importing random and time
import random
import time

# Importing modules to draw screen template cards
import draw_screen_pick
import draw_screen_try
import draw_screen_great
import draw_screen_win

# Importing modules for distinguishing cards chosen
import flash_number


# This function takes a list of capital letters and
# Returns a list 5 random uppercase letters and
# Their lowercase counterparts
def get_ltrs_board(a_list):  # pass in letters
    '''
    Passes in a list of letters and returns five uppercase
    and five lowercase letters in randow order in a list
    '''
    # Gets 5 random sample from variable a_list
    r_a_list = (random.sample((a_list), 5))
    # Storing empty list case_a_r_list rand_alpha_list
    case_a_r_list = []
    rand_alpha_list = []
    # Loop though each letter in random sample to store
    # its uppercase and lowercase counter part in case_a_r_list
    for i in r_a_list:
        case_a_r_list.append(i.upper())
        case_a_r_list.append(i.lower())
    # Mixing up the uppercase and lowercase
    random.shuffle(case_a_r_list)
    random.shuffle(rand_alpha_list)  # test
    # Returning randomized list
    return case_a_r_list


def ask_for_pair(matches_left):  # pass in
    # repeat variable controlling while loop
    repeat_1 = "false"
    repeat_2 = "false"
    # variables for storing player input
    choice_1 = 0
    choice_2 = 0
    # Draw pick screen from import with updated card board
    draw_screen_pick.print_pick(current_board_list)
    # print(answer_list) # comment out for answers
    print("Can you find the match?")
    # While will loop until true in set in repeat_1
    while repeat_1 == "false":
        # store user input
        choice_1 = input("Enter your first choice!")
        # error handling for if the user enters more than one number
        # slice takes only the first number
        choice_1 = choice_1[:1]
        # if statement for quitting program
        if choice_1 == "q" or choice_1 == "Q":
            print("Thank you for playing!")
            exit()
        # try for handling non number input errors
        try:
            # convert string to number
            choice_1 = int(choice_1)
        except:
            # print error message with current board
            draw_screen_try.print_try_pick(current_board_list)
            print("Please enter a number! Try again!\n")
            # start loop again
            continue
        # check if number is already chosen
        if current_board_list[choice_1] not in original_board_list:
            draw_screen_try.print_try_pick(current_board_list)
            print("Number already chosen! Try again!\n")
        else:
            # Flip number on the board
            current_board_list[choice_1] = answer_list[choice_1]
            # user flash message for import to highlight the choice
            flash_number.flashNumber(choice_1, answer_list[choice_1], current_board_list)
            # Set repeat to true to end loop
            repeat_1 = "true"

    # While will loop until true in set in repeat_2
    while repeat_2 == "false":
        # store user input
        choice_2 = input("Enter your second choice!")
        # error handling for if the user enters more than one number
        # slice takes only the first number
        choice_2 = choice_2[:1]
        # if statement for quitting program
        if choice_2 == "q" or choice_2 == "Q":
            print("Thank you for playing!")
            exit()
        # try for handling non number input errors
        try:
            # convert string to number
            choice_2 = int(choice_2)
        except:
            # print error message with current board
            draw_screen_try.print_try_pick(current_board_list)
            print("Please enter a number! Try again!\n")
            # start loop again
            continue
        # check if number is the same as choice 1
        if choice_1 == choice_2:
            draw_screen_try.print_try_pick(current_board_list)
            print("Same number chosen!  Try again!\n")
            # start loop again
            continue
        # check if number is already chosen
        if current_board_list[choice_2] not in original_board_list:
            draw_screen_try.print_try_pick(current_board_list)
            print("Number already chosen! Try again!\n")
            # start loop again
            continue
        # Flip second number on the board
        current_board_list[choice_2] = answer_list[choice_2]
        # user flash message for import to highlight the choice
        flash_number.flashNumber(choice_2, answer_list[choice_2], current_board_list)
        # check if upper and lowercase letters match
        if answer_list[choice_1].lower() == answer_list[choice_2].lower():
            # Leave cards flipped and display message match found
            draw_screen_great.print_great_job(current_board_list)
            print("You found a match!")
            time.sleep(3)
            # subtract 2 from the number of available choices left to choose
            matches_left -= 2
            # Set repeat to true to end loop
            repeat_2 = "true"
        else:
            draw_screen_try.print_try_pick(current_board_list)
            print("Sorry, wrong answers!\n")
            # revert current_board_list to state before choices
            current_board_list[choice_1] = str(choice_1)
            current_board_list[choice_2] = str(choice_2)
            # Timer to wait so player can view their choices
            time.sleep(3)
            # Set repeat to true to end loop
            repeat_2 = "true"
    # return the value matches_left to keep track of choices left
    # keeps this local variable from an unbound error
    return matches_left


# list of letters to randomize - can be modified to focus on a 
# specific letters
alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]


# this board list compares to current board
original_board_list = ["0", "1", "2", "3", "4",
                       "5", "6", "7", "8", "9"]
# this board is to keep track of what been chosen
current_board_list = ["0", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9"]
# global variable to keep track of the choice left
# to determine whether the game is over
matches_available = 10

# call function to get randomized letters
answer_list = get_ltrs_board(alphabet_list)  # answers for grid
# while loop runs ask_for_pair until the game is over
while matches_available > 0:
    matches_available = ask_for_pair(matches_available)
# Draws final board - user wins
draw_screen_win.print_you_win(current_board_list)
