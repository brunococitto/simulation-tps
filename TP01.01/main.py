import corrida as c
import ruleta as r
import graficar as g
import numpy as np

# defino valores e inicializo variables antes de ejecutar el programa
corridas = []
nCorridas = int(input("Ingrese el número de corridas: "))
nTiradas = int(input("Ingrese el número de tiradas por corrida: "))
nFijo = int(input("Ingrese el número sobre el cual se calculará la frecuencia relativa del valor fijo: "))

# cargo arreglo con las corridas
for n in range(nCorridas):
    corridas.append(c.corrida(nTiradas))

# media aritmética de las medias airtméticas
def mom(corridas):
    _aux = []
    for n in corridas:
        _aux.append(n.media())
    _mom = np.round(np.mean(_aux), 4)
    return _mom

# media aritmética de los desvíos
def mos(corridas):
    _aux = []
    for n in corridas:
        _aux.append(n.std())
    _mos = np.round(np.mean(_aux), 4)
    return _mos

# media aritmética de las varianzas
def mov(corridas):
    _aux = []
    for n in corridas:
        _aux.append(n.var())
    _mov = np.round(np.mean(_aux), 4)
    return _mov

# mostrar valores característicos de la corrida
# mostrar frecuencia relativa esperada
print("Frecuencia relativa ESPERADA del valor", nFijo, ":", r.fr(nFijo))
# mostrar frecuencias relativas reales del valor fijo
for n in range(nCorridas):
    print("Frecuencia relativa REAL del valor", nFijo, "en la corrida N°", n+1, ":", corridas[n].fNum(nFijo))
# mostrar media esperada
print("Media arimética ESPERADA de la corrida:", r.media())
# mostrar medias reales
for n in range(nCorridas):
    print("Media aritmética REAL de la corrida N°", n+1, ":", corridas[n].media())
# mostrar desvío estándar esperado
print("Desvío estándar ESPERADO de la corrida:", r.std())
# mostrar desvíos reales
for n in range(nCorridas):
    print("Desvío estandar REAL de la corrida N°", n+1, ":", corridas[n].std())
# mostrar varianza esperada
print("Varianza ESPERADA de la corrida:", r.var())
# mostrar varianzas reales
for n in range(nCorridas):
    print("Varianza REAL de la corrida N°", n+1, ":", corridas[n].var())
# fin mostrar valores

# gráficos de valores característicos de las corridas
    g.fr(corridas, nFijo, nTiradas)
    g.fRelativas(corridas, nTiradas)
    g.media(corridas, nTiradas)
    g.std(corridas, nTiradas)
    g.var(corridas, nTiradas)

# mostrar promedios o medias aritméticas de los valores característicos
# esto solo se hace si hay más de una corrida, si no no tiene sentido
# pues sería el mismo valor que los anteriores
if (nCorridas > 1):
    # media de las medias
    print("Media aritmética de las medias airméticas:", mom(corridas))
    # media de los desvíos
    print("Media aritmética de los desvíos:", mos(corridas))
    # media de las varianzas
    print("Media aritmética de las varianzas:", mov(corridas))
# gráficos de valores característicos de valores característicos
    # media de las medias
    g.mom(corridas)
    # media de los desvíos
    g.mos(corridas)
    # media de las varianzas
    g.mov(corridas)