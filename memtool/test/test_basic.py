# test/test_basic.py
from memtool import malloc_int, set_int, get_int, free

ptr = malloc_int(5)
set_int(ptr, 0, 100)
set_int(ptr, 1, 200)

print("Valor 0:", get_int(ptr, 0))
print("Valor 1:", get_int(ptr, 1))

free(ptr)
