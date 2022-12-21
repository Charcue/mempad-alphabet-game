import os
# import time
import sys

def print_pick(c):
    '''
    function to print graphic placeholder for 
    the user to select a number from list
    Expect a list 10 single characters
    (c = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    '''
    # Clear screen before printing graphics
    os.system('cls' if os.name == 'nt' else 'clear')
    # Top padding
    print("\n" * 4)
    # graphics format string placeholders
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
    print("           ╰─────╯                                          'Q' to quit!                                 _/,_/, __ ~\"__ }____,/")
    print("                                                                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~")