
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""


def split_to_syllables(word: str) -> list[str]:
    
    if len(word) <= 2:
        word2 =[word]
        return word2

    sylaby = [word[:2]]
    for i in range(2, len(word)):
        sylaba = word[i-1] + word[i]
        sylaby.append(sylaba)

    return sylaby
