
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek3


"""




def open_lock(key: list[int], lock: list[int]) -> int:
    # sprawdzenie czy wartości nie są < 0
    if len(key) != len(lock):
        result = "nie możesz wejść, zły klucz"
        return result  #zamek sie otwiera
    if any(x < 0 for x in key) or any(x < 0 for x in lock):
        result = "nie możesz wejść, zły klucz"
        return result  #zamek sie otwiera  
    
    #proba otworzenia zamka
    key_index = key[0]+lock[0]

    result = ""
    for i in range(len(key)):
        if key[i] >= 0 and lock[i] >= 0:
                for j in range(len(key)):
                    if key[j]+lock[j] != key_index:
                        result = "nie możesz wejść, zły klucz"
                        return result  #zamek sie otwiera
        result = "możesz wejść"
        return result  #zamek sie otwiera
