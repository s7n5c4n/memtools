import time
import numpy as np
from memtool import malloc_float, sum_float, init_float_sequence, free

N = 5000_000

# NumPy
arr = np.arange(N, dtype=np.float32)
start = time.time()
total = np.sum(arr)
end = time.time()
print(f"[NumPy float32] Total: {total}, Tiempo: {end - start:.5f}s")

# memtool
ptr = malloc_float(N)
init_float_sequence(ptr, N)

start = time.time()
total = sum_float(ptr, N)
end = time.time()
free(ptr)

print(f"[memtool float] Total: {total}, Tiempo: {end - start:.5f}s")
