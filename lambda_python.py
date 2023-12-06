def sample(x):
    return lambda a:a+x
b = sample(2)
print(b(5))

