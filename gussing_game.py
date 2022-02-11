import random
x = random.randint(0,100)

u = int(input("plz enter how many guess do yo want !! :  "))
print(f"****** you have {u} gesue and win this game ******")
gusee = 0
left = u
while(True):
    if gusee == u :
        print(f"you gussed {gusee} times :    ****GAME OVER**** ")
        break

    y = int(input(f"Enter your Number , Your guess number {gusee} You have left guess is {left} :  "))
    if y>x :
        print("plz tell a small number :")
        gusee = gusee + 1
        left  = left - 1
        continue
    if gusee == u :
        print(f"you guessed {gusee} times :    GAME OVER ")
        break

    elif y<x :
        print("plz tell a big number :")
        gusee = gusee + 1
        left = left - 1
        continue
    else:
        print(f"You took total {gusee}/{u} guess for win !! BINGO !!")
    gusee = gusee + 1

    break

