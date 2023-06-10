import random
import string

def encoder(s: str) -> str:
    encoded = ''
    for c in s:
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 5)))
        encoded += c + random_chars + c
    return encoded

def decoder(s: str) -> str:  # pierwsza badz ostatnia zawsze jest poprawna litera
    pass
  

s = 'kad'
encoded = encoder(s)
print(encoded)

# decoded = decoder(encoded)
# print(decoded)