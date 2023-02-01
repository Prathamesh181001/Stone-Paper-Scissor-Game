import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'c':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'c':
            return True
    elif comp == 'c':
        if you == 'p':
            return False
        elif you == 's':
            return True

print("Enter s, p or c: stone(s), paper(p) or scisor(c): ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
if randNo == 3:
    comp = 'c'

you=input("Enter s,p or c: stone(s), paper(p) or scisor(c): ")

a = gamewin(comp,you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if a == None:
    print("The game is tie.")
elif a:
    print("You win.")
else:
    print("You lose.")