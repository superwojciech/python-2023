Zadanie... będzie trzeba ułożyć liczbę n jako sumę pewnych liczb 1...k (które można powtarzać), bez użycia liczby x; czyli:

niech n=10, k=5, x=3
możemy napisać 10 = 5 + 5
lub 10 = 5 + 2 + 2 + 1
ale nie 10 = 5 + 2 + 3

---
gdyby n=7, k=3, x=2
to można napisać 7 = 3 + 3 + 1
ale nie 7 = 2 + 3 + 2
czyli ostatecznie

```py
def get_decomposition(n, k, x) -> list[int]:
    numbers = list(range(1, k+1))
    numbers.remove(x)

    result = []
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
        return result
    else:
        return 0    
                       
n = 10
k = 5
x = 3

result = find_combination(n, k, x)

```
