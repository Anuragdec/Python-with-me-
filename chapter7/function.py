def convert(c):
    fat= (c*(9/5)+32)
    return fat

c= float(input("enter the degree celcius  :"))
a=convert(c)
print(f"{a} is in farengisht")
