import os
import time
import draw_screen_pick

# orig=position_number, choice=flippe_letter, c_list=current_list
# Mo
def flashNumber(orig,choice,c_list):
    '''
    flashNumber - displays acsii characters over the number in the
    card to simulate the letter turning to highlight the choice the 
    user has chosen
    (orig=position_number, choice=flippe_letter, c_list=current_list)
    '''
    # print(c_list) # test to compare list when flashed
    c_list_a = c_list
    t = 0.4
    btime = range(1)
    for i in btime:
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = str(choice)
        draw_screen_pick.print_pick(c_list_a)
        # c_list_a=clist[choice]= "*"
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = "-"
        draw_screen_pick.print_pick(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = " "
        draw_screen_pick.print_pick(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = "|"
        draw_screen_pick.print_pick(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = choice
        draw_screen_pick.print_pick(c_list_a)
        time.sleep(t)

# test_c_list = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
# flashNumber(2,"A",test_c_list)