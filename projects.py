# snake water game 

import random 

computer = random.choice([1, -1, 0])

your_choice=(input("Enter your choice :"))
yourDict={"s":1,"w":-1,"g":0}
reverse_dict={1:"s",-1:"w",0:"g"}

you=(yourDict[your_choice])

print(f"you choose : {reverse_dict[you]} \n computer choose : {reverse_dict[computer]} ")

if(you==computer):
    print("It's a draw")

elif(computer==1 and you==-1):
    print("you loose..!!")
        
elif(computer==1 and you==0):
    print("you win..:)")

elif(computer==-1 and you==1):
    print("you win..:)")

elif(computer==-1 and you==-0):
    print("you loose..!!")

elif(computer==0 and you==1):
    print("you loose..!!")

elif(computer==0 and you==-1):
    print("you win..:)")