def has_duplicates(lista):
    return len(lista) != len(set(lista))



a=['aa', 'aa', 'c', 'bb']
print(a)
print(has_duplicates(a))