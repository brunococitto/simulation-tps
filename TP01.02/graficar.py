import matplotlib.pyplot as plt
import numpy as np

mostrar = True

# monto apostado y disponible por tiradas
def amdt(t):
    for n in t:
        plt.plot(n.hmd, label ='Caja', color = 'C' + str(t.index(n)))
        plt.plot(n.ha, label = 'Apuesta', color = 'C' + str(t.index(n) + 1))
    plt.plot(len(n.ha)-1, n.hmd[-1], color = 'C' + str(t.index(n)), marker = 'o')
    plt.axhline(t[0].hmd[0], color = 'k', label = 'Caja inicial')
    plt.axhline(t[0].ha[0], color = 'r', label = 'Apuesta inicial')
    plt.legend()
    plt.title('Flujo de caja y apuesta vs tiradas')
    plt.xlabel('Tiradas')
    plt.ylabel('Dinero en caja y a apostar')
    if (mostrar):
        plt.show()
    else:
        figure = plt.gcf()
        figure.set_size_inches(8, 7)
        plt.savefig( 'images/' +  str(len(t)) + 'C_' + t[0].e + '_' + t[0].tipo + '_' + t[0].c + '_amdt_' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
        plt.clf()

def tiradasHastaGanar(c):
    _aux = []
    for n in c:
        plt.bar(c.index(n),n.primerGanador())
        _aux.append(n.primerGanador())
    plt.axhline(np.mean(_aux), color = 'k', label = 'Media')
    plt.legend()
    plt.xticks(range(len(c)), range(1,len(c)+1))
    #plt.yticks(range(max(_aux)+1), range(0, max(_aux)+1))
    plt.title('Tiradas hasta ganar vs corridas')
    plt.xlabel("Corrida")
    plt.ylabel("Cantidad de tiradas hasta ganar")
    if (mostrar):
        plt.show()
    else:
        plt.savefig( 'images/' + str(len(c)) + 'C_' + c[0].e + '_' + c[0].tipo + '_' + c[0].c + '_thg_' + '.png', quality = 100, format = 'png', bbox_inches = 'tight')
        plt.clf()

def montoRetiradaPorCorrida(c):
    _aux = []
    for n in c:
        plt.bar(c.index(n), n.hmd[-1])
        _aux.append(n.hmd[-1])
    plt.axhline(np.mean(_aux), color = 'k', label = 'Media')
    plt.axhline(c[-1].hmd[0], color = 'r', label = 'Caja inicial')
    plt.legend()
    plt.xticks(range(len(c)), range(1,len(c)+1))
    plt.title('Caja retirada vs corridas')
    plt.xlabel("Corrida")
    plt.ylabel("Caja retirada")
    if (mostrar):
        plt.show()
    else:
        plt.savefig( 'images/' + str(len(c)) + 'C_' + c[0].e + '_' + c[0].tipo + '_' + c[0].c + '_mr_' + '.png', quality = 100, format = 'png', bbox_inches = 'tight')
        plt.clf()

def montosDisponibles(c):
    for n in c:
        plt.plot(n.hmd, color = 'C' + str(c.index(n)), label = ('C ' + str(c.index(n)+1)))
        plt.plot(len(n.ha)-1, n.hmd[-1], color = 'C' + str(c.index(n)), marker ='o')
    plt.axhline(c[-1].hmd[0], color = 'k', label = 'Caja Inicial')
    plt.legend()
    plt.title('Flujo de caja vs tiradas por corrida')
    plt.xlabel("Tiradas")
    plt.ylabel("Caja")
    if (mostrar):
        plt.show()
    else:
        figure = plt.gcf()
        figure.set_size_inches(10, 7)
        plt.savefig( 'images/' + str(len(c)) + 'C_' + c[0].e + '_' + c[0].tipo + '_' + c[0].c + '_md_' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
        plt.clf()

def tortaBalance(c):
    # primero armo lista con tres elementos:
    # posición 0 los que se fueron con un balance positivo (ganaron)
    # posición 1 los que se fueron con un balance negativo (perdieron)
    # posición 2 los que se fueron con balance = 0 (no perdieron ni ganaron)
    _aux = [0, 0, 0]
    _labels = ['Perdieron', 'Ganaron', 'Salieron derechos']
    for n in c:
        if (n.balanceRetirada() < 0):
            _aux[0] += 1
        if (n.balanceRetirada() > 0):
            _aux[1] += 1
        # este podria ser un  else, lo puse así para que sea más entendible al leerlo
        if (n.balanceRetirada() == 0):
            _aux[2] += 1
    # si no hay ganadores o nadie salio derecho los borro de las listas para no mostrarlos
    if (_aux[2] == 0):
        _aux.pop(2)
        _labels.pop(2)
    if (_aux[1] == 0):
        _aux.pop(1)
        _labels.pop(1)
    # una vez q tengo la lista procedo a graficar
    plt.pie(_aux, labels = _labels, autopct='%1.0f%%')
    plt.title('Porcentaje de ganadores y perdedores en ' + str(len(c)) + ' corridas')
    if (mostrar):
        plt.show()
    else:
        plt.savefig( 'images/' + str(len(c)) + 'C_' + c[0].e + '_' + c[0].tipo + '_' + c[0].c + '_torta_' +  '.png', quality = 100, format = 'png', bbox_inches = 'tight')
        plt.clf()

# evolución frecuencia relativa de la apuesta
def evFr(c):
    # seteo valor para la barra horizontal según el tipo de apuesta
    if (c[0].tipo == 'color' or c[0].tipo == 'ubicacion' or c[0].tipo == 'paridad'):
        _p = 18/37
    if (c[0].tipo == 'docena' or c[0].tipo == 'columna'):
        _p = 12/37
    if (c[0].tipo == 'pleno'):
        _p = 1/37
    for n in c:
        plt.plot(n.evFrApuesta(), color = 'C' + str(c.index(n)), label = 'C ' + str(c.index(n)+1))
        plt.plot(len(n.evFrApuesta())-1, n.evFrApuesta()[-1], color = 'C' + str(c.index(n)), marker = 'o')
    plt.axhline(_p, color = 'k', label = 'Frecuencia esperada')
    plt.legend()
    plt.title('Evolución de la frecuencia relativa de la apuesta en las tiradas')
    plt.xlabel('Tiradas')
    plt.ylabel('Frecuencia relativa de la apuesta')
    if (mostrar):
        plt.show()
    else:
        figure = plt.gcf()
        figure.set_size_inches(10, 7)
        plt.savefig( 'images/' + str(len(c)) + 'C_' + c[0].e + '_' + c[0].tipo + '_' + c[0].c + '_evFr_' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
        plt.clf()