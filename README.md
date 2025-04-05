# memtool

![PyPI version](https://img.shields.io/pypi/v/memtool)
![License](https://img.shields.io/pypi/l/memtool)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

> A low-level memory manager for Python that lets you allocate, manipulate, and free memory manually using C, with a clean Pythonic interface.

---

## 🚀 What is `memtool`?

`memtool` is a Python library that allows **manual memory control** using **C-level performance**. It gives you:

- Raw access to memory through pointers
- Zero-copy conversion to NumPy arrays
- Support for `int`, `float`, and `double`
- Operations written in C for blazing fast performance
- Safe, Pythonic wrappers (with OOP-style arrays)

### ⚠️ Hardcore mode activated
You're no longer in safe Python land — with `memtool` you're directly manipulating memory using C pointers under the hood.

This tool is designed for **power users, data engineers, and performance-focused developers** who want to:

- Get closer to hardware-level optimization
- Control how memory is allocated and freed
- Replace performance bottlenecks in Python with native C speed

If you're familiar with `malloc`, `free`, and pointer arithmetic in C/C++, you'll feel at home.
If not — proceed with curiosity and caution 🧠

---

## 📦 Installation

From PyPI:

```bash
pip install memtool
```

---

## ✅ Supported types

- `IntArray`
- `FloatArray`
- `DoubleArray`

All backed by real pointers in C.

---

## 📘 Quick Example

```python
from memtool import IntArray

arr = IntArray(10, init_sequence=True)
print(arr[0], arr[5])  # Output: 0 5

arr[2] = 999
print(arr[2])  # Output: 999

print("Sum:", arr.sum())

arr.free()  # Optional: memory is freed automatically at destruction
```

---

## 🔬 Manual Memory Access: Allocate, Modify and Free

You can create raw memory blocks using the lower-level API:

```python
from memtool import malloc_int, set_int, get_int, sum_int, free

# Allocate memory for 100 integers
ptr = malloc_int(100)

# Write values manually
for i in range(100):
    set_int(ptr, i, i * 2)

# Access values
print(get_int(ptr, 10))  # Output: 20

# Compute sum (on the C side)
print("Sum:", sum_int(ptr, 100))

# Free memory manually (important if not using wrapper class)
free(ptr)
```

---

## 🤖 Use Case: Integrate with ML Pipeline

You can combine `memtool` with NumPy to prepare fast memory-backed datasets for ML models:

```python
from memtool import FloatArray
from sklearn.linear_model import LinearRegression

# Allocate and initialize features (X) and labels (y)
X = FloatArray(1000, init_sequence=True)
y = FloatArray(1000)

for i in range(1000):
    y[i] = X[i] * 3.5 + 1.2  # y = 3.5x + 1.2

# Convert to NumPy for training
X_np = X.to_numpy().reshape(-1, 1)
y_np = y.to_numpy()

model = LinearRegression().fit(X_np, y_np)
print("Coef:", model.coef_, "Intercept:", model.intercept_)

# Cleanup
X.free()
y.free()
```

This allows you to keep the allocation in fast memory and avoid the overhead of Python list creation.

---

## 🧠 Advanced: Use with NumPy (zero-copy)

```python
import numpy as np
from memtool import IntArray

arr = IntArray(1000000, init_sequence=True)
np_arr = arr.to_numpy()  # ⚠️ No memory copy!

print(np_arr[:5])
print(np_arr.sum())
```

---

## 🧰 API Overview

Each type (`IntArray`, `FloatArray`, `DoubleArray`) supports:

- `set(index, value)` / `get(index)`
- `__getitem__`, `__setitem__`
- `sum()` — C-level summation
- `scale(factor)` — Multiply all values
- `fill(value)` — Fill memory with constant
- `dot_product(other)` — C-level dot product
- `to_numpy()` — NumPy view without copy

---

## 🔒 Memory safety

Although it uses raw C memory, the Python classes **automatically free memory** on deletion and avoid out-of-bounds access.

You can also call `.free()` manually when needed.

**Note:** Misuse of pointers can still lead to segmentation faults. This tool assumes you know what you're doing.

---

## 📈 Benchmarks

```bash
python benchmark_sum.py
```

| Operation   | Time       |
|-------------|------------|
| Python `sum`| ~0.18s     |
| NumPy       | ~0.01s     |
| memtool C   | ~0.01–0.02s|

---

## 🛠️ Build from source

```bash
git clone https://github.com/s7n5c4n/memtools.git
cd memtools
python3 -m build
```

---

## 🧪 Run tests

```bash
python3 -m memtool.test.test_basic
```

---

## 📄 License

MIT License. Open to contributions, forks and feedback!

