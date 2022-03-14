import random

def girar():
    _r = random.randint(0, 36)
    return _r

def color(n):
    if n == 0:
        _c = ''
        return _c
    if n == 10 or n == 28:
        _c = 'negro'
        return _c
    aux = int(n / 10) + (n % 10)
    if (aux % 2 == 0):
        _c = 'negro'
    else:
        _c = 'rojo'
    return _c

def paridad(n):
    if n == 0:
        _p = ''
        return _p
    if (n % 2 == 0):
        _p = 'par'
    else:
        _p = 'impar'
    return _p

def ubicacion(n):
    if n == 0:
        _u = ''
        return _u
    if (n <= 18):
        _u = 'menor'
    else:
        _u = 'mayor'
    return _u

def columna(n):
    if (n == 0):
        _c = ''
        return _c
    if (n % 3 == 0):
        _c = 3
        return _c
    _col1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    if (n in _col1):
        _c = 1
    else:
        _c = 2
    return _c

def docena(n):
    if (n == 0):
        _d = 0
        return _d
    if (n >= 1 and n <= 12):
        _d = 1
        return _d
    if (n >= 13 and n <= 24):
        _d = 2
    else:
        _d = 3
    return _d

def gane(r, t, v):
    #default
    _r = r
    if (t == 'color'):
        _r = color(r)
    if (t == 'paridad'):
        _r = paridad(r)
    if (t == 'ubicacion'):
        _r = ubicacion(r)
    if (t == 'columna'):
        _r = columna(r)
    if (t == 'docena'):
        _r = docena(r)
    if (v == _r):
        return True
    else:
        return False

def coef(t):
    if (t == 'color' or t == 'paridad' or t == 'ubicacion'):
        _c = 2
    if (t == 'columna' or t == 'docena'):
        _c = 3
    if (t == 'pleno'):
        _c = 36
    return _c