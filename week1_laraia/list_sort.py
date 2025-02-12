import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", nargs="?", type=int, default=10)
args = parser.parse_args()

import time
import numpy as np

def find_minimum(array):
    value = min(array)
    return value

def generate_random_array(n):
    return np.random.random((n))

def sort_array(array):
    for i in range(len(array)):
        minimum = find_minimum(array[i:])
        for j in range(i,len(array)):
            if array[j] == minimum:
                array[j] = array[i]
                array[i] = minimum
                break
    return array

A = generate_random_array(args.n)
print(A)

t = time.perf_counter()
B = sort_array(A)
t = time.perf_counter() - t

print(B)

print(f'Calculation time: {t} seconds.')

C = A.copy()
t = time.perf_counter()
C = sorted(C)
t = time.perf_counter() - t
print(C)

print(f'Calculation time: {t} seconds.')
