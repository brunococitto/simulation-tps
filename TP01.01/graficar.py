import ruleta as r
import corrida as c
import matplotlib.pyplot as plt
import numpy as np

# gráfico frecuencia relativa
def fr(c, nF, nT):
    fe = r.fr(nF)
    plt.hlines(fe, 0, nT, 'k', zorder = len(c))
    for i in c:
        plt.plot(i.evFNum(nF), label=c.index(i)+1, zorder = c.index(i))
        plt.legend()
    plt.title("Frecuencia relativa esperada vs evolución del número fijo")
    plt.xlabel("Cantidad de tiradas")
    plt.ylabel("Frecuencia relativa")
    plt.xlim(0,nT)
    plt.ylim(0,0.1)
    plt.show()

# gráfico media aritmética
def media(c, nT):
    me = r.media()
    plt.hlines(me, 0, nT, 'k', zorder = len(c))
    for i in c:
        plt.plot(i.evMedia(), label=c.index(i)+1, zorder = c.index(i))
        plt.legend()
    plt.title("Media esperada vs evolución")
    plt.xlabel("Tiradas")
    plt.ylabel("Media aritmética")
    plt.xlim(0,nT)
    plt.ylim(15,20)
    plt.show()

# gráfico desvío estándar
def std(c, nT):
    se = r.std()
    plt.hlines(se, 0, nT, 'k', zorder = len(c))
    for i in c:
        plt.plot(i.evStd(), label=c.index(i)+1, zorder = c.index(i))
        plt.legend()
    plt.title("Evolución del desvío estándar")
    plt.xlabel("Tiradas")
    plt.ylabel("Desvío estándar")
    plt.xlim(0,nT)
    plt.ylim(8,13)
    plt.show()

# gráfico variancia
def var(c, nT):
    _ve = r.var()
    plt.hlines(_ve, 0, nT, 'k', zorder = len(c))
    for i in c:
        plt.plot(i.evVar(), label=c.index(i)+1, zorder = c.index(i))
        plt.legend()
    plt.title("Evolución de la varianza")
    plt.xlabel("Tiradas")
    plt.ylabel("Varianza")
    plt.xlim(0,nT)
    plt.ylim(100,130)
    plt.show()

# gráfico media de medias
def mom(c):
    plt.plot(evMom(c))
    plt.title("Evolución de la media de las medias")
    plt.xlabel("Corridas")
    plt.ylabel("Media aritmética")
    plt.xlim(0,len(c)-1)
    plt.ylim(17,19)
    plt.xticks(range(len(c)), range(1,len(c)+1))
    plt.show()

# método para generar un arreglo con la evolución de la media de las medias
def evMom(c):
    _aux = []
    _eM = []
    for i in c:
        _aux.append(i.media())
        _eM.append(np.mean(_aux))
    return _eM

# gráfico media de desvíos
def mos(c):
    plt.plot(evMos(c))
    plt.title("Evolución de la media de los desvíos")
    plt.xlabel("Corridas")
    plt.ylabel("Desvío estándar")
    plt.xlim(0,len(c)-1)
    plt.ylim(10,11)
    plt.xticks(range(len(c)), range(1,len(c)+1))
    plt.show()

# método para generar un arreglo con la evolución de la media de los desvíos
def evMos(c):
    _aux = []
    _eS = []
    for i in c:
        _aux.append(i.std())
        _eS.append(np.mean(_aux))
    return _eS

# gráfico media de varianzas
def mov(c):
    plt.plot(evMov(c))
    plt.title("Evolución de la media de las varianzas")
    plt.xlabel("Corridas")
    plt.ylabel("Varianza")
    plt.xlim(0,len(c)-1)
    plt.ylim(112,116)
    plt.xticks(range(len(c)), range(1,len(c)+1))
    plt.show()

# método para generar un arreglo con la evolución de la media de la varianza
def evMov(c):
    _aux = []
    _eV = []
    for i in c:
        _aux.append(i.var())
        _eV.append(np.mean(_aux))
    return _eV

# graficar frecuencias relativas de todos los valores
def fRelativas(c, nT):
    _aux = []
    _fr = 1/37
    for i in c:
        for n in r.num:
            _aux.append(i.fNum(n))
    plt.stem(r.num, _aux, basefmt="", use_line_collection=True)
    plt.hlines(_fr, 0, nT, 'k', zorder = len(r.num))
    plt.title(str(nT) + ' tiradas')
    plt.xlabel("Número")
    plt.ylabel("Frecuencia relativa")
    plt.xlim(0,36)
    plt.ylim(0,0.05)
    plt.show()