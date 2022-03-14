import math
import graficos as g
import numpy as np
from scipy import stats

def chiUniforme(_nros):
    _n = len(_nros)
    _m = 15 # cantidad de intervalos
    _p = (max(_nros) - min(_nros)) / _m # tamaño de intervalo
    _i = min(_nros) # limite inferior del intervalo
    _s = _i + _p # limite superior del intervalo
    _oi = [] # arreglo de frecuencias observadas
    _ei = _n / _m # cálculo del valor esperado (es igual para todos los intervalos)
    _aux = 0 # acumulador para comparar los estadisticos
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n > _i and n <= _s for n in _nros))
        _i += _p # incremento el limite inferior
        _s += _p # incremento el limite superior
        _aux += (_oi[i] - _ei)**2 / _ei # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1)
    _r = _aux < _c
    g.bondadC(_oi, _ei, 'uniforme')
    return _r

def ksUniforme(_nros, a, b):
    _n = len(_nros)
    _m = math.trunc(math.sqrt(_n)) # cantidad de intervalos
    _p = (max(_nros) - min(_nros)) / _m # tamaño de intervalo
    _s = min(_nros) + _p # limite superior del intervalo
    _oi = [] # arreglo de F observadas
    _ei = [] # arreglo de F esperadas
    _d = [] # arreglo de estadisticos D
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n <= _s for n in _nros) / _n)
        _ei.append((_s - a) / (b - a))
        _s += _p # incremento el limite superior
        _d.append(abs(_ei[i] - _oi[i]))
    _dmax = max(_d)
    _vc = 1.36 / math.sqrt(_n)
    _r = _dmax < _vc
    g.bondadKS(_oi, _ei, 'uniforme')
    return _r

def chiExponencial(_nros, a):
    _n = len(_nros)
    _m = 15 # cantidad de intervalos
    _p = 1 / _m # probabilidad de cada intervalo
    _t = [] # tamaños de intervalo
    for i in range(1, _m):
        _t.append(-(1/a) * math.log(1 - i * _p)) # se calculan los limites superiores  de los intervalos
    _i = 0 # limite inferior del intervalo
    _s = _i + _t[0] # limite superior del intervalo
    _oi = [] # arreglo de frecuencias observadas
    _ei = _n / _m # cálculo del valor esperado (es igual para todos los intervalos)
    _aux = 0 # acumulador para comparar los estadisticos
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        if (i == _m - 1):
            _oi.append(sum(n > _i for n in _nros))
        else:
            _oi.append(sum(n > _i and n <= _s for n in _nros))
            _i = _t[i] # incremento el limite inferior
            if (i != _m - 2):
                _s = _t[i+1] # incremento el limite superior
        _aux += (_oi[i] - _ei)**2 / _ei # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1)
    _r = _aux < _c
    g.bondadC(_oi, _ei, 'exponencial')
    return _r

def ksExponencial(_nros, a):
    _n = len(_nros)
    _m = math.trunc(math.sqrt(_n)) # cantidad de intervalos
    _a = (max(_nros) - min(_nros)) / _m # amplitud del intervalo
    _s = _a # limite superior del intervalo
    _oi = [] # arreglo de F observadas
    _ei = [] # arreglo de F esperadas
    _d = [] # arreglo de estadisticos D
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n <= _s for n in _nros) / _n)
        _ei.append(stats.expon.cdf(_s, scale = 1/a))
        _s += _a # incremento limite superior
        _d.append(abs(_ei[i] - _oi[i]))
    _dmax = max(_d)
    _vc = 1.36 / math.sqrt(_n)
    _r = _dmax < _vc
    g.bondadKS(_oi, _ei, 'exponencial')
    return _r

def chiNormal(_nros, _mu, _std):
    _n = len(_nros) # cantidad de elementos en la muestra
    _m =  15 # cantidad de intervalos
    _a = (max(_nros) - min(_nros)) / _m # amplitud intervalos
    _i = min(_nros) # limite inferior del intervalo
    _s = _i + _a # limite superior del intervalo
    _oi = [] # arreglo de frecuencias observadas
    _ei = [] # arreglo de frecuencias observadas
    _aux = 0 # acumulador para calcular el estadistico chi de la distribucion empírica
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n > _i and n <= _s for n in _nros))
        _pi = stats.norm.cdf(_s, _mu, _std) - stats.norm.cdf(_i, _mu, _std) # calculo probabilidad del intervalo
        _ei.append(_pi * (_n-1)) # agrego frecuencia esperada al arreglo
        _i += _a  # incremento el limite inferior
        _s += _a # incremento el limite superior
        _aux += (_oi[i] - _ei[i])**2 / _ei[i] # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1) # obtengo estadistico teórico chi de la tabla
    _r = _aux < _c # comparo estadístico empírico con teórico y lo asigno a una variable booleana
    g.bondadC(_oi, _ei, 'normal')
    return _r

