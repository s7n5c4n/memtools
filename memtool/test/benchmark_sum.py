import time
import numpy as np
from memtool import malloc_int, sum_int, free, init_int_sequence

N = 1_000_000

# --- Python puro ---
lista = list(range(N))
start = time.time()
total = sum(lista)
end = time.time()
print(f"[Python puro] Total: {total}, Tiempo: {end - start:.5f}s")

# --- NumPy ---
arr = np.arange(N, dtype=np.int32)
start = time.time()
total = np.sum(arr)
end = time.time()
print(f"[NumPy] Total: {total}, Tiempo: {end - start:.5f}s")

# --- memtool con suma en C ---
ptr = malloc_int(N)
init_int_sequence(ptr, N) 

start = time.time()
total = sum_int(ptr, N)
end = time.time()
free(ptr)

print(f"[memtool (C sum)] Total: {total}, Tiempo: {end - start:.5f}s")
