import random

skissors = [('scissors',0),('paper',1),('rock',2),('gun',3),('lazer',4),]
for element in skissors:
    space = ' ' * (10 - len(element[0]))
    print(f'{element[0]}{space}| {element[1]}')


com_choice = 1 #random.choice(skissors)
while False:
    pl_choice = int(input(': '))
    print(pl_choice,com_choice)
    if pl_choice >= len(skissors) -2:
        pl_choice = pl_choice - len(skissors)
    if com_choice - pl_choice > 0 and  com_choice - pl_choice <= 2:
        print('yay')

    #    print(f'{pl_choice} beats {com_choice} yay1')
    #elif ((com_choice + 2) % 5 > pl_choice):
    #    print('nope2')
    else:
       print(f'{com_choice} beats {pl_choice} noo')

