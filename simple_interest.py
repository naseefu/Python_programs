def interest(p,n,r):
    return (p*n*r)/100
p = int(input("Principal Amount:"))
n = int(input("No of years:"))
r = int(input("rate:"))
a = interest(p,n,r)
print("Simple interest is: ",a)
