def greater(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greter than all remaining {b} and {c} ")
    elif(b>c):
        print(f"{b} is greater than all {a} and {c}")
    else:
        print(f"{c} is greater than all {a} and {b}")
        
a=int(input("Enter the vslue of a:"))        
b=int(input("Enter the vslue of b:"))        
c=int(input("Enter the vslue of c:"))        

greater(a,b,c)