import math
from scipy.stats import chi2
from scipy.stats import norm
import graficos as g

def chi(_nros):
    _n = len(_nros)
    _m = math.trunc(math.sqrt(_n)) # cantidad de intervalos
    _p = 1 / _m # tamaño de intervalo
    _oi = []
    _i = 0 # limite inferior del intervalo
    _s = _p # limite superior del intervalo
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n > _i and n <= _s for n in _nros))
        _i += _p # incremento el limite inferior
        _s += _p # incremento el limite superior
    _ei = _n / _m # cálculo del valor esperado (es igual para todos los intervalos)
    _aux = 0
    for i in _oi:
        _aux += (i - _ei)**2 / _ei
    _c = chi2.isf(0.05, _m-1)
    _r = _aux < _c
    g.bondadC(_oi, _ei)
    return _r

def ks(_nros):
    _n = len(_nros)
    _m = math.trunc(math.sqrt(_n)) # cantidad de intervalos
    _p = 1 / _m # tamaño de intervalo
    _oi = []
    _ei = []
    _s = _p # limite superior del intervalo
    for i in range(_m):
        # esto cuenta los elementos en ese intervalo
        # aprovecha la cuestion de que para python True = 1 y False = 0
        # entonces "suma" 0 y 1
        _oi.append(sum(n <= _s for n in _nros) / _n)
        _ei.append(_s)
        _s += _p # incremento el limite superior
    _d = []
    for i in range(_m):
        _d.append(abs(_ei[i] - _oi[i]))
    _dmax = max(_d)
    _vc = 1.36 / math.sqrt(_n)
    _r = _dmax < _vc
    g.bondadKS(_oi, _ei)
    return _r

def ks2(_nros): # acá se realiza el método de otra forma y se llega al mismo resultado
    _n = len(_nros)
    _nros.sort()
    _dmenos = []
    _dmas = []
    for i in range(1, _n + 1):
        _dmas.append(i / _n - _nros[i - 1])
        _dmenos.append(_nros[i - 1] - (i - 1) / _n)
    _d = max(max(_dmenos), max(_dmas))
    _vc = 1.36 / math.sqrt(_n)
    _r = _d < _vc
    return _r

def espera(_nros):
    _i = 0 # extremo inferior subintervalo, >= 0
    _s = 0.5 # extremo superior subintervalo, < 1
    _psi = _s - _i # calculo probabilidad del subintervalo
    # cálculo de posiciones donde hay números perteneciente al subintervalo seleccionado
    _pos = []
    for i in _nros:
        if (i >= _i and i < _s):
            _pos.append(True)
        else:
            _pos.append(False)
    # cálculo de la longitud de cada hueco
    _tesp = []
    _c = 0
    for i in _pos:
        if (i):
            _tesp.append(_c)
            _c = 0
        else:
            _c += 1
    _ch = max(_tesp) + 1 # cantidad de huecos
    if (_ch > 10):
        _ch = 10
    # cálculo de la frecuencia observada
    _fO = []
    for i in range(_ch):
        if (i == 9):
            _fO.append(sum(n >= 9 for n in _tesp))
        else:
            _fO.append(_tesp.count(i))
    # cálculo de la frecuencia esperada
    _fE = []
    for i in range(_ch):
        if (i == 9):
            _fE.append(sum(_fO) - sum(_fE))
        else:
            _fE.append((1 - _psi)**i * _psi * sum(_fO))
    # cálculo del estadístico
    _aux = 0
    for i in range(_ch):
        _aux += (_fO[i] - _fE[i])**2 / _fE[i]
    _r = _aux < chi2.isf(0.05, _ch - 1)
    g.espera(_fO, _fE)
    return _r

def subidas(_nros):
    _n = len(_nros) - 1
    _t = []
    _c = 1
    # auxiliar del while
    _aux = 0
    while (_aux < _n ):
        if (_nros[_aux] < _nros[_aux + 1]):
            _c += 1
        else:
            _t.append(_c)
            _c = 1
            _aux += 1
        _aux += 1
    if(_c > 1 or (_nros[-1] > _nros[-2])):
        _t.append(_c)
    _cr = max(_t) # cantidad de rachas
    # asigno límite de rachas porque puede haber infinintas en teoría
    if (_cr > 10):
        _cr = 10
    # cálculo de la frecuencia observada
    _fO = []
    for i in range(_cr):
        if (i == 9):
            _fO.append(sum(n >= 10 for n in _t))
        else:
            _fO.append(_t.count(i + 1))
    # cálculo de la frecuencia esperada
    _fE = []
    for i in range(_cr):
        if (i == _cr - 1):
            _fE.append(sum(_fO) / math.factorial(_cr))
        else:
            _fE.append(sum(_fO) * (i + 1) / math.factorial(i + 2))
    # cálculo del estadístico
    _aux = 0
    for i in range(_cr):
        _aux += (_fO[i] - _fE[i])**2 / _fE[i]
    _r = _aux < chi2.isf(0.05, _cr-1)
    g.subidas(_fO, _fE)
    return _r

def series(_nros):
    _n = len(_nros)
    # se hace en dos dimensiones
    _k = 2
    # pares a realizar
    _cp = len(_nros) / 2
    # intervalos o clases a realizar
    _ci = math.trunc(math.sqrt(_cp))
    # intrevalos o clases por dimension
    _cid = math.trunc(math.sqrt(_ci))
    # amplitud de cada intervalo (en cada dimension)
    _a = 1 / _cid
    # conversión lista en 1 dimension a duplas o parejas
    # esto podría no hacerse y continuar trabajando con la lista anterior
    _tuplas = []
    _i = 0
    while (_i < _n):
        _tuplas.append([_nros[_i], _nros[_i + 1]])
        _i += 2
    # cargo matriz con las frecuencias observadas
    _fO = []
    # acá manejo 2 intervalos
    _i1 = 0
    _i2 = 0
    _s1 = _a
    _s2 = _a
    for i in range(_cid):
        for j in range(_cid):
            _fO.append(sum((n[0] >= _i1 and n[0] <= _s1) and (n[1] >= _i2 and n[1] <= _s2)  for n in _tuplas))
            _s2 += _a
            _i2 += _a
        _i1 += _a
        _s1 += _a
        _i2 = 0
        _s2 = _a
    _fE = _cp / len(_fO)
    _aux = 0
    for i in _fO:
        _aux += (_fE - i)**2 / _fE
    _vc = chi2.isf(0.05, len(_fO) - 1)
    _r = _aux <= _vc
    g.series(_fO, _fE)
    return _r