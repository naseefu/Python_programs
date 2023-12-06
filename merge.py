nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
n = int(input())
for i in range(n):
    nums1.append(nums2[i])
for j in nums1:
    if j==0:
        nums1.remove(j)
nums1.sort()
if nums1[0]==0:
     print(nums1[1:])
else:
    print(nums1)