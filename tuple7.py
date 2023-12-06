# .Create a tuple with 7 elements
# 1. Use Insert, Append.
# 2. Print the last second element.

a = (1,2,3,4,5,6,7)
b = list(a)
b.insert(3,8)
b.append(9)
a = tuple(b)
print(a)
print(a[-2])



