nums = list(map(int,input().split()))
flag = 0
s= set()
for i in nums:
    if i in s:
        flag = 1
        break
    else:
        s.append(i)
if flag == 1:
    print('true')
else :
    print('false')