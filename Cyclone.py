# Write code below 💖
height = int(input('Enter your Height:'))
credits = int(input('Enter your Credits:'))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >=10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You don't met the requirements.")