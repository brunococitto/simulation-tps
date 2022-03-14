import ruleta as r
import corrida as c
import graficar as g
import menu as m

# parámetros de ejecución
# cantidad de corridas a realizar
nCorridas = 5
# limite de la mesa fijo independiente del capital
apuestaMaxima = 10000
# opción para elegir si usar el menú o no
usarMenu = True
# RECORDAR: si no se usa el menú establecer los parámetros manualmente debajo!!!

# begin código
# declaro empty array para después cargarle las corridas
corridas = []
continuar = True
while (continuar):
    if (usarMenu):
        o = m.menu()
        # cargo lista con las corridas
        for n in range(nCorridas):  
            corridas.append(c.corrida(o['tApuesta'], o['valor'], o['apInicial'], o['mInicial'], o['estrategia'], o['capital'], apuestaMaxima))
    else:
        ##########
        # RECORDAR ESTABLECER PARÁMETROS SI NO SE USA MENÚ
        ##########
        # cantidad de tiradas a realizar por corrida
        # nTiradas != 0 significa capital infinito
        nTiradas = 1000
        # apuesta inicial que se realizará en cada corrida
        apuestaInicial = 250
        # monto inicial del cual se dispondrá en cada corrida
        montoInicial = 5000
        # tipo de apuesta a realizar
        # opciones: color, ubicacion, paridad, columna, docena, pleno
        tipo = 'docena'
        # valor
        # las opciones dependen del tipo de apuesta seleccionado arriba
        # opciones: negro, rojo, mayor, menor, par, impar, 1, 2, 3, nro entre 0 y 36
        valor = 2
        # estrategia
        estrategia = 'dalembert'
        # cargo lista con las corridas
        for n in range(nCorridas):
            corridas.append(c.corrida(tipo, valor, apuestaInicial, montoInicial, estrategia, nTiradas, apuestaMaxima))

    # muestro valores de salida
    for n in corridas:
        print('----------')
        print('Corrida', corridas.index(n)+1)
        print('Apuesta máxima:', max(n.ha))
        print('Frecuencia relativa final de la apuesta:', n.evFrApuesta()[-1])
        print('Monto retirada:', n.hmd[-1])
        print('Balance:', n.balanceRetirada())
        print('Tiradas hasta la primer victoria:', n.primerGanador())
        print('----------')

    # graficos
    # esta siempre
    g.evFr(corridas)
    # estas dependen de la cantidad de corridas
    if (len(corridas) > 1):
        g.montosDisponibles(corridas)
        g.tiradasHastaGanar(corridas)
        g.montoRetiradaPorCorrida(corridas)
        g.tortaBalance(corridas)
    else:
        g.amdt(corridas) # monto apostado y disponible por tiradas
    continuar = m.continuar()['continuar']