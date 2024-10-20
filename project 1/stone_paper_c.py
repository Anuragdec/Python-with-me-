import random
#s=-1
#P=0
#C=1
computer=random.choice([-1,0,1])
youchoose=input("enter your choose from stone(S)....paper(P)...cessor(C) :")
youDict={'S':-1,'P':0,'C':1}
reverseDict={
    -1:'Stone',0:'Paper',1:'cessor'
}
you=youDict[youchoose]
print(f"you choose  :{reverseDict[you]}\n computer choose  : { reverseDict[computer]}")


if(computer==you):
    {
        print("It is draw")
    }
else:
    if(computer==0 and you==-1):
        print("you loose")
    elif(computer==-1 and you==1):
        print("you loose")
    elif(computer==1 and you==0):
        print("you loose")
    
    elif(computer==-1 and you==0):
        print("you win")
    
    elif(computer==1 and you==-1):
        print("you win")
    
    elif(computer==0 and you==1):
        print("you win")
    else:
        print("somthing went wrong")
    