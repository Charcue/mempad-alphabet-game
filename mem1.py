import random
import time
import draw_screen_pick
import draw_screen_try
import draw_screen_great
import draw_screen_win
import flash_number


def alpha_figures():
    A_fig1 = "    _    "
    A_fig2 = "   / \\   "
    A_fig3 = "  / _ \\  "
    A_fig4 = " / ___ \\ "
    A_fig5 = "/_/   \\_\\"

    print(A_fig1)
    print(A_fig2)
    print(A_fig3)
    print(A_fig4)
    print(A_fig5)


def draw_grid(board):
    print("\n")
    print("\t   |   |")
    print("\t {} | {} | {}".format(board[3][0], board[3][1], board[3][2]))
    print("\t___|___|___")
    print("\t   |   |")
    print("\t {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t___|___|___")
    print("\t   |   |")
    print("\t {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print("\t___|___|___")
    print("\t   |   |")
    print("\t   | {} |".format(board[0][1]))
    print("\t   |   |   ")
    print("\n")


def get_ltrs_board(a_list):  # pass in letters
    '''
    Passes in a list of letters and returns five uppercase
    and five lowercase letters in randow order in a list
    '''
    r_a_list = (random.sample((a_list), 5))
    case_a_r_list = []
    rand_alpha_store = a_list
    # print(a_list)
    # print(r_a_list)
    rand_alpha_list = []
    for i in r_a_list:
        # print(i.upper(),i.lower())
        case_a_r_list.append(i.upper())
        case_a_r_list.append(i.lower())
    # random.shuffle(rand_alpha_store)
    random.shuffle(case_a_r_list)
    #
    # print()
    # print(case_a_r_list)  # test
    random.shuffle(rand_alpha_list)  # test
    # print(random.sample((range(10)), 10))  # test
    ##############################
    return case_a_r_list


def fill_cards(f_board):
    ans_board = [[" ", "0", " "],
                 ["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "9"]]

    ans_board[0][1] = f_board[0]
    ans_board[1][0] = f_board[1]
    ans_board[1][1] = f_board[2]
    ans_board[1][2] = f_board[3]
    ans_board[2][0] = f_board[4]
    ans_board[2][1] = f_board[5]
    ans_board[2][2] = f_board[6]
    ans_board[3][0] = f_board[7]
    ans_board[3][1] = f_board[8]
    ans_board[3][2] = f_board[9]
    # draw_grid(ans_board)
    return ans_board


def ask_for_pair():
    repeat_1 = "false"
    repeat_2 = "false"
    choice_1 = 0
    choice_2 = 0

    draw_screen_pick.print_pick(current_board_list)
    # print(current_board_list)
    print(answer_list)
    print("Can you find the match?")
    while repeat_1 == "false":
        choice_1 = int(input("Enter your first choice!"))
        if current_board_list[choice_1] not in original_board_list:
            print("Try again!")
            draw_screen_try.print_try_pick(current_board_list)
        else:
            # Flip second number
            current_board_list[choice_1] = answer_list[choice_1]
            # print(current_board_list)
            flash_number.flashNumber(choice_1,answer_list[choice_1], current_board_list)
            repeat_1 = "true"
        # draw_screen_pick.print_pick(current_board_list)

    while repeat_2 == "false":
        choice_2 = int(input("Enter your second choice!"))
        if choice_1 == choice_2:
            print("Same number chosen!  Try again!\n")
            draw_screen_try.print_try_pick(current_board_list)
            continue
        if current_board_list[choice_2] not in original_board_list:
            print("Try again!")
            draw_screen_try.print_try_pick(current_board_list)
            continue
        # Flip second number
        current_board_list[choice_2] = answer_list[choice_2]
        # draw_screen_pick.print_pick(current_board_list)
        flash_number.flashNumber(choice_2,answer_list[choice_2], current_board_list)
        # print(current_board_list)
        if answer_list[choice_1].lower() == answer_list[choice_2].lower():
            print("Yes!")
            draw_screen_great.print_great_job(current_board_list)
            time.sleep(3)
            repeat_2 = "true"
        else:
            draw_screen_try.print_try_pick(current_board_list)
            print("Sorry, wrong answers!")
            current_board_list[choice_1] = str(choice_1)
            current_board_list[choice_2] = str(choice_2)
            time.sleep(3)
            repeat_2 = "true"
    print(answer_list[choice_1])
    print(answer_list[choice_2])


alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]

board = [[" ", "0", " "],
         ["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

original_board_list = ["0", "1", "2", "3", "4",
                       "5", "6", "7", "8", "9"]
current_board_list = ["0", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9"]

draw_screen_pick.print_pick(current_board_list)
# alpha_figures()
answer_list = get_ltrs_board(alphabet_list)  # answers for grid
current_board = (fill_cards(answer_list))  # grid with answers to match
fill_cards(current_board_list)
# draw_grid(board)
# current_board = board[:]
# draw_grid(current_board)
ask_for_pair()
# for answer in answer_list:
for i in range(5):
    ask_for_pair()
    if current_board_list == answer_list:
        break
draw_screen_pick.print_pick(current_board_list)
draw_screen_win.print_you_win(current_board_list)