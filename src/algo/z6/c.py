data = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]

d = {}

for id, name in data:
    if id not in d:
        d[id] = [name]
    else:
        d[id].append(name)

for id, names in d.items():
    if len(names) > 1:
        print(f"Do ID: {id} przypisane są imiona takie jak: {names}")
