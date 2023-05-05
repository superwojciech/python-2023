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