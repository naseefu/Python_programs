g = list(map(int,input('enter the greed factor of children:').split()))
s = list(map(int,input('enter the size of cookie:').split()))

count = 0
for i in s:
    for j in g:
        if i>=j and j>0:
            count=count+1
            g.remove(j)
            s.remove(i)
print(count)