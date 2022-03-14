import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import stats

# de no existir, se crea la carpeta images para guardar los plot
if (not os.path.exists('./images')):
    os.mkdir('./images')

# solo afectan a los graficos de bondad y ajuste y a los de comparacion visual
# no afectan a los teóricos
mostrar = True
guardar = True

discretas = ['binomial', 'poisson', 'empirica']
# es un arreglo auxiliar para luego ver si la distribución
# enviada como parámetro en la gráfica de chi cuadrado es o no discreta

# graficos de pruebas de bondad y ajuste
# estos son universales para todas las distribuciones
# por eso recibe como parámetro el nombre de la distribucion
# y asi poder guardar el plot de forma dinamica
def bondadKS(_o, _e, distribucion):
    plt.plot(_o, 'bo', label = 'Observado')
    plt.plot(_e, 'ro', label = 'Esperado')
    plt.title('Prueba de bondad y ajuste Kolmogorov-Smirnov')
    plt.xlabel('Intervalo')
    plt.ylabel('Función de distribución acumulada')
    plt.legend()
    if (guardar):
        plt.savefig( 'images/' + distribucion + '-ks' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    plt.clf()

def bondadC(_n, _e, distribucion):
    _a = []
    for i in _n:
        _a.append(i / sum(_n))
    if (isinstance(_e, float)):
        plt.axhline(_e/sum(_n), color = 'r', label = 'F. Esperada')
        plt.ylim(0, _e*3/sum(_n))
    else:
        _b = []
        for i in _e:
            _b.append(i / sum(_e))
        plt.plot(_b, 'ro', label = 'Esperado')
    plt.plot(_a, 'bo', label = "Observado")
    plt.title('Prueba de bondad y ajuste Chi-Cuadrado')
    if (distribucion in discretas):
        plt.xlabel('Valor puntual')
    else:
        plt.xlabel('Intervalo')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    if (guardar):
        plt.savefig( 'images/' + distribucion + '-chi' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    plt.clf()

# gráficos de comparación visual
def uniforme(a, b, ao, bo):
    # lo que esta comentado es para pintar el area de la grafica
    z = 1 / (b-a)
    plt.vlines(b, 0, z, color = 'b', label = 'Esperada')
    plt.vlines(a, 0, z, color = 'b')
    plt.hlines(z, a, b, color = 'b')
    #p1 = [a, a, b, b]
    #p2 = [0, z, z, 0]
    #plt.fill(p1, p2, 'r', alpha = 0.5, label = 'Esperada')

    z = 1 / (bo-ao)
    plt.vlines(bo, 0, z, color = 'r', label = 'Observada')
    plt.vlines(ao, 0, z, color = 'r')
    plt.hlines(z, ao, bo, color = 'r')
    #p1 = [ao, ao, bo, bo]
    #p2 = [0, z, z, 0]
    #plt.fill(p1, p2, 'b', alpha = 0.5, label = 'Observada')
    plt.title('Comparación entre la distribución uniforme observada y esperada')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend(loc = 'lower center')
    if (guardar):
        plt.savefig( 'images/uniforme-empirica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    plt.clf()

def exponencial(lo, ae, cantidad, nros):
    # el primer parametro de la proxima linea es el calculo de las posiciones en x de cada valor generado
    plt.plot((-1/ae)*(np.log(nros) - np.log(ae)), nros, 'bo', label = 'Observada')
    x = np.linspace(0, 5, cantidad)
    # el segundo parametro de la proxima linea es el calculo de la funcion de densidad de probabilidad de la exponencial
    # se usa la formula porque seria la variable teorica o esperada
    plt.plot(x, ae * np.exp(-ae*x), label = 'Esperada', color = 'r')
    # como el valor mas grande que puede tomar la variable es igual a lambda
    # se establece el limite en el eje y en ese valor + 1
    plt.ylim([0, ae+1])
    # se tomo 5 como valor arbitrario porque los siguientes son casi todos 0 generalmente
    plt.xlim([0,5])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Comparación entre la distribución exponencial observada y esperada')
    plt.legend()
    if (guardar):
        plt.savefig( 'images/exponencial-empirica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    plt.clf()

def normal(et, st, eo, so):
    x = np.linspace(stats.norm.ppf(0.01, et, st), stats.norm.ppf(0.99, et, st), 100)
    plt.plot(x, stats.norm.pdf(x, eo, so), 'b', label = 'Observada')
    plt.plot(x, stats.norm.pdf(x, et, st), 'r', label = 'Esperada')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Comparación entre la distribución normal observada y esperada')
    plt.legend()
    if (guardar):
        plt.savefig( 'images/normal-empirica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    plt.clf()

# gráficos para la parte teórica
# la de la uniforme no está porque la de wikipedia era linda
def teoriaExp():
    x = np.linspace(stats.expon.ppf(0.01), stats.expon.ppf(0.99), 100)
    plt.plot(x, stats.expon.pdf(x))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de densidad de probabilidad')
    plt.savefig( 'images/exponencial-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.expon.cdf(x))
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/exponencial-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaGamma():
    a = 4
    x = np.linspace(stats.gamma.ppf(0.01, a), stats.gamma.ppf(0.99, a), 100)
    plt.plot(x, stats.gamma.pdf(x, a))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de densidad de probabilidad')
    plt.savefig( 'images/gamma-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.gamma.cdf(x, a))
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/gamma-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaNormal():
    x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), 100)
    plt.plot(x, stats.norm.pdf(x))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de densidad de probabilidad')
    plt.savefig( 'images/normal-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.norm.cdf(x))
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/normal-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaBinomNegativa():
    n = 3
    p = 0.2
    x = np.arange(stats.nbinom.ppf(0.01, n, p), stats.nbinom.ppf(0.99, n, p))
    plt.plot(x, stats.nbinom.pmf(x, n, p), 'bo')
    plt.vlines(x, 0, stats.nbinom.pmf(x, n, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de masa de probabilidad')
    plt.savefig( 'images/binomNegativa-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.nbinom.cdf(x, n, p), 'bo')
    plt.vlines(x, 0, stats.nbinom.cdf(x, n, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/binomNegativa-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaBinomial():
    n = 1000
    p = 0.1
    x = np.arange(stats.binom.ppf(0.01, n, p), stats.binom.ppf(0.99, n, p))
    plt.plot(x, stats.binom.pmf(x, n, p), 'bo')
    plt.vlines(x, 0, stats.binom.pmf(x, n, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de masa de probabilidad')
    plt.savefig( 'images/binomial-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.binom.cdf(x, n, p), 'bo')
    plt.vlines(x, 0, stats.binom.cdf(x, n, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/binom-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaHiperg():
    N = 30
    n = 5
    p = 0.4
    x = np.arange(0, n+1)
    plt.plot(x, stats.hypergeom.pmf(x, N, N*p, n), 'bo')
    plt.vlines(x, 0, stats.hypergeom.pmf(x, N, N*p, n), colors='b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de masa de probabilidad')
    plt.savefig( 'images/hipergeom-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.hypergeom.cdf(x, N, N*p, n), 'bo')
    plt.vlines(x, 0, stats.hypergeom.cdf(x, N, N*p, n), colors='b')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/hipergeom-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaPoisson():
    p = 2
    x = np.arange(stats.poisson.ppf(0.01, p), stats.poisson.ppf(0.99, p)+5)
    plt.plot(x, stats.poisson.pmf(x, p), 'bo')
    plt.vlines(x, 0, stats.poisson.pmf(x, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de masa de probabilidad')
    plt.savefig( 'images/poisson-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.plot(x, stats.poisson.cdf(x, p), 'bo')
    plt.vlines(x, 0, stats.poisson.cdf(x, p), colors='b')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/poisson-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

def teoriaEmpirica():
    _p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    _F = [0.273, 0.31, 0.505, 0.514, 0.638, 0.696, 0.758, 0.909, 0.956, 1]
    _v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.stem(_v, _p, markerfmt = 'bo', linefmt = 'b', basefmt=" ", use_line_collection=True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función de masa de probabilidad')
    plt.savefig( 'images/empirica-fchica' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()
    plt.stem(_v, _F, markerfmt = 'bo', linefmt = 'b', basefmt=" ", use_line_collection=True)
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Función de distribución acumulada')
    plt.savefig( 'images/empirica-F' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()
    plt.clf()

# ir descomentando para generar las graficas teoricas
# recordar que las teoricas guardan y muestran, no sirven las variables de arriba
# estan pensadas para ejecutarlas una vez, por eso no lo puse
#teoriaExp()
#teoriaGamma()
#teoriaNormal()
#teoriaBinomNegativa()
#teoriaBinomial()
#teoriaHiperg()
#teoriaPoisson()