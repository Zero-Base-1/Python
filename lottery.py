import random
my_numbers = []
winning_numbers = []

for i in range(5): 
  my_numbers.append(random.randint(1,69))

for i in range(5):
  winning_numbers.append(random.randint(1,69))

my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

print(f'My Numbers: {my_numbers}')
print(f'Winning Numbers: {winning_numbers}')