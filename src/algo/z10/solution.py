def find(x):
    long = 0
    count = 1
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            count += 1
        elif count > long:
            long = count
            count = 1
    return long

print(find('<>>'))