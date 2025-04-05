import time
import numpy as np
from memtool import malloc_double, init_double_sequence, sum_double, free

N = 10_000_000

# python puro
lista = list(range(N))
start = time.time()
total = sum(lista)
end = time.time()
print(f"[Python puro] Total: {total}, Tiempo: {end - start:.5f}s")

# NumPy (float64)
arr = np.arange(N, dtype=np.float64)
start = time.time()
total = np.sum(arr)
end = time.time()
print(f"[NumPy float64] Total: {total}, Tiempo: {end - start:.5f}s")

# memtool double
ptr = malloc_double(N)
init_double_sequence(ptr, N)

start = time.time()
total = sum_double(ptr, N)
end = time.time()
free(ptr)

print(f"[memtool double] Total: {total}, Tiempo: {end - start:.5f}s")
