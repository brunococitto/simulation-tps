#ParteMediaDelCuadrado
def mediacuad(_s):
    _nros = []
    while _s not in _nros:
        _nros.append(_s)
        _s = int(str(_s * _s).zfill(8)[2:6])
    #transformarlos a [0,1)
    for i in range(len(_nros)):
        _nros[i] = _nros[i] / max(_nros)
    return _nros

#Rand
def rand(_s, _i):
    _a = 7**5
    _m = 2**31 - 1
    _nros_u = [_s / _m]
    for i in range(_i - 1):
        _s = _a * _s % _m
        _nros_u.append(_s / _m)
    return _nros_u

#RandU
def randu(_s, _i):
    _a = 2**16
    _c = 3
    _m = 2**31
    _nros_u = [_s / _m]
    for i in range(_i - 1):
        _s = (_a + _c) * _s % _m
        _nros_u.append(_s / _m)
    return _nros_u

#GCL
def gcl(_i, _m, _a, _c, _s):
    _nros_u = [_s / _m]
    for i in range(_i - 1):
        _s = (_a * _s + _c) % _m
        _nros_u.append(_s / _m)
    return _nros_u

#debajo se encuentra comentaddo el código utilizado para solicitar la generacion de números al sitio random.org
#eliminé la key de mi cuenta personal por obvias razones
# from randomapi import RandomJSONRPC
# random_client = RandomJSONRPC('KEY')
# r = random_client.generate_decimal_fractions(5000, 10)
# with open("rdonumbers.txt", 'w') as file:
#     file.write(str(r))