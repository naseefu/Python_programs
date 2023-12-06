def octal(n):
  a=0
  n= str(n)
  n= n[::-1]
  for i,j in enumerate(n):
    a+=int(j)*(8**int(i))
  return a
print(octal(512))