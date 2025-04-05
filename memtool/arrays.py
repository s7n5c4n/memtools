# memtool/arrays.py
from .base import BaseArray
from . import (
    malloc_int, set_int, get_int, sum_int, init_int_sequence, free as free_mem,
    malloc_float, set_float, get_float, sum_float, init_float_sequence,
    malloc_double, set_double, get_double, sum_double, init_double_sequence,
    scale_int, fill_int, dot_product_int
)


class IntArray(BaseArray):
    def __init__(self, size, init_sequence=False):
        ptr = malloc_int(size)
        if init_sequence:
            init_int_sequence(ptr, size)
        super().__init__(size, ptr, set_int, get_int, sum_int, free_mem, scale_func=scale_int, fill_func=fill_int, dot_func=dot_product_int)


class FloatArray(BaseArray):
    def __init__(self, size, init_sequence=False):
        ptr = malloc_float(size)
        if init_sequence:
            init_float_sequence(ptr, size)
        super().__init__(size, ptr, set_float, get_float, sum_float, free_mem, scale_func=None, fill_func=None, dot_func=None)


class DoubleArray(BaseArray):
    def __init__(self, size, init_sequence=False):
        ptr = malloc_double(size)
        if init_sequence:
            init_double_sequence(ptr, size)
        super().__init__(size, ptr, set_double, get_double, sum_double, free_mem, scale_func=None, fill_func=None, dot_func=None)