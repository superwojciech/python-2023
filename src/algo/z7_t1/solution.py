
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
    
    if any(x < 0 for x in key) or any(x < 0 for x in lock):
        return -1    
    
    key_index = 0
    lock_index = 0
    while key_index < len(key) and lock_index < len(lock):
        if key[key_index] == lock[lock_index]:
            key_index += 1
            lock_index += 1
        else:
            key_index += 1
    
    if lock_index == len(lock):
        return 0  
    else:
        return 1  
