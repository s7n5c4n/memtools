// memtool/core.c
#include <stdlib.h>
#include <stdio.h> 

// INT
void* mem_malloc_int(int size) {
    return malloc(size * sizeof(int));
}

void mem_set_int(int* ptr, int index, int value) {
    ptr[index] = value;
}

int mem_get_int(int* ptr, int index) {
    return ptr[index];
}

// FLOAT
void* mem_malloc_float(int size) {
    return malloc(size * sizeof(float));
}

void mem_set_float(float* ptr, int index, float value) {
    ptr[index] = value;
}

float mem_get_float(float* ptr, int index) {
    return ptr[index];
}

// DOUBLE
void* mem_malloc_double(int size) {
    return malloc(size * sizeof(double));
}

void mem_set_double(double* ptr, int index, double value) {
    ptr[index] = value;
}

double mem_get_double(double* ptr, int index) {
    return ptr[index];
}

// FREE
void mem_free(void* ptr) {
    free(ptr);
}

// SUM INT
long long mem_sum_int(int* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido.\n");
        return 0;
    }

    long long total = 0;
    for (int i = 0; i < size; i++) {
        total += ptr[i];
    }
    return total;
}

// RESTA INT
long long mem_subtract_int(int* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido.\n");
        return 0;
    }

    long long total = 0;
    for (int i = 0; i < size; i++) {
        total -= ptr[i];
    }
    return total;
}
// MULTIPLICACION INT
long long mem_multiply_int(int* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido.\n");
        return 0;
    }

    long long total = 1;
    for (int i = 0; i < size; i++) {
        total *= ptr[i];
    }
    return total;
}
// DIVISION INT
long long mem_divide_int(int* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido.\n");
        return 0;
    }

    long long total = 1;
    for (int i = 0; i < size; i++) {
        if (ptr[i] != 0) {
            total /= ptr[i];
        } else {
            printf("Error: división por cero en el índice %d.\n", i);
            return 0;
        }
    }
    return total;
}

// fOR INT
void mem_init_int_sequence(int* ptr, int size) {
    for (int i = 0; i < size; i++) {
        ptr[i] = i;
    }
}

// Escalar todos los elementos de un array de enteros
void mem_scale_int(int* ptr, int size, int factor) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] *= factor;
    }
}

// Rellenar array de enteros con un valor constante
void mem_fill_int(int* ptr, int size, int value) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] = value;
    }
}

// Producto punto entre dos arrays de enteros
long long mem_dot_product_int(int* a, int* b, int size) {
    if (a == NULL || b == NULL || size <= 0) {
        return 0;
    }

    long long total = 0;
    for (int i = 0; i < size; i++) {
        total += (long long)a[i] * (long long)b[i];
    }
    return total;
}


// SUMA FLOAT
float mem_sum_float(float* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (float).\n");
        return 0.0f;
    }

    float total = 0.0f;
    for (int i = 0; i < size; i++) {
        total += ptr[i];
    }
    return total;
}

// RESTA FLOAT
float mem_subtract_float(float* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (float).\n");
        return 0.0f;
    }

    float total = 0.0f;
    for (int i = 0; i < size; i++) {
        total -= ptr[i];
    }
    return total;
}
// MULTIPLICACION FLOAT
float mem_multiply_float(float* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (float).\n");
        return 0.0f;
    }

    float total = 1.0f;
    for (int i = 0; i < size; i++) {
        total *= ptr[i];
    }
    return total;
}
// DIVISION FLOAT
float mem_divide_float(float* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (float).\n");
        return 0.0f;
    }

    float total = 1.0f;
    for (int i = 0; i < size; i++) {
        if (ptr[i] != 0.0f) {
            total /= ptr[i];
        } else {
            printf("Error: división por cero en el índice %d.\n", i);
            return 0.0f;
        }
    }
    return total;
}

// INICIALIZAR FLOAT SECUENCIAL
void mem_init_float_sequence(float* ptr, int size) {
    for (int i = 0; i < size; i++) {
        ptr[i] = (float)i;
    }
}
void mem_scale_float(float* ptr, int size, float factor) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] *= factor;
    }
}

void mem_fill_float(float* ptr, int size, float value) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] = value;
    }
}

float mem_dot_product_float(float* a, float* b, int size) {
    if (a == NULL || b == NULL || size <= 0) return 0.0f;
    float total = 0.0f;
    for (int i = 0; i < size; i++) {
        total += a[i] * b[i];
    }
    return total;
}

// SUMA DOUBLE
double mem_sum_double(double* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (double).\n");
        return 0.0;
    }

    double total = 0.0;
    for (int i = 0; i < size; i++) {
        total += ptr[i];
    }
    return total;
}

// RESTA DOUBLE
double mem_subtract_double(double* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (double).\n");
        return 0.0;
    }

    double total = 0.0;
    for (int i = 0; i < size; i++) {
        total -= ptr[i];
    }
    return total;
}

// MULTIPLICACION DOUBLE
double mem_multiply_double(double* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (double).\n");
        return 0.0;
    }

    double total = 1.0;
    for (int i = 0; i < size; i++) {
        total *= ptr[i];
    }
    return total;
}

// DIVISION DOUBLE
double mem_divide_double(double* ptr, int size) {
    if (ptr == NULL || size <= 0) {
        printf("Error: puntero nulo o tamaño inválido (double).\n");
        return 0.0;
    }

    double total = 1.0;
    for (int i = 0; i < size; i++) {
        if (ptr[i] != 0.0) {
            total /= ptr[i];
        } else {
            printf("Error: división por cero en el índice %d.\n", i);
            return 0.0;
        }
    }
    return total;
}

// INICIALIZAR DOUBLE SECUENCIAL
void mem_init_double_sequence(double* ptr, int size) {
    for (int i = 0; i < size; i++) {
        ptr[i] = (double)i;
    }
}

void mem_scale_double(double* ptr, int size, double factor) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] *= factor;
    }
}

void mem_fill_double(double* ptr, int size, double value) {
    if (ptr == NULL || size <= 0) return;
    for (int i = 0; i < size; i++) {
        ptr[i] = value;
    }
}

double mem_dot_product_double(double* a, double* b, int size) {
    if (a == NULL || b == NULL || size <= 0) return 0.0;
    double total = 0.0;
    for (int i = 0; i < size; i++) {
        total += a[i] * b[i];
    }
    return total;
}
