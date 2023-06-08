def find_compatible_array(s: str, a: list[int]) -> bool:

    if (len(a) -1) != len(s):
            return False
    
    for i in range(len(a) -1 ):  
         
        if s[i] != '<' and not '>':
            return False     
        
        if s[i] == '<' and not (a[i] < a[i + 1]):
                return False
                   
        elif s[i] == '>' and not (a[i] > a[i + 1]):
                return False

    return True
