import random

#add as many as you want! it will scale
skissors = [('rock','🪨'),('fire','🔥'),('scissors','✂️'),('sponge','🧽'),('paper','📄'),('air','💨'),('water','💧'),]

def print_choices():
    print()
    for i, element in enumerate(skissors):
        space = ' ' * (10 - len(element[0]))
        print(f'{element[0]}{space}| {i}')

#ugly camelCase function name
def playGame(out_of):
    wins = 0
    print_choices()

    win_len = len(skissors) // 2
    while out_of > 0:
        pl_choice = int(input('~~~~~~~~~~~~~\n: ')) % len(skissors)
        com_choice = random.randint(0, len(skissors)-1)
        print(f"\n{skissors[pl_choice][1]}  vs {skissors[com_choice][1]}\n")
        if pl_choice == com_choice:
            print('Tie!')
            continue
        if pl_choice >= len(skissors) - win_len:
            pl_choice = pl_choice - len(skissors)
        if com_choice - pl_choice > 0 and  com_choice - pl_choice <= win_len:
            print(f'Yay! {skissors[pl_choice][0]}  beats {skissors[com_choice][0]}')
            out_of -= 1
            wins += 1
        else:
            print(f'Noo! {skissors[com_choice][0]}  beats {skissors[pl_choice][0]}')
            out_of -= 1
            wins -= 1
    print()
    if wins < 0: return "computer wins!"
    elif wins > 0: return "player wins!"
    else: return "tie!"

print(playGame(int(input("play out of: "))))
