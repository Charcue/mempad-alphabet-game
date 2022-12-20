# This a game where to object is to match uppercase and
# lowercase letters hidden behind numbered cards. The
# player chooses a pair of numbers to try and guess 
# upper and lowercase matches.

# The inspiration and purpose for this program was to help
# my grand kids with the alphabet and the numbers.

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


def ask_for_pair():
    repeat_1 = "false"
    repeat_2 = "false"
    choice_1 = 0
    choice_2 = 0

    draw_screen_pick.print_pick(current_board_list)
    print(answer_list)
    print("Can you find the match?")
    while repeat_1 == "false":
        choice_1 = input("Enter your first choice!")
        if choice_1 == "q" or choice_1 == "Q":
            print("Thank you for playing!")
            exit()
        try:
            choice_1 = int(choice_1)
        except:
                draw_screen_try.print_try_pick(current_board_list)
                print("Please enter a number! Try again!\n")
                continue
        if current_board_list[choice_1] not in original_board_list:
            draw_screen_try.print_try_pick(current_board_list)
            print("Number already chosen! Try again!\n")
        else:
            # Flip second number
            current_board_list[choice_1] = answer_list[choice_1]
            flash_number.flashNumber(choice_1,answer_list[choice_1], current_board_list)
            repeat_1 = "true"

    while repeat_2 == "false":
        choice_2 = input("Enter your second choice!")
        if choice_2 == "q" or choice_2 == "Q":
            print("Thank you for playing!")
            exit()
        try:
            choice_2 = int(choice_2)
        except:
                draw_screen_try.print_try_pick(current_board_list)
                print("Please enter a number! Try again!\n")
                continue
        if choice_1 == choice_2:
            draw_screen_try.print_try_pick(current_board_list)
            print("Same number chosen!  Try again!\n")
            continue
        if current_board_list[choice_2] not in original_board_list:
            draw_screen_try.print_try_pick(current_board_list)
            print("Number already chosen! Try again!\n")
            continue
        # Flip second number
        current_board_list[choice_2] = answer_list[choice_2]
        flash_number.flashNumber(choice_2, answer_list[choice_2], current_board_list)
        if answer_list[choice_1].lower() == answer_list[choice_2].lower():
            draw_screen_great.print_great_job(current_board_list)
            print("You found a match!")
            time.sleep(3)
            repeat_2 = "true"
        else:
            draw_screen_try.print_try_pick(current_board_list)
            print("Sorry, wrong answers!\n")
            current_board_list[choice_1] = str(choice_1)
            current_board_list[choice_2] = str(choice_2)
            time.sleep(3)
            repeat_2 = "true"
    print(answer_list[choice_1])
    print(answer_list[choice_2])


alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]


original_board_list = ["0", "1", "2", "3", "4",
                       "5", "6", "7", "8", "9"]
current_board_list = ["0", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9"]

answer_list = get_ltrs_board(alphabet_list)  # answers for grid
ask_for_pair()
# for answer in answer_list:
for i in range(5):
    ask_for_pair()
    if current_board_list == answer_list:
        break
draw_screen_pick.print_pick(current_board_list)
draw_screen_win.print_you_win(current_board_list)
