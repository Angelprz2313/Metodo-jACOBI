"""
Programa: Método de Jacobi para resolver sistemas de ecuaciones lineales
Autor: [Tu Nombre]
Descripción:
    Este programa resuelve un sistema de ecuaciones lineales Ax = b 
    utilizando el método iterativo de Jacobi. 
    Además, verifica si la matriz es diagonalmente dominante.
"""

def es_diagonalmente_dominante(A):
    """
    Verifica si la matriz A es diagonalmente dominante.
    Una matriz es diagonalmente dominante si:
        |a_ii| >= suma(|a_ij|) para todo i, j != i
    """
    n = len(A)
    for i in range(n):
        suma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) < suma:
            return False
    return True


def metodo_jacobi(A, b, tol=1e-4, max_iter=1000):
    """
    Resuelve el sistema Ax = b con el método de Jacobi.
    Parámetros:
        A : matriz de coeficientes
        b : vector independiente
        tol : tolerancia (criterio de paro)
        max_iter : número máximo de iteraciones
    Retorna:
        x : vector aproximado solución
    """
    n = len(A)
    x = [0.0 for _ in range(n)]  # Vector inicial (x0 = 0)
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i][i]
        
        # Criterio de convergencia: norma infinito
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new
        x = x_new
    return x


# ------------------- PROGRAMA PRINCIPAL -------------------
if __name__ == "__main__":
    # Lectura de datos
    n = int(input())  # Tamaño del sistema
    A = []
    b = []
    for _ in range(n):
        fila = list(map(float, input().split()))
        A.append(fila[:-1])  # Coeficientes
        b.append(fila[-1])   # Término independiente

    # Verificación de diagonal dominante
    if es_diagonalmente_dominante(A):
        print("DD")  # Diagonalmente Dominante
        x = metodo_jacobi(A, b)
        print(" ".join(f"{val:.4f}" for val in x))
    else:
        print("DND")  # Diagonal No Dominante
        print(0)
