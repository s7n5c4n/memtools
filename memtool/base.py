# memtool/base.py
import numpy as np
import ctypes


class BaseArray:
    def __init__(self, size, ptr, set_func, get_func, sum_func, free_func, scale_func=None, fill_func=None,  dot_func=None):
        self.size = size
        self.ptr = ptr
        self._set = set_func
        self._get = get_func
        self._sum = sum_func
        self._free = free_func
        self._scale = scale_func
        self._fill = fill_func
        self._dot = dot_func
        self._freed = False

    def set(self, index, value):
        if 0 <= index < self.size:
            self._set(self.ptr, index, value)
        else:
            raise IndexError("Índice fuera de rango")

    def get(self, index):
        if 0 <= index < self.size:
            return self._get(self.ptr, index)
        else:
            raise IndexError("Índice fuera de rango")

    def sum(self):
        return self._sum(self.ptr, self.size)

    def __getitem__(self, index): return self.get(index)
    def __setitem__(self, index, value): self.set(index, value)
    def __len__(self): return self.size

    def free(self):
        if not self._freed:
            self._free(self.ptr)
            self._freed = True

    def __del__(self):
        self.free()

    def scale(self, factor):
        if self._scale is None:
            raise NotImplementedError("Esta clase no soporta scale().")
        self._scale(self.ptr, self.size, factor)

    def fill(self, value):
        if self._fill is None:
            raise NotImplementedError("Esta clase no soporta fill().")
        self._fill(self.ptr, self.size, value)

    def dot(self, other):
        if self._dot is None:
            raise NotImplementedError("Esta clase no soporta dot().")
        if not isinstance(other, BaseArray):
            raise TypeError("dot() solo acepta otro BaseArray.")
        if self.size != other.size:
            raise ValueError("Los arrays deben tener el mismo tamaño.")
        return self._dot(self.ptr, other.ptr, self.size)
    
    def to_numpy(self):
        """Retorna un np.ndarray que referencia directamente a la memoria del puntero."""
        if isinstance(self.ptr, ctypes._Pointer):
            return np.ctypeslib.as_array(self.ptr, shape=(self.size,))
        else:
            raise TypeError("El puntero no es compatible con ctypes para convertir a NumPy.")


