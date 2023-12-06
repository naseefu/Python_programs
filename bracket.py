M = []
s = input('enter the string:')
for i in s:
    if i in ('(','[','{'):
        M.append(i)
    elif i==']' and M!=[] and M[-1]=='[':
        M.pop(-1)
    elif i==')' and M!=() and M[-1]=='(':
        M.pop(-1)
    elif i=='}' and M!={} and M[-1]=='{':
        M.pop(-1)
    elif i ==(')',']','}'):
        M.append(i)

if M == []:
    print('balanced')
else :
    print('unbalanced')


    