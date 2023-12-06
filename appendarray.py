n = int(input('enter the number'))
s = list(map(int,input().split()))
k = int(input('enter the key:'))
for i in range(n-1):
    s+= list(map(int,input().split()))

arr = {}

for i in s:
    for j in s:
        if i+j ==k and i!=0 and j!=0:
            arr = {i,j}
            print(arr)