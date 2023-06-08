def find(x: str) -> int:
    
    long = 0
    count = 1
    if '<' not in x and '>' not in x:
        return 0

    for i in range(1, len(x)):
        
        if x[i] == x[i - 1] and x[i] in ['<', '>']:
            count += 1

        else:
            long = max(long, count)
            count = 1

    long = max(long, count)
    return long