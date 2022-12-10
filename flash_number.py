import os
import time
import draw_screen_pick

def flashNumber(orig,choice,c_list):
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(c_list)
    c_list_a = c_list
    t = 0.2
    btime = range(10)
    for i in btime:
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = str(choice)
        print(c_list_a)
        # c_list_a=clist[choice]= "*"
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = "-"
        print(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = " "
        print(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = "|"
        print(c_list_a)
        time.sleep(t)
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        c_list_a[orig] = choice
        print(c_list_a)
        time.sleep(t)

test_c_list = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
flashNumber(2,"A",test_c_list)