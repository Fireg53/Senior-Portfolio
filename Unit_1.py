import random

skissors = [('scissors',0),('paper',1),('rock',2),]
for element in skissors:
    space = ' ' * (10 - len(element[0]))
    print(f'{element[0]}{space}| {element[1]}')

pl_choice = input(': ')

com_choice = random.choice(skissors)
print(com_choice)

if ((int(pl_choice) + 1) % 3 - com_choice[1] < 2):
    print('yay')

