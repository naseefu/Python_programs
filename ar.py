n = int(input('enter the total number:'))
k = int(input('key:'))
print('input the elements:')

s = list(map(int, input().split()))  # Create a list to store the input elements

for i in range(n - 1):
    s += list(map(int, input().split()))  # Append more input elements to the list

arr = {}
for n in s:
    for j in s:
        if n + j == k:
            arr = {n, j}
    print(arr)
