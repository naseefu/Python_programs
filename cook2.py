g = list(map(int,input('enter the greed factor of children:').split()))
s = list(map(int,input('enter the size of cookie:').split()))

count = 0
i = 0
j = 0
n,m = len(g),len(s)

g.sort()
s.sort()

while(i<n and j<m):
    if g[i]<=s[j]:
        count+=1
        i+=1
        j+=1
    else:
        i+=1
print(count)