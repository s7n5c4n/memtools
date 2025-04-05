from ctypes import CDLL, POINTER, c_int, c_float, c_double, c_void_p, c_longlong
import os
import sysconfig

# Detectar automáticamente la carpeta build generada
py_version = sysconfig.get_config_var('LDVERSION') or sysconfig.get_python_version()
lib_dir = f"build/lib.linux-x86_64-cpython-{py_version.replace('.', '')}"

# Armar la ruta completa al .so generado
lib_path = os.path.join(os.path.dirname(__file__), f"core.cpython-{py_version.replace('.', '')}-x86_64-linux-gnu.so")

# Y en caso de que quieras permitir fallback en dev, podés hacerlo así:
if not os.path.exists(lib_path):
    dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', f'lib.linux-x86_64-cpython-{py_version.replace(".", "")}', 'memtool', f'core.cpython-{py_version.replace(".", "")}-x86_64-linux-gnu.so'))
    if os.path.exists(dev_path):
        lib_path = dev_path

lib = CDLL(lib_path)

# Para operaciones con enteros, usamos POINTER(c_int)
lib.mem_malloc_int.restype = POINTER(c_int)
lib.mem_set_int.argtypes = [POINTER(c_int), c_int, c_int]
lib.mem_get_int.argtypes = [POINTER(c_int), c_int]
lib.mem_get_int.restype = c_int

# Actualizamos mem_sum_int para que retorne un entero de 64 bits
lib.mem_sum_int.argtypes = [POINTER(c_int), c_int]
lib.mem_sum_int.restype = c_longlong

lib.mem_init_int_sequence.argtypes = [POINTER(c_int), c_int]
lib.mem_init_int_sequence.restype = None

lib.mem_scale_int.argtypes = [POINTER(c_int), c_int, c_int]
lib.mem_scale_int.restype = None

lib.mem_fill_int.argtypes = [POINTER(c_int), c_int, c_int]
lib.mem_fill_int.restype = None

lib.mem_dot_product_int.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
lib.mem_dot_product_int.restype = c_longlong

def dot_product_int(ptr_a, ptr_b, size): return lib.mem_dot_product_int(ptr_a, ptr_b, size)

def malloc_int(n):
    ptr = lib.mem_malloc_int(n)
    if not ptr:
        raise MemoryError(f"Fallo al reservar memoria para {n} enteros.")
    return ptr

def set_int(ptr, i, val): 
    lib.mem_set_int(ptr, i, val)
    
def get_int(ptr, i): 
    return lib.mem_get_int(ptr, i)
    
def sum_int(ptr, size): 
    return lib.mem_sum_int(ptr, size)
    
def init_int_sequence(ptr, size):
    lib.mem_init_int_sequence(ptr, size)

def scale_int(ptr, size, factor): lib.mem_scale_int(ptr, size, factor)

def fill_int(ptr, size, value): lib.mem_fill_int(ptr, size, value)

# FLOAT
lib.mem_malloc_float.restype = POINTER(c_float)
lib.mem_set_float.argtypes = [POINTER(c_float), c_int, c_float]
lib.mem_get_float.argtypes = [POINTER(c_float), c_int]
lib.mem_get_float.restype = c_float

lib.mem_sum_float.argtypes = [POINTER(c_float), c_int]
lib.mem_sum_float.restype = c_float

lib.mem_init_float_sequence.argtypes = [POINTER(c_float), c_int]
lib.mem_init_float_sequence.restype = None

lib.mem_scale_float.argtypes = [POINTER(c_float), c_int, c_float]
lib.mem_scale_float.restype = None

lib.mem_fill_float.argtypes = [POINTER(c_float), c_int, c_float]
lib.mem_fill_float.restype = None

lib.mem_dot_product_float.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
lib.mem_dot_product_float.restype = c_float

def scale_float(ptr, size, factor): lib.mem_scale_float(ptr, size, factor)
def fill_float(ptr, size, value): lib.mem_fill_float(ptr, size, value)
def dot_product_float(ptr1, ptr2, size): return lib.mem_dot_product_float(ptr1, ptr2, size)


def malloc_float(n):
    ptr = lib.mem_malloc_float(n)
    if not ptr:
        raise MemoryError(f"Fallo al reservar memoria para {n} floats.")
    return ptr

def set_float(ptr, i, val): lib.mem_set_float(ptr, i, val)
def get_float(ptr, i): return lib.mem_get_float(ptr, i)
def sum_float(ptr, size): return lib.mem_sum_float(ptr, size)
def init_float_sequence(ptr, size): lib.mem_init_float_sequence(ptr, size)

# DOUBLE
lib.mem_malloc_double.restype = POINTER(c_double)
lib.mem_set_double.argtypes = [POINTER(c_double), c_int, c_double]
lib.mem_get_double.argtypes = [POINTER(c_double), c_int]
lib.mem_get_double.restype = c_double

lib.mem_sum_double.argtypes = [POINTER(c_double), c_int]
lib.mem_sum_double.restype = c_double

lib.mem_init_double_sequence.argtypes = [POINTER(c_double), c_int]
lib.mem_init_double_sequence.restype = None

lib.mem_scale_double.argtypes = [POINTER(c_double), c_int, c_double]
lib.mem_scale_double.restype = None

lib.mem_fill_double.argtypes = [POINTER(c_double), c_int, c_double]
lib.mem_fill_double.restype = None

lib.mem_dot_product_double.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
lib.mem_dot_product_double.restype = c_double

def scale_double(ptr, size, factor): lib.mem_scale_double(ptr, size, factor)
def fill_double(ptr, size, value): lib.mem_fill_double(ptr, size, value)
def dot_product_double(ptr1, ptr2, size): return lib.mem_dot_product_double(ptr1, ptr2, size)


def malloc_double(n):
    ptr = lib.mem_malloc_double(n)
    if not ptr:
        raise MemoryError(f"Fallo al reservar memoria para {n} doubles.")
    return ptr

def set_double(ptr, i, val): lib.mem_set_double(ptr, i, val)
def get_double(ptr, i): return lib.mem_get_double(ptr, i)
def sum_double(ptr, size): return lib.mem_sum_double(ptr, size)
def init_double_sequence(ptr, size): lib.mem_init_double_sequence(ptr, size)

# FREE
def free(ptr): lib.mem_free(ptr)

from .arrays import IntArray, FloatArray, DoubleArray

__all__ = [
    "malloc_int", "set_int", "get_int", "sum_int", "init_int_sequence", "scale_int", "fill_int", "dot_product_int",
    "malloc_float", "set_float", "get_float", "sum_float", "init_float_sequence", "scale_float", "fill_float", "dot_product_float",
    "malloc_double", "set_double", "get_double", "sum_double", "init_double_sequence", "scale_double", "fill_double", "dot_product_double",
    "free",
    "IntArray", "FloatArray", "DoubleArray"
]
