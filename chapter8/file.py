'''
f= open("abc.text","r")

data= f.read()
print(data)
f.close()
'''
f= open("abc.text")

lines= f.readlines()

print(lines,type(lines))

f.close()