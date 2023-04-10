from multiprocessing import Pool
import random
import time
import numpy as np


a = 0
b = np.pi #limits of integration
N = 1000

param = (a, b, N)
    
def func(x):
    return np.sin(x)

def Monte_Carlo_integration(ls):
    a, b, N = ls

    for i in range(N):

        xrand = np.zeros(N)

        for i in range(len(xrand)):
            xrand[i] = random.uniform(a, b)
            integral = 0.0

        for i in range(N):
            integral += func(xrand[i])
        
        answer = (b-a)/float(N)*integral

    return answer


if __name__ == '__main__':
    with Pool(12) as p:
        start = time.time()
        l1 = (p.map(Monte_Carlo_integration,
                    [param, param, param, param, param]))
        print(sum(l1) / len(l1), time.time() - start)



