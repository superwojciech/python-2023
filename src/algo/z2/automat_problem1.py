from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    # tutaj wstawić coś co generuje dane dla naszego algorytmu
    # return [randint(0, 10 ** 6) for _ in range(data_size)]
    x = []
    y = []
    r = []
    for _ in range(data_size*2):
        r.append(randint(0,25))
    for u in r[0::2]:
        x.append(u)
    for n in r[1::2]:
        y.append(n)
    return x,y
    


def solve_problem(data):
    # tutaj wstawić algorytm który rozwiązuje dany problem dla danych `data
    x = data[0]
    y = data[1]
    wynik=[]
    for i in x:
        incr = 0
        if i!=0:
            for j in y:    
                if (j!=0) & (j%i == 0): 
                    incr +=1
        wynik.append(incr)

    
    return(wynik)
    


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 10000:
        print(f'testing solver for {size=}')
        data = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 2

    return sizes, times


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()


#test