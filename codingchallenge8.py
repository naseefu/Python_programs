def student(x):
    return (x-x*0.1)
def regbuyer(x):
    return (x -x*0.05)
b = int(input("enter the price of product: "))
c = regbuyer(student(b))
print(c)

