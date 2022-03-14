import generadoresVariables as genVar
import pruebas as test
import graficos as g
import numpy as np

cantidad = 5000 # cantidad de números a generar

# CONTINUAS
# uniforme
def uniforme():
    # opción 1 con a y b
    a = 10
    b = 20
    # opción 2 con esperanza y varianza
    # esp = 15
    # var = 2.5
    # a = esp - (3*var*esp)**(1/2)
    # b = 2 * esp - a

    X = genVar.uniforme(a, b, cantidad)

    mediaTeorica = (a+b)/2
    mediaEmpirica = np.mean(X)
    varianciaTeorica = (b-a)**2/12
    varianciaEmpirica = np.var(X)

    print('Distribución uniforme')
    print('Prueba de Chi-Cuadrado:', test.chiUniforme(X))
    print('Prueba de Kolmogorov-Smirnov:', test.ksUniforme(X, a, b))
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

    g.uniforme(a, b, min(X), max(X))

#exponencial
def exponencial():
    a = 2 # parámetro

    X = genVar.exponencial(a, cantidad)

    mediaTeorica = 1/a
    mediaEmpirica = np.mean(X)
    varianciaTeorica = 1/ (a**2)
    varianciaEmpirica = np.var(X)

    print('Distribución exponencial')
    print('Prueba de Chi-Cuadrado:', test.chiExponencial(X, a))
    print('Prueba de Kolmogorov-Smirnov:', test.ksExponencial(X, a))
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

    g.exponencial(np.mean(X),a, cantidad, X)

# gamma
def gamma():
    k = 5 # cantidad de exponenciales que se suman
    a = 2 # parametro de la exponencial

    X = genVar.gamma(k, a, cantidad)

    mediaTeorica = k/a
    mediaEmpirica = np.mean(X)
    varianciaTeorica = k/(a**2)
    varianciaEmpirica = np.var(X)

    print('Distribución Gamma')
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# normal
def normal():
    k = 10
    esp = 4 # esperanza
    std = 1.5 # desvío estándar

    X = genVar.normal(k, esp, std, cantidad)

    print('Distribución Normal')
    print('Prueba de Chi-Cuadrado:', test.chiNormal(X, esp, std))
    print('Prueba de Kolmogorov-Smirnov:', test.ksNormal(X, esp, std))
    print('Media teórica:', esp)
    print('Media empírica:', np.mean(X))
    print('Diferencia:', abs(np.mean(X)-esp))
    print('Desvío estándar teórico:', std)
    print('Desvío estándar empírico:', np.std(X))
    print('Diferencia:', abs(np.std(X)-std))

    g.normal(esp, std, np.mean(X), np.std(X))

# DISCRETAS
# binomial negativa
def binomNegativa():
    k = 20
    q = 0.3
    p = 1 - q

    X = genVar.binomNegativa(k, q, cantidad)

    mediaTeorica = k * q / p
    mediaEmpirica = np.mean(X)
    varianciaTeorica = k * q / (p**2)
    varianciaEmpirica = np.var(X)

    print('Distribución binomial negativa')
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# binomial
def binomial():
    n = 10
    p = 0.5

    X = genVar.binomial(n, p, cantidad)

    mediaTeorica = n*p
    mediaEmpirica = np.mean(X)
    varianciaTeorica = n*p*(1-p)
    varianciaEmpirica = np.var(X)

    print('Distribución binomial')
    print('Prueba de Chi-Cuadrado:', test.chiBinomial(X, n, p))
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# hipergeométrica
def hipergeometrica():
    N = 10
    n = 5
    p = 0.1

    X = genVar.hipergeometrica(N, n, p, cantidad)

    mediaTeorica = n*p
    mediaEmpirica = np.mean(X)
    varianciaTeorica = n*p*(1-p)*((N-n)/(N-1))
    varianciaEmpirica = np.var(X)

    print('Distribución hipergeométrica')
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# poisson
def poisson():
    p = 2

    X = genVar.poisson(p, cantidad)

    mediaTeorica = p
    mediaEmpirica = np.mean(X)
    varianciaTeorica = p
    varianciaEmpirica = np.var(X)

    print('Distribución Poisson')
    print('Prueba de Chi-Cuadrado:', test.chiPoisson(X, p))
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# empírica discreta
def empiricaD():
    # probabilidades fijas, se podrian cambiar (agregar, quitar, modificar)
    _p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]

    X = genVar.empiricaD(cantidad, _p)
    
    mediaTeorica = 0
    for i in range(len(_p)):
        mediaTeorica += _p[i] * i
    
    mediaCuad = 0 # media de los valores de X al cuadrado
    for i in range(len(_p)):
        mediaCuad += _p[i] * (i**2)
    varianciaTeorica = mediaCuad- mediaTeorica**2

    mediaEmpirica = np.mean(X)
    varianciaEmpirica = np.var(X)

    print('Distribución Empírica discreta')
    print('Prueba de Chi-Cuadrado:', test.chiEmpirica(X, _p))
    print('Media teórica:', mediaTeorica)
    print('Media empírica:', mediaEmpirica)
    print('Diferencia:', abs(mediaEmpirica-mediaTeorica))
    print('Variancia teórica:', varianciaTeorica)
    print('Variancia empírica:', varianciaEmpirica)
    print('Diferencia:', abs(varianciaEmpirica-varianciaTeorica))

# ir descomentando el método acá abajo para ejecutar cada distribución
# CONTINUAS
#uniforme()
#exponencial()
#gamma()
#normal()
# DISCRETAS
#binomNegativa()
#binomial()
#hipergeometrica()
#poisson()
#empiricaD()