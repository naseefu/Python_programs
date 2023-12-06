
head = list(map(str,input().split()))
n = int(input())
a = len(head)
head.pop(a-(n))
print(head)