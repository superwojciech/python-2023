def get_min_number_of_operations(a: list[int]) -> int:
    x = 0
    y = 0
    length = len(a)
    while length > y:
        if a[y] < 0:
            x = x +1
            while a[y] <= 0:
                   y = y+1
                   if length == y: break
        y = y +1
    return x