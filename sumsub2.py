arr = list(map(int,input().split()))
k = int(input('enter k:'))
count = 0
dic ={}
sum_=0
for i in arr:
    sum_+=i

    if sum_==k:
        count+=1
    if sum_-k in dic:
        count+=(dic[sum_-k])
    if sum_ in dic:
        dic[sum_]+=1
    else:
        dic[sum_]=1
    print('dictionary:',dic)
print(count)
        
