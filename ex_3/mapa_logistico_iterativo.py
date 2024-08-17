import numpy as np

def mapIt(n: int, x_0: float, a):
    lista = []
    lista.append(x_0)

    for i in range(1,n):
        lista.append(lista[i-1]*a*(1-lista[i-1]))

    return lista


def media(arr: list):
    n = len(arr)
    soma = 0

    for i in range(n):
        soma += arr[i]

    return (soma/n)

def variancia(arr: list):
    somaMed = 0
    somaVar = 0
    n = len(arr)

    for i in range(n):
        somaMed += arr[i]
    med = somaMed/n

    for i in range(n):
        somaVar += (arr[i] - med)**2

    return (somaVar/n)


lista = mapIt(3, (0.1), 1)
print("Valores obtidos para n = 3: {}".format(lista))

media = media(lista)
print("Media pela função: {}".format(media))

print("variancia pela função: {}".format(variancia(lista, media)))

average = np.average(lista)
print("media pelo numpy: {}".format(average))

variance = np.var(lista)
print("variancia pelo numpy: {}".format(variance))