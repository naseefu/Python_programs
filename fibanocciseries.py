# def fibanocci(x):
#     c=[]
#     for i in range(x):
#         if i==0:
#             c.append(0)
#         elif i==1:
#             c.append(1)
#         else:
#             c.append(c[i-1]+c[i-2])
#     return c
# a = fibanocci(12)
# print(a)

def fibanocci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibanocci(x-1)+fibanocci(x-2)
a = int(input("enter the value"))
for i in range(a):
    print(fibanocci(i),end=" ")