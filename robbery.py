house = list(map(int,input('enter the cash in houses').split()))

rob1,rob2 = 0,0

for n in house:

    temp = max(n+rob1,rob2)
    rob1=rob2
    rob2= temp 

print(rob2)