import random
import string

def encoder(s: str) -> str:

    encoded = ''

    for c in s:
        available_chars = string.ascii_letters.replace(c, '')
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 5)))
        encoded += c + random_chars + c
    return encoded

def decoder(encoded: str) -> str:

    correct = encoded[0]
    decoded = correct
    i = 1

    while i < len(encoded):
        if correct == encoded[i]:
            if i+1 < len(encoded):
                i += 1
                decoded += encoded[i]
                correct = encoded[i]
        i += 1
    return decoded
   
  

s = 'texttestowy'
encoded = encoder(s)
print(encoded)

decoded = decoder(encoded)
print(decoded)