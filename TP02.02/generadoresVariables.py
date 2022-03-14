import random
import math

def uniforme(a, b, cantidad):
    _valores = []
    for i in range(cantidad):
        _u = random.random()
        _x = a + (b - a) * _u
        _valores.append(_x)
    return _valores

def exponencial(a, cantidad):
    _valores = []
    for i in range(cantidad):
        _u = random.random()
        _x = -(1/a) * math.log(_u)
        _valores.append(_x)
    return _valores

def gamma(k, a, cantidad):
    _valores = []
    for i in range(cantidad):
        _tr = 1
        for j in range(k):
            _u = random.random()
            _tr *= _u
        _x = -(1/a) * math.log(_tr)
        _valores.append(_x)
    return _valores

def normal(k, e, std, cantidad):
    _valores = []
    for i in range(cantidad):
        _sum = 0
        for j in range(k):
            _u = random.random()
            _sum += _u
        _x = std * math.sqrt(12/k) * (_sum - k/2) + e
        _valores.append(_x)
    return _valores

def binomNegativa(k, q, cantidad):
    _valores = []
    _qr = math.log(q)
    for i in range(cantidad):
        _tr = 1
        for j in range(k):
            _u = random.random()
            _tr *= _u
        _x = math.log(_tr)/_qr
        _valores.append(round(_x))
    return _valores

def binomial(n, p, cantidad):
    _valores = []
    for i in range(cantidad):
        _x = 0
        for j in range(n):
            _u = random.random()
            if(_u < p):
                _x += 1
        _valores.append(_x)
    return _valores

def hipergeometrica(N, n, p, cantidad):
    _valores = []
    _Nb = N # hago backup del parámetro
    _pb = p # hago backup del parámetro
    for i in range(cantidad):
        _x = 0
        N = _Nb # reasigno el parámetro
        p = _pb # reasigno el parámetro
        for j in range(n):
            _u = random.random()
            if(_u < p):
                _s = 1
                _x += 1
            else:
                _s = 0
            p = (N*p - _s)/(N-1)
            N -= 1
        _valores.append(_x)
    return _valores

def poisson(p, cantidad):
    _valores = []
    for i in range(cantidad):
        _x = 0
        _tr = 1
        _b = math.e**(-p)
        _u = random.random()
        _tr *= _u
        while(_tr > _b):
            _x += 1
            _u = random.random()
            _tr *= _u
        _valores.append(_x)
    return _valores

def empiricaD(cantidad, _p):
    _valores = []
    for i in range(cantidad):
        _u = random.random()
        _F = 0
        _i = 0
        while(_u > _F and _u > _p[0]):
            _F += _p[_i]
            _i += 1
        if (_i == 0):
            _valores.append(_i)
        else:
            _valores.append(_i - 1)
    return _valores
