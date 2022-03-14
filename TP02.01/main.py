import generadores as g
import pruebas as p
import graficos as gr
import random

seed = 1234 # semilla inicial
n = 5000 # cantidad de números a generar
# para GLC hay que agregar estos de abajo
m = 2**64 # módulo > 0
a = 29889745643 # multiplicador >= 0 < m
c = 15 # incremento <= m
gen = 'ms' # generador a utilizar (ms, rand, randu, gcl, py, rdotorg)

# acá armo un arreglo según un generador seleccionado
# es el que luego se envía como parámetro a las pruebas o gráficas
if (gen == 'ms'):
    _nros = g.mediacuad(seed)
if (gen == 'rand'):
    _nros = g.rand(seed, n)
if (gen == 'randu'):
    _nros = g.randu(seed, n)
if (gen == 'gcl'):
    _nros = g.gcl(n, m, a, c, seed)
if (gen == 'py'):
    _nros = []
    for i in range(n):
        _nros.append(random.random())
if (gen == 'rdotorg'):
    #los valores del archivo se pidieron una vez a random mediante la api
    #el código se encuentra comentado al final del archivo generadores.py
    _nros = []
    with open("rdonumbers.txt", 'r') as file:
        _aux = eval(file.readline())
    for i in _aux:
        _nros.append(float(i))

#gráfrica de los números generados
gr.nros(_nros)
#gráfica de la correlación lineal de números generados
gr.nrosCorrelacion(_nros)
#prueba de bondad y ajuste chi cuadrado
print('Pruebas de uniformidad')
print('Prueba de Chi-Cuadrado:', p.chi(_nros))
#prueba de bondad y ajuste Kolmorogov-Smirnov
print('Prueba de Kolmogorov-Smirnov:', p.ks(_nros))
print('Pruebas de independencia')
#prueba de espera o huecos
print('Prueba de huecos:', p.espera(_nros))
#prueba de subidas, rachas o corridas
print('Prueba de rachas:', p.subidas(_nros))
#prueba de series
print('Prueba de series:', p.series(_nros))