#Write a function which would divide two numbers, design the
# function in a manner that it handles the divide by zero exception

def fil(a,b):
    try:
        print(a/b)
    except:
        print('divisor cannot be zero')
a = int(input())
b = int(input())
fil(a,b)
