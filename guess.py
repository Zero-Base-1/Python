guess = 0
tries = 3

while guess != 6 and tries != 0:
  guess = int(input("Guess the number:  "))
  tries -= 1

if tries == 0:
  print('Out of Tries')
else:
  print("You got it!")