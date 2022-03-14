import matplotlib.pyplot as plt

guardarGraficos = False
mostrarGraficos = True

colores = [
    'crimson',
    'gold',
    'yellowGreen',
    'dodgerBlue',
    'mediumvioletRed',
    'coral',
    'limeGreen',
    'slateGray',
    'darkMagenta',
    'orange'
]

def clientesSistema(c, pArribos):
    for n in c:
        plt.plot(n.htime, n.hcps, label = 'Corrida ' + str(c.index(n)+1), color = colores[c.index(n)])
    plt.title('Clientes promedio en el sistema')
    plt.ylabel('Clientes')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-cps-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def clientesCola(c, pArribos):
    for n in c:
        plt.plot(n.htime, n.hcpc, label = 'Corrida ' + str(c.index(n)+1), color = colores[c.index(n)])
    plt.title('Clientes promedio en cola')
    plt.ylabel('Clientes')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-cpc-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def tiempoSistema(c, pArribos):
    for n in c:
        plt.plot(n.htime, n.htps, label = 'Corrida ' + str(c.index(n)+1), color = colores[c.index(n)])
    plt.title('Tiempo promedio en el sistema')
    plt.ylabel('Tiempo')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-tps-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def tiempoCola(c, pArribos):
    for n in c:
        plt.plot(n.htime, n.htpc, label = 'Corrida ' + str(c.index(n)+1), color = colores[c.index(n)])
    plt.title('Tiempo promedio en cola')
    plt.ylabel('Tiempo')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-tpc-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def usoServer(c, pArribos):
    for n in c:
        plt.plot(n.htime, n.hutil, label = 'Corrida ' + str(c.index(n)+1), color = colores[c.index(n)])
    plt.title('Uso del servidor')
    plt.ylabel('%')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-uds-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def probClientes(c, pArribos):
    for i in c:
        _aux = []
        for j in range(max(i.hnis)):
            _p = i.hnis.count(j+1)/len(i.hnis)
            _aux.append(_p)
        plt.plot(range(max(i.hnis)), _aux, label = 'Corrida ' + str(c.index(i) + 1), color = colores[c.index(i)], marker = '.')
    plt.title('Probabilidad de n clientes en el sistema')
    plt.ylabel('Probabilidad')
    plt.xlabel('Clientes')
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-pnc-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()

def pDoS(c, pArribos, qlimit):
    for i in c:
        plt.plot(i.htime, i.hdng, label = 'Corrida ' + str(c.index(i) + 1), color = colores[c.index(i)])
    plt.title('Probabilidad de denegación de servicio')
    plt.ylabel('Probabilidad')
    plt.xlabel('Tiempo')
    plt.grid()
    plt.legend(ncol = 2)
    if(guardarGraficos):
        plt.savefig( 'images/py-pdos-' + str(qlimit) + '-' + str(pArribos) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if(mostrarGraficos):
        plt.show()
    plt.clf()