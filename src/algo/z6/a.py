def has_duplicates(lista):
    return len(lista) != len(set(lista))



a=['aa', 'a', 'c', 'bb']
print(has_duplicates(a)) #Jeśli false to nic sie nie powtarza, jeśli true są duplikaty