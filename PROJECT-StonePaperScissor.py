#stone Paper Scissor Game:

#Calculation of winner.
def gamewin(comp,you):
    if you==comp:
        return print("The game is Tie")
    
    if comp==1 and you ==2:
        return print("You won this match.")
    if comp==2 and you ==3:
        return print("You won this match.")
    if comp==3 and you ==1:
        return print("You won this match.")
    
    if comp==1 and you ==3:
        return print("Computer won this match.")
    if comp==2 and you ==1:
        return print("Computer won this match.")
    if comp==3 and you ==2:
        return print("Computer won this match.")
#Take input for computer.
import random
comp=random.randint(1,3)
#Print as Template
print("This is Stone Paper Scissor game.")     
print("[Enter 1 for stone, 2 for paper,3 for scissor]")
#player's turn   
you=int(input("Your Turn:"))
0
if you==1:
    print("Your's Turn is:Stone")
elif you==2:
    print("Your's Turn is:paper")
elif you==3:
    print("Your's Turn is:Scissor")
 
if comp==1:
    print("computer's Turn is:Stone")
elif comp==2:
    print("computer's Turn is:paper")
elif comp==3:
    print("computer's Turn is:Scissor")
#call the value for cheking the winner.   
gamewin(comp,you)




