import random

skissors = [('scissors',0),('paper',1),('rock',2),('gun',3),('lazer',4),]
for element in skissors:
    space = ' ' * (10 - len(element[0]))
    print(f'{element[0]}{space}| {element[1]}')

win_len = len(skissors) // 2

while False:
    pl_choice = int(input(': '))
    if pl_choice == com_choice:
        print('again')
    print(pl_choice,com_choice)
    if pl_choice >= len(skissors) - win_len:
        pl_choice = pl_choice - len(skissors)
    if com_choice - pl_choice > 0 and  com_choice - pl_choice <= win_len:
         print(f'Yay! {pl_choice} beats {com_choice}')
         break
    else:
       print(f'Noo! {com_choice} beats {pl_choice}')
       break

