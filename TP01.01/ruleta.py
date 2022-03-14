import numpy as np
import matplotlib.pyplot as plt

num = range(37)
decimales = 4

def fr(n):
    _f = np.round(num.count(n)/len(num), decimales)
    return _f

def media():
    _m = np.round(np.mean(num), decimales)
    return _m

def std():
    _s = np.round(np.std(num), decimales)
    return _s

def var():
    _v = np.round(np.var(num), decimales)
    return _v

# graficar frecuencias relativas de los valores de la ruleta
def graficar():
    _aux = []
    for n in num:
        _aux.append(fr(n))
    plt.stem(num, _aux)
    plt.title("Esperado")
    plt.xlabel("Número")
    plt.ylabel("Frecuencia relativa")
    plt.xlim(-0.5,36.5)
    plt.ylim(0,0.05)
    plt.show()
