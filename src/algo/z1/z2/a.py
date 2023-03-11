# from datetime import datetime
# from random import randint


# def gen_random_numbers(count: int, seed_number: int):
#     seed(seed_number)
#     return [randint(0,10**6) for _ in range(count)]

# def sort_numbers(nums: list[int]) -> list[int]:
#     ret = sorted(nums)
#     return ret



# if __name__=='__main__':
#     w = gen_random_numbers(200, seed_number=111)
#     REPETITIONS = 10000
#     time_sum = 0
#     for i in range(REPETITIONS):
#         st = datetime.now().timestamp()
#         ret = sort_numbers(w)
#         en = datetime.now().timestamp()
#         time_sum += (en-st)

#     print(f'czas wykonania: {time_sum / REPETITIONS:.6} s')


   
    

a = [2,5,7,9]
b = [4,8,18,27]
wynik = []

for i in a:
    incr = 0
    for j in b:    
        if j%i == 0: 
            incr +=1
    wynik.append(incr)
print(wynik)
