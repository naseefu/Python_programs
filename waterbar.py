m = []
w = list(map(int,input().split()))
N = len(w)
max_=0
index_max = 0
water = 0
last_water = 0
for i in range(len(w)):
    if w[i]>=max_:
        max_=w[i]
        index_max=i
        last_water=0
    else:
        water +=(max_ -w[i] )
        last_water+=(max_-w[i])

    print('total water:',water)
    print('last water:',last_water)
if index_max!=N:
    max_=0
    water-=last_water
    for i in range(N-1,index_max-1,-1):
        if w[i]>=max_:
            max_=w[i]
        else:
            water+=(max_-w[i])
            print('total water:',water)
print(water)
