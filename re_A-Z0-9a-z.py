import re

a = "[A-Z][0-9]*[a-z]"
if re.search(a,"L02467283462873460i"):
    print("yes")
else:
    print("no")