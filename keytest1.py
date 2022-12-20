import tty, sys, termios, os

# import required module
# play sound
# file = "button-4.mp3"
# print('playing sound using native player')
# os.system("mpg123 " + file)
print("\a") # bell sound escape sequence

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while 1:
  x=sys.stdin.read(1)[0]
  print("You pressed", x)
  if x == "r":
    print("If condition is met")
  if x=="q":
    break
  if x=="[A":
    print("You pressed back the match   button")
termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)