def ksNormal(_nros, esp, std):
    _n = len(_nros)
    _m = math.trunc(math.sqrt(_n)) # cantidad de intervalos
    _a = (max(_nros) - min(_nros)) / _m # amplitud del intervalo
    _s = min(_nros) + _a # limite superior del intervalo
    _oi = [] # arreglo de F observadas
    _ei = [] # arreglo de F esperadas
    _d = [] # arreglo de estadisticos D
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n <= _s for n in _nros) / _n)
        _ei.append(stats.norm.cdf(_s, loc=esp, scale = std))
        _s += _a # incremento limite superior
        _d.append(abs(_ei[i] - _oi[i]))
    _dmax = max(_d)
    _vc = 1.36 / math.sqrt(_n)
    _r = _dmax < _vc
    g.bondadKS(_oi, _ei, 'normal')
    return _r

def chiBinomial(_nros, n, p):
    _n = len(_nros) # cantidad de elementos en la muestra
    _m = max(_nros) - min(_nros) + 1  # cantidad de valores
    _s = min(_nros) # valor puntual
    _oi = [] # arreglo de frecuencias observadas
    _ei = [] # arreglo de frecuencias esperadas
    _aux = 0 # acumulador para calcular el estadistico chi de la distribucion empírica
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n == _s for n in _nros))
        _pi= stats.binom.pmf(_s, n, p) # calculo probabilidad del valor 
        _ei.append(_pi * _n) # agrego frecuencia esperada al arreglo
        _s += 1 # incremento
        if(_ei[i] != 0):
            _aux += (_oi[i] - _ei[i])**2 / _ei[i] # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1) # obtengo estadistico teórico chi de la tabla
    _r = _aux < _c # comparo estadístico empírico con teórico y lo asigno a una variable booleana
    g.bondadC(_oi, _ei, 'binomial')
    return _r

def chiPoisson(_nros, p):
    _n = len(_nros) # cantidad de elementos en la muestra
    _m = max(_nros) - min(_nros) + 1 # cantidad de valores
    _s = min(_nros) # valor actual
    _oi = [] # arreglo de frecuencias observadas
    _ei = [] # arreglo de frecuencias esperadas
    _aux = 0 # acumulador para calcular el estadistico chi de la distribucion empírica
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n == _s for n in _nros))
        _pi= stats.poisson.pmf(_s, p) # calculo probabilidad del valor
        _ei.append(_pi * _n) # agrego frecuencia esperada al arreglo
        _s += 1 # incremento
        if (_ei[i] != 0):
            _aux += (_oi[i] - _ei[i])**2 / _ei[i] # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1) # obtengo estadistico teórico chi de la tabla
    _r = _aux < _c # comparo estadístico empírico con teórico y lo asigno a una variable booleana
    g.bondadC(_oi, _ei, 'poisson')
    return _r

def chiEmpirica(_nros, _p):
    _n = len(_nros) # cantidad de elementos en la muestra
    _m = max(_nros) - min(_nros) + 1 # cantidad de valores
    _s = min(_nros) # valor actual
    _oi = [] # arreglo de frecuencias observadas
    _ei = [] # arreglo de frecuencias esperadas
    _aux = 0 # acumulador para calcular el estadistico chi de la distribucion empírica
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n == _s for n in _nros))
        _ei.append(_p[i] * _n) # agrego frecuencia esperada al arreglo
        _s += 1 # incremento
        if (_ei[i] != 0):
            _aux += (_oi[i] - _ei[i])**2 / _ei[i] # incremento acumulador del estadístico 
    _c = stats.chi2.isf(0.05, _m-1) # obtengo estadistico teórico chi de la tabla
    _r = _aux < _c # comparo estadístico empírico con teórico y lo asigno a una variable booleana
    g.bondadC(_oi, _ei, 'empirica')
    return _r