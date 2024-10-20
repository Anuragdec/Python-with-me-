#sum of n natural numbers
num=int(input("enter the value of num : "))


def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(num))
