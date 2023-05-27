"""
Zadanie: mamy daną tablicę liczb całkowitych "a"; chcemy potencjalnie stworzyć inną tablicę
tej samej długości, "b", gdzie
b[i] = a[i] lub a[i] - a[j],
przy czym "j" może być inne dla każdego "i".

Chcemy by ostatecznie wszystkie elementy tablicy "b" miały tą samą parzystość... czyli by były wszystkie
parzyste, lub wszystkie nieparzyste. Dodatkowo wszystkie liczby tablicy "a" i "b" mają być > 0.

Przykład:

a = [1, 5, 6]
można wykorzystać do budowy
b = [1, 5, 5]  (wszystkie są nieparzyste, przy czym a[0]=b[0], a[1]=b[1], b[2] = a[2] - a[0])
lub
b = [1, 5, 1]  (teraz na ostatniej pozycji odjęliśmy 5, czyli a[1])



"""


def equalize_parity(a: list[int]) -> bool:
    is_all_even = all(x % 2 == 0 for x in a)
    is_all_odd = all(x % 2 != 0 for x in a)
    min_num = min(a)

    if min_num % 2 != 0:
        return True
    else:
        return is_all_even or is_all_odd

