import matplotlib.pyplot as plt

#acá abajo poner el nombre del generador actualmente usado
#lo había hecho para que lo levante solo pero me parecia ineficiente
#el hecho de crear una clase y todo solamente para una variable
gen = 'null'
#acá abajo poner True si se quieren mostrar los gráficos o False si se quieren guardar automáticamente
#el nombre se codifica de la siguiente manera: generador_nombreGrafico.png
#se guarda en la carpeta raiz/images
mostrar = True

def nros(_n):
    plt.plot(_n, 'bo', alpha = 0.5)
    plt.title('Números generados')
    plt.ylabel('Valor')
    plt.xlabel('Número')
    plt.savefig( 'images/' +  gen + '_nros' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def nrosCorrelacion(_n):
    plt.plot(_n, _n, 'go', alpha = 0.5)
    plt.title('Correlación lineal entre números generados')
    plt.ylabel('Número')
    plt.xlabel('Número')
    plt.savefig( 'images/' +  gen + '_nrosCorrelacion' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def bondadKS(_o, _e):
    plt.plot(_o, 'bo', label = 'Observado')
    plt.plot(_e, 'ro', label = 'Esperado')
    plt.title('Prueba de bondad y ajuste Kolmogorov-Smirnov')
    plt.xlabel('Clase')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.savefig( 'images/' +  gen + '_bondadKS' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def bondadC(_n, _e):
    _a = []
    for i in _n:
        _a.append(i / sum(_n))
    plt.plot(_a, 'bo', label = "Observado")
    plt.axhline(_e/sum(_n), color = 'r', label = 'F. Esperada')
    plt.ylim(0, 3 * 1 / len(_n))
    plt.title('Prueba de bondad y ajuste Chi-Cuadrado')
    plt.xlabel('Intervalo')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.savefig( 'images/' +  gen + '_bondadC' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def espera(_o, _e):
    plt.bar(range(len(_o)), _o, label = 'Observado')
    plt.bar(range(len(_e)), _e, color = 'y', alpha = 0.6, label = 'Esperado')
    plt.title('Prueba de esperas')
    plt.xlabel('Longitud de hueco')
    plt.ylabel('Cantidad de ocurrencias')
    plt.legend()
    plt.savefig( 'images/' +  gen + '_espera' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def subidas(_o, _e):
    plt.bar(range(len(_o)), _o, label = 'Observado')
    plt.bar(range(len(_e)), _e, color = 'y', alpha = 0.6, label = 'Esperado')
    plt.title('Prueba de subidas')
    plt.xlabel('Longitud de racha')
    plt.ylabel('Cantidad de ocurrencias')
    #calculo y asigno las labels del eje x para omitir el 0
    _xt = []
    for i in range(len(_o)):
        _xt.append(i + 1)
    plt.xticks(range(len(_o)), _xt)
    plt.legend()
    plt.savefig( 'images/' +  gen + '_subidas' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()

def series(_n, _e):
    _a = []
    for i in _n:
        _a.append(i / sum(_n))
    plt.plot(_a, 'bo', label = "Observado")
    plt.axhline(_e/sum(_n), color = 'r', label = 'F. Esperada')
    plt.ylim(min(_a) - 0.1, max(_a) + 0.1)
    plt.title('Prueba de series')
    plt.xlabel('Intervalo')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.savefig( 'images/' +  gen + '_series' + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    if (mostrar):
        plt.show()
    else:
        plt.clf()
    