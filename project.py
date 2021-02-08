game ="Welcome, this a game of numbers, you may play this game if you are getting bored"
print(game)
intro = int(input("are you ready, if you are then type 1 else you may type 0:-    "))
if (intro==1):
    print("ready")
else:
  print("so you are not ready but try this game ")

game1 = int(input("Pick a whole number between 1 and 10 and remember this number as 1st number:-  "))
game2 = int(input("pick another whole number between 1 to 100 and remember this as 2nd number:-  "))
game3 = int(input("multiply 1st and the second number and type your answer:-  "))

if (game3==game1*game2):
    print("CONGRATULATIONS YOU GOT THE CORRECT ANSWER !!!")
else:
  print("Oops!! There was a silly mistake try again")
