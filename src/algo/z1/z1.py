# z1

def add(a, b):
    return a+b


def mul(a, b):
    return a*b


print(add(5, 10))
print(mul(5, 5))

# z2


def calculate(fn, a, b):
    return fn(a, b)


print(calculate(add, 6, 6))
print(calculate(mul, 6, 6))
