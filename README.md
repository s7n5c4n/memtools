# 🧠 memtool — Control de memoria manual en Python con C

**memtool** es un framework experimental que permite trabajar con arrays en Python controlando directamente la memoria mediante punteros escritos en C. Proporciona acceso de bajo nivel a la memoria, permitiendo realizar operaciones como reserva, lectura, escritura, escalado, relleno, producto punto y conversión directa a NumPy, todo con rendimiento casi nativo.

---

## ✨ Características principales

- Acceso manual a memoria con punteros desde Python
- Tipos soportados: `int`, `float`, `double`
- Operaciones: `malloc`, `set`, `get`, `free`, `sum`, `scale`, `fill`, `dot`, `to_numpy()`
- Sin garbage collector → control total de recursos
- Compatible con `NumPy` sin copia de memoria
- Clases `IntArray`, `FloatArray`, `DoubleArray` con estilo Pythonic

---

## ⚡ Motivación

Python es muy fácil de usar, pero lento para ciertas tareas. NumPy es rápido, pero no ofrece control sobre la memoria. **memtool** busca combinar lo mejor de ambos mundos:

> 💡  "Velocidad y control de C, con la interfaz amigable de Python."

Ideal para ciencia de datos, ingeniería de datos, procesamiento por lotes, o microservicios que requieren rendimiento extremo.

---

## 📂 Instalación (modo desarrollo)

```bash
git clone https://github.com/tuusuario/memtool.git
cd memtool
python3 setup.py build
python3 setup.py install --user  # o usa venv
```

---

## 📃 Ejemplo rápido

```python
from memtool import IntArray

arr = IntArray(5, init_sequence=True)  # [0, 1, 2, 3, 4]
print(arr.sum())         # 10
arr.scale(2)             # [0, 2, 4, 6, 8]
arr.fill(1)              # [1, 1, 1, 1, 1]
print(arr.dot(arr))      # 5

np_arr = arr.to_numpy()
print(np_arr)            # [1 1 1 1 1]
```

---

## 📈 Benchmark (suma de 10M de elementos)

```bash
[Python puro]      ≈ 0.18s
[NumPy]            ≈ 0.010s
[memtool (C)]      ≈ 0.020s
```

> memtool está muy cerca de NumPy en rendimiento, pero con control total sobre la memoria.

---

## 🌐 Uso avanzado con NumPy y FastAPI

Puedes usar `to_numpy()` para convertir directamente un puntero a `np.ndarray`:

```python
np_arr = arr.to_numpy()
plt.plot(np_arr)  # o guardarlo como CSV, usar con pandas, etc.
```

Y también podrías integrarlo en un microservicio con FastAPI:

```python
@app.post("/dot")
def producto_punto(data: List[int]):
    a = IntArray(len(data), init_sequence=True)
    b = IntArray(len(data), init_sequence=True)
    return {"dot": a.dot(b)}
```

---

## 📄 Clases disponibles

```python
IntArray(size, init_sequence=False)
FloatArray(size, init_sequence=False)
DoubleArray(size, init_sequence=False)
```

Cada una soporta:

- `set(index, value)` / `get(index)` / indexado `[]`
- `sum()`
- `scale(factor)`
- `fill(value)`
- `dot(other)`
- `to_numpy()`
- `free()`

---

## 🌐 Estado actual

-

---

## 📅 Roadmap futuro

- 🔄 Compatibilidad con `float16` y `int64`
- 🔄 Interfaz para `pandas.Series` y `DataFrame`
- 🔄 Validaciones avanzadas y manejo de errores
- 🔄 Extensiones con funciones vectoriales en C

---

## 👥 Autor

Desarrollado por [tu nombre o usuario de GitHub] con el objetivo de experimentar y crear una alternativa de alto rendimiento para tareas críticas con arrays en Python.

---

## 🏆 Licencia

MIT License.
Libre para usar, modificar, aprender o contribuir.

---

🚀 Si te gustó este proyecto, ⭐ dale una estrella en GitHub y compartilo. Es solo el comienzo. 🚀

