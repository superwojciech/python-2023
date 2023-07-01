def get_decomposition(n, k, x) -> list[int]:
    numbers = list(range(1, k+1))
    numbers.remove(x)

    combination = []
    total_sum = 0

    for num in reversed(numbers):
        if num == x:
            continue

        if num <= n - total_sum:
            combination.append(num)
            total_sum += num

        if total_sum == n:
            break

    if total_sum == n:
        return combination
    else:
        return []