cost = list(map(int,input().split()))
s= 0
print(len(cost))
for i in range(len(cost)-3,-1,-1):
    s += i
    print(s) 
    #cost[i] += min(cost[i+1],cost[i+2])
#print(min(cost[0],cost[1]))
print(s)