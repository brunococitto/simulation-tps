import generador as g

class corrida:
    def __init__(self, marrvt, mservt, totcus, qlimit, reportes):
        # parámetros
        self.marrvt = marrvt # tiempo medio entre arribos
        self.mservt = mservt # tiempo medio de servicio
        self.totcus = totcus # clientes a atender
        self.qlimit = qlimit # limite de la cola
        self.tarrvl = [None] * qlimit # lista de tiempos de arribo
        # inivializar variables servidor
        self.time = 0 # reloj
        self.server = False # estado del servidor
        self.niq = 0 # cantidad de clientes en cola actualmente
        self.nis = 0 # cantidad de clientes en el sistema actualmente
        self.tlevent = self.time # tiempo del ultimo evento
        # inicializar contadores estadisticos
        self.numcus = 0 # clientes que se atendieron hasta el momento
        self.totdel = 0 # tiempo total en cola hasta el momento
        self.totsis = 0 # tiempo total en el sistema hasta el momento
        self.aniq = [] # area debajo de Q(t)
        self.autil = [] # area debajo de B(t)
        self.anis = [] # area debajo de S(t)
        # inicializar lista de eventos
        self.tna = self.time + g.exponencial(marrvt) # tiempo del proximo evento de llegada
        self.tnd = 1.0e30 # tiempo del proximo evento de partida
        self.next = 0 # tipo de evento próximo: 0 arribo / 1 partida
        # prob DoS
        self.denegados = 0 # clientes a los que se les denegó el servicio
        self.totalIn = 0 # total de clientes que ingresaron al sistema
        # historiales
        self.htime = [] # tiempo
        self.hutil = [] # uso del servidor
        self.hniq = [] # clientes en cola
        self.hnis = [] # clientes en el sistema
        self.hcps = [] # clientes promedio en el sistema
        self.hcpc = [] # clientes promedio en cola
        self.htps = [] # tiempo promedio en el sistema
        self.htpc = [] # tiempo promedio en cola
        self.hdng = [] # prob. denegación de servicio
        # mostrar reportes
        self.reportes = reportes
        self.ejecutar()

    def ejecutar(self):
        while (self.numcus < self.totcus):
            self.timing()
            self.uptavg()
            if (self.next == 0):
                self.arrive()
            else:
                self.depart()
        if (self.reportes):
            self.report()

    # rutina de tiempo
    def timing(self):
        _mintne = 1.0e29
        self.next = -1

        if (self.tna < _mintne):
            _mintne = self.tna
            self.next = 0
        if (self.tnd < _mintne):
            _mintne = self.tnd
            self.next = 1

        if (self.next == -1):
            print('Lista de eventos vacía en el tiempo:', self.time)
            exit()
        else:
            self.time = _mintne

    # rutina para actualizar estadisticos
    def uptavg(self):
        # calcular el tiempo desde el ultimo evento
        _tsle = self.time - self.tlevent
        # actualizar el tiempo del ultimo evento
        self.tlevent = self.time
        # actualizar el area debajo de Q(t)
        self.aniq.append(self.niq * _tsle)
        # actualizar el area debajo de B(t)
        self.autil.append(self.server * _tsle)
        # actualizar el area debajo de S(t)
        if (self.server):
            _nis = self.niq + 1
        else:
            _nis = self.niq
        self.anis.append((_nis * _tsle))
        # historiales
        self.htime.append(self.time) # tiempo
        self.hcps.append(self.avgnis()) # clientes promedio sistema
        self.hcpc.append(self.avgniq()) # clientes promedio cola
        self.htps.append(self.avgsis()) # tiempo sistema
        self.htpc.append(self.avgdel()) # tiempo cola
        self.hutil.append(sum(self.autil) / self.time * 100) # uso servidor
        self.hniq.append(self.niq) # clientes cola
        self.hdng.append(self.pDoS()) # prob DoS

    # rutina de arribo   
    def arrive(self):
        self.nis += 1 # clientes en el sistema
        self.hnis.append(self.nis) # historial de clientes en sistema
        self.totalIn += 1 # total de clientes que ingresaron al sistema
        self.tna = self.time + g.exponencial(self.marrvt)
        if (self.server):
            if (self.niq < self.qlimit):
                self.niq += 1
                self.tarrvl[self.niq-1] = self.time
            else:
                self.denegados += 1
        else:
            self.server = True
            _tiempoServicio = g.exponencial(self.mservt)
            self.tnd = self.time + _tiempoServicio
            self.totsis += _tiempoServicio
        
    # rutina de partida
    def depart(self):
        self.nis -= 1
        if (self.niq == 0):
            self.server = False
            self.tnd = 1.0e30
        else:
            self.niq -= 1
            _delay = self.time - self.tarrvl[0]
            self.totdel += _delay
            self.numcus += 1
            _tiempoServicio = g.exponencial(self.mservt)
            self.tnd = self.time + _tiempoServicio
            self.totsis += _delay + _tiempoServicio
            for i in range(self.niq):
               self.tarrvl[i] = self.tarrvl[i + 1]

    # rutina de reportes
    def report(self):
        print('Clientes promedio en el sistema:', self.avgnis(), 'clientes')
        print('Clientes promedio en cola:', self.avgniq(), 'clientes')
        print('Tiempo promedio en el sistema:', self.avgsis(), 'minutos')
        print('Tiempo promedio en cola:', self.avgdel(), 'minutos')
        print('Utilización del servidor:', self.util(), '%')
        print('Probabilidad de denegación de servicio:', self.pDoS()*100, '%')
        print('Tiempo de fin de simulación:', self.time, 'minutos')

    # métodos para calcular estadísticos
    def avgnis(self):
        _avgnis = sum(self.anis) / self.time
        return _avgnis

    def avgniq(self):
        _avgniq = sum(self.aniq) / self.time
        return _avgniq
 
    def avgsis(self):
        if (self.numcus > 0):
            _avgsis = self.totsis / self.numcus
        else:
            _avgsis = 0
        return _avgsis

    def avgdel(self):
        if (self.numcus > 0):
            _avgdel = self.totdel / self.numcus
        else:
            _avgdel = 0
        return _avgdel

    def util(self):
        _util = sum(self.autil) / self.time * 100
        return _util
    
    def pDoS(self):
        if (self.totalIn > 0):
            _pDoS = self.denegados / self.totalIn
        else:
            _pDoS = 0
        return _pDoS