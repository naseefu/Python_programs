c =[]

n = int(input('enter the number of elements:'))

for i in range(n):
    if i==0:
        c.append(i)
    elif i==1:
        c.append(i)
    else :
        c.append(i+i-1)

print(c)
