def has_duplicates_string(lista):
    print(len(lista))
    print(len(set(lista)))
    return len(lista) != len(set(lista))



a=['xxx', 'www', 'yyy', 'abc']
print(has_duplicates_string(a))