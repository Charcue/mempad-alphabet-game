import os
import time
import sys
# import keyboard
import random

# clear the screen
# os.system('cls' if os.name == 'nt' else 'clear')


# print to screen function
def print_to_screen(string):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(string)
    time.sleep(0.1)


# print to console function
def print_to_console(string):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(string)
    time.sleep(0.1)


# print the alphabet on the screen one letter at a time
def print_alphabet(string):
    for i in range(len(string)):
        print(string[i], end=' ')
        time.sleep(0.1)
        # if (i + 1) % 10 == 0:
        #     print('\n')
        #     time.sleep(0.1)


def print_alphabet1(string):
    for i in range(len(string)):
        print_to_console(string[i])
        time.sleep(0.2)
        if (i + 1) % 10 == 0:
            print('\n')
            time.sleep(0.1)


a = 'Lorem ipsum dolor sit amet'

# Default: { "─", "│", "─", "│", "╭", "╮", "╯", "╰" }
# print_to_console(a)'
# print the alphabet on the console one letter at a time
# print_alphabet(a)
# print_alphabet1(a)
# print_alphabet1('Hello World ')

o_list = ["0", "1", "2", "3", "4",
          "5", "6", "7", "8", "9"]

c= ["a", "A", "2", "3", "4",
    "5", "6", "7", "8", "9"]

def print_pick(c):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 5)
    print("  ╭─────╮  ╭─────╮  ╭─────╮              ____  _      _                                _ _            < hi >") 
    print("  │     │  │     │  │     │             |  _ \(_) ___| | __   __ _    ___ __ _ _ __ __| | |            ----") 
    print("  │  {}  │  │  {}  │  │  {}  │             | |_) | |/ __| |/ /  / _` |  / __/ _` | '__/ _` | |               \\       .".format( c[7],c[8],c[9]))
    print("  │     │  │     │  │     │             |  __/| | (__|   <  | (_| | | (_| (_| | | | (_| |_|                \\      l\\ /\\")
    print("  ╰─────╯  ╰─────╯  ╰─────╯             |_|   |_|\___|_|\_\  \__,_|  \___\__,_|_|  \__,_(_)                 \     !)Y.))")
    print("                                                                                                                 _\| //")
    print("  ╭─────╮  ╭─────╮  ╭─────╮                                                                                    ,/oo  \\")
    print("  │     │  │     │  │     │                                                                                 .-+    _ /")
    print("  │  {}  │  │  {}  │  │  {}  │                                                                                `-_--=-'/".format( c[4],c[5],c[6]))
    print("  │     │  │     │  │     │                                                                                      / /")
    print("  ╰─────╯  ╰─────╯  ╰─────╯                                                                                     /  \\_")
    print("                                                                                                               Y  .  )")
    print("  ╭─────╮  ╭─────╮  ╭─────╮                                                                              .--v--^--' /\"\\")
    print("  │     │  │     │  │     │                                                                              \\/~\\/~T\"--' _ \\")
    print("  │  {}  │  │  {}  │  │  {}  │                                                                                    !  ./~ \" \\".format( c[1],c[2],c[3]))
    print("  │     │  │     │  │     │                                                                                    `\\.Y      Y    _")
    print("  ╰─────╯  ╰─────╯  ╰─────╯                                                                                    (~~|      |   |^Y")
    print("                                                                                                               `\\. \\     |   l |")
    print("           ╭─────╮                                                                                               T~\\^. Y |   / |")
    print("           │     │                                                                                               | |\\| | !  l  |")
    print("           │  {}  │                                                                                               ! | Y | `\\/'. |".format( c[0]))
    print("           │     │                                                                                         ______L_j l j   ~\"  l")
    print("           ╰─────╯                                                                                       _/,_/, __ ~\"__ }____,/")
    print("                                                                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# < hi >")
#  ----")
#   \\       .")
#    \\      l\\ /\\")
#     \     !)Y.))")
#          _\| //")
#        ,/oo  \\")
#     .-+    _ /")
#    `-_--=-'/")
#          / /")
#         /  \\_")
#        Y  .  )")
#  .--v--^--' /\"\\")
#  \\/~\\/~T\"--' _ \\")
#        !  ./~ \" \\")
#        `\\.Y      Y    _")
#        (~~|      |   |^Y")
#        `\\. \\     |   l |")
#          T~\\^. Y |   / |")
#          | |\\| | !  l  |")
#          ! | Y | `\\/'. |")
#    ______L_j l j   ~\"  l")
#  _/,_/, __ ~\"__ }____,/")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Which is better:
# ╭─────╮ ╭─────╮ ╭─────╮
# │╭───╮│ │ ─── │ │ ─── │
# ││ 8 ││ ││ 8 ││ │  8  │
# │╰───╯│ │ ─── │ │ ─── │
# ╰─────╯ ╰─────╯ ╰─────╯


# "│     │           │      │"
# "│                        │"
# "│                        │"
# "│                        │"
# "│                        │"
# "│                        │"
# "│                        │"
# "│                        │"
# "│                        │"
# "╰────────────────────────╯"│    , "─", "│", "╭", "╮", "╯", "╰" }
# print_to_console(a)'

# while True:
#     if keyboard.read_key() == "a":
#         print("You pressed 'a'.")
#         break


# print(" ____")
# print("< hi >")
# print(" ----")
# print("    \                                  ___-------___")
# print("     \                             _-~~             ~~-_")
# print("      \                         _-~                    /~-_")
# print("             /^\__/^\         /~  \                   /    \")
# print("           /|  O|| O|        /      \_______________/        \")
# print("          | |___||__|      /       /                \          \")
# print("          |          \    /      /                    \          \")
# print("          |   (_______) /______/                        \_________ \")
# print("          |         / /         \                      /            \")
# print("           \         \^\\         \                  /               \     /")
# print("             \         ||           \______________/      _-_       //\__//")
# print("               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/")
# print("                 ~-----||====/~     |==================|       |/~~~~~")
# print("                  (_(__/  ./     /                    \_\      \.")
# print("                         (_(___/                         \_____)_)")

# print("   ▛▀▖                           ▌        ▐ ")
# print("   ▙▄▘▙▀▖▞▀▖▞▀▘▞▀▘ ▝▀▖ ▛▀▖▌ ▌▛▚▀▖▛▀▖▞▀▖▙▀▖▐ ")
# print("   ▌  ▌  ▛▀ ▝▀▖▝▀▖ ▞▀▌ ▌ ▌▌ ▌▌▐ ▌▌ ▌▛▀ ▌  ▝ ")
# print("   ▘  ▘  ▝▀▘▀▀ ▀▀  ▝▀▘ ▘ ▘▝▀▘▘▝ ▘▀▀ ▝▀▘▘  ▝ ")

#   ____  _      _                                    _               _ 
#  |  _ \(_) ___| | __   __ _   _ __  _   _ _ __ ___ | |__   ___ _ __| |
#  | |_) | |/ __| |/ /  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| |
#  |  __/| | (__|   <  | (_| | | | | | |_| | | | | | | |_) |  __/ |  |_|
#  |_|   |_|\___|_|\_\  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_)

#  ____  _      _                                _ _ 
# |  _ \(_) ___| | __   __ _    ___ __ _ _ __ __| | |
# | |_) | |/ __| |/ /  / _` |  / __/ _` | '__/ _` | |
# |  __/| | (__|   <  | (_| | | (_| (_| | | | (_| |_|
# |_|   |_|\___|_|\_\  \__,_|  \___\__,_|_|  \__,_(_)

# print_pick(c)
# time.sleep(.5)