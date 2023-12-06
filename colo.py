a = int(input('enter the number of elements:'))

arr = []

for i in range(a):
    b = int(input(f'enter the {i+1} element'))
    arr.append(b)

print(f'list:{arr}')
arr.sort()
print(f'sorted array is:{arr}')

unique=[]

for num in arr:
    if num not in unique:
        unique.append(num)

print(f'unique numbers are { unique}')