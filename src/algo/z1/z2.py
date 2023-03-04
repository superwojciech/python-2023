def calculate(fn, a, b):
    if fn == "add":
        return a+b
    elif fn == "mul":
        return a*b


print(calculate("add", 5, 5))
print(calculate("mul", 5, 5))
