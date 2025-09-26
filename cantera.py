
# Resolución del problema de las canteras con eliminación de Gauss

def gauss_eliminacion(A, b):
    n = len(A)
    A = [fila[:] for fila in A]
    b = b[:]

    for k in range(n-1):
        max_fila = max(range(k, n), key=lambda i: abs(A[i][k]))
        if max_fila != k:
            A[k], A[max_fila] = A[max_fila], A[k]
            b[k], b[max_fila] = b[max_fila], b[k]
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    x = [0]*n
    for i in range(n-1, -1, -1):
        suma = b[i] - sum(A[i][j]*x[j] for j in range(i+1, n))
        x[i] = suma / A[i][i]
    return x

if __name__ == "__main__":
    # Coeficientes en %
    A = [
        [55, 25, 25],
        [30, 45, 20],
        [15, 30, 55]
    ]
    # Demandas multiplicadas x100
    b = [480000, 580000, 570000]

    solucion = gauss_eliminacion(A, b)
    print("Cantidad a extraer de cada cantera:")
    for i, val in enumerate(solucion, start=1):
        print(f"Cantera {i}: {val:.2f} m3")
