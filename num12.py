m = int(input('number:'))
nums1 = list(map(int,input().split()))
n = int(input('number:'))
nums2 = list(map(int,input().split()))
s = []
for i,j in enumerate(nums1):
    if i<m:
        s.append(j)
for i,j in enumerate(nums2):
    if i<n:
        s.append(j)
            
print(s)