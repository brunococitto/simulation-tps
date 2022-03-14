import corrida as c
import graficas as g

def promDeProm(c):
    print('----------')
    print('Promedios de estadísticos para', len(c), 'corridas')
    print('----------')
    _aux = 0
    for i in c:
        _aux += i.avgnis()
    _aux = _aux / len(c)
    print('Clientes promedio en el sistema:', _aux, 'clientes')
    _aux = 0
    for i in c:
        _aux += i.avgniq()
    _aux = _aux / len(c)
    print('Clientes promedio en cola:', _aux, 'clientes')
    _aux = 0
    for i in c:
        _aux += i.avgsis()
    _aux = _aux / len(c)
    print('Tiempo promedio en el sistema:', _aux, 'minutos')
    _aux = 0
    for i in c:
        _aux += i.avgdel()
    _aux = _aux / len(c)
    print('Tiempo promedio en cola:', _aux, 'minutos')
    _aux = 0
    for i in c:
        _aux += i.util()
    _aux = _aux / len(c)
    print('Utilización del servidor:', _aux, '%')
    _aux = 0
    for i in c:
        _aux += i.time
    _aux = _aux / len(c)
    print('Tiempo de simulación:', _aux, 'minutos')
    _aux = 0
    for i in c:
        _aux += i.pDoS()
    _aux = _aux / len(c)
    print('Probabilidad de denegación de servicio:', _aux*100, '%')

# parámetros de ejecución
nCorridas = 10 # cantidad de corridas a realizar
tServicio = 30 # tasa de servicio
pArribos = 75 # porcentaje de la tasa de servicios
tArribos =  pArribos / 100 * tServicio # tasa de arribos
totcus = 500 # total de clientes
qlimit = 2 # tamaño de la cola
reportes = False # mostrar reportes por cada corrida

print('Sistema de colas de un servidor - MM1')
print('Tiempo medio entre arribos:', 1/tServicio, 'minutos')
print('Tiempo medio de servicio:', 1/tArribos, 'minutos')
print('Número de clientes:', totcus)

corridas = []

for i in range(nCorridas):
    if (reportes):
        print('----------')
        print('Corrida', i+1)
    corridas.append(c.corrida(tArribos, tServicio, totcus, qlimit, reportes))

# Promedios de los estadísticos para todas las corridas
promDeProm(corridas)

# Gráficas
# g.clientesSistema(corridas, pArribos)
# g.clientesCola(corridas, pArribos)
# g.tiempoSistema(corridas, pArribos)
# g.tiempoCola(corridas, pArribos)
# g.usoServer(corridas, pArribos)
# g.probClientes(corridas, pArribos)
# g.pDoS(corridas, pArribos, qlimit)