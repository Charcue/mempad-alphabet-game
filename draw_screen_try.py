import os
# import time
import sys

def print_try_pick(c):
    '''
    function to print graphic placeholder for 
    the user when they need to try again
    Expect a list 10 single characters
    (c = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    '''
    # Clear screen before printing graphics
    os.system('cls' if os.name == 'nt' else 'clear')
    # Top padding
    print("\n" * 4)
    # graphics format string placeholders
    print("  ╭─────╮  ╭─────╮  ╭─────╮                _____                               _       _              < hi >") 
    print("  │     │  │     │  │     │               |_   _| __ _   _    __ _  __ _  __ _(_)_ __ | |              ----") 
    print("  │  {}  │  │  {}  │  │  {}  │                 | || '__| | | |  / _` |/ _` |/ _` | | '_ \| |                 \\       .".format( c[7],c[8],c[9]))
    print("  │     │  │     │  │     │                 | || |  | |_| | | (_| | (_| | (_| | | | | |_|                  \\      l\\ /\\")
    print("  ╰─────╯  ╰─────╯  ╰─────╯                 |_||_|   \__, |  \__,_|\__, |\__,_|_|_| |_(_)                   \     !)Y.))")
    print("                                                     |___/         |___/                                         _\| //")
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