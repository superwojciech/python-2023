
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

Zadanie -- mamy dostępny zbiór sylab, oraz pewne słowo `word`; pytanie -- czy przy użyciu tych sylab
(każdą można użyć dowolną liczbę razy, również 0) można utworzyć dane słowo.

"""


def construct_word(syllables: set[str], word: str) -> bool:
    x = []

    for i in range(len(word)):
        if i+1 < len(word):
            x.append(word[i] + word[i+1])
    if set(x) & syllables == set(x):
        return True
    return False