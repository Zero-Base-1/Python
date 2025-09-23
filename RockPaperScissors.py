import random

print('Rock Paper Scissors')
print('1. is for ✊ Rock.')
print('2. is for ✋ Paper.')
print('3. is for ✌️ Scissors.')

computer = random.randint(1,3)
player = int(input('Pick a number: '))


if player == 1:
    print(f'You chose: ✊')
elif player == 2:
    print(f'You chose: ✋')
elif player == 3:
    print(f'You chose: ✌️')
else:
    print('Error')

if computer == 1:
    print(f'CPU chose: ✊')
elif computer == 2:
    print(f'CPU chose: ✋')
elif computer == 3:
    print(f'CPU chose: ✌️')
else:
    print('Error')

if ((player == 1) and (computer == 3)) or ((player == 2) and (computer == 1)) or ((player == 3) and (computer == 2)):
    print('The player Won!')
elif((player == 3) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 3)):
    print('The CPU Won!')
elif((player == 1) and (computer == 1)) or ((player == 2) and (computer == 2)) or ((player == 3) and (computer == 3)):
    print('Tie')
else:
    print('Error')