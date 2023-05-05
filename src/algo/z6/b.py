<<<<<<< HEAD
def has_duplicates(lista):
    duplicates = []
    no_duplicates = [] 
    for x in lista:
        if x not in no_duplicates:
            no_duplicates.append(x)
        else:
            duplicates.append(x)
    
    if len(lista) != len(set(no_duplicates)):
        print('Duplikaty to: ', duplicates)
        return
    else:
        print("Nie ma powtórzeń")
        return
    #return len(lista) != len(set(no_duplicates))



a=['aa', 'a', 'c', 'bb']
has_duplicates(a)
=======
def has_duplicates_string(lista):
    print(len(lista))
    print(len(set(lista)))
    return len(lista) != len(set(lista))



a=['xxx', 'www', 'yyy', 'abc']
print(has_duplicates_string(a))
>>>>>>> c5c9a331f1e91f39545037b3fe9f187f433d93f0
