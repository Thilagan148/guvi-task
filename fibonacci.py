d=[]
a=0
b=1
c=int(input("Enter a number"))
d.append(a)
d.append(b)
for i in range(2,c):
    e=a+b
    d.append(e)
    a=b
    b=e
print(d)    
