import re

i = input("enter the string: ")
a = input("enter the desired string: ")

if re.match(a,i):
    print("{} is present in the string".format(a))
else:
    print("doesnt exist")

print(re.sub(a,"bro",i))

b = "[A-Z][0-9][a-z]"
if re.search(b,"L0i"):
    print("yes")
else:
    print("no")