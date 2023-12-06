a = int(input('enter the decimal number:'))
arr = []
i=0
while a==1:
    if a%2==0:
        a=a/2
        arr[i]=0
        i=i+1
    elif a%2==1:
        a=(a-1)/2
        arr[i]=1
        i=i+1
    
print(arr)    