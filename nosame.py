nums = list(map(int,input().split()))
s = {}
j =1
for i in nums:
    if i not in s:
        s[j]= i
        j+=1
print(s)