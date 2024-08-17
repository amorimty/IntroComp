

def mapLogistico(n, a, x_0):
    if n > 0:
        x_anterior = mapLogistico((n - 1), a, x_0)
        return a * x_anterior * (1 - x_anterior)
    elif n == 0:
        return x_0
    
print(mapLogistico(3, 1, 0.1))