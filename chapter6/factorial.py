#5!=5*4*3*2*1
#5!=1*2*3*4*5

num=int(input("enter the value of num : "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)
    