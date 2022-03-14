import ruleta as r

class corrida:
    def __init__(self, typ, value, iniBet, iniAmount, estrategia, nT, maxBet):
        self.tipo = typ
        self.valor = value
        self.am = maxBet # apuesta máxima
        self.hmd = [iniAmount] # historial monto disponible
        self.ha = [iniBet] # historial monto apostado
        self.e = estrategia
        self.hg = [] # historial tiradas ganadoras
        if (nT == 0):
            self.c = 'fin'
            self.capFinito()
        else:
            self.c = 'infi'
            self.capInfinito(nT)

    def capFinito(self):
        _mD = self.hmd[0]
        _aA = self.ha[0]
        while (_mD >= _aA):
            _mD -= _aA
            _r = r.girar()
            if (r.gane(_r, self.tipo, self.valor)):
                _mD += _aA * r.coef(self.tipo)
                _aA = self.resetApuesta()
                self.hg.append(True)
            else:
                _aA = self.aumentarApuesta(_aA)
                self.hg.append(False)
            self.ha.append(_aA)
            self.hmd.append(_mD)

    def capInfinito(self, _nT):
        _mD = self.hmd[0]
        _aA = self.ha[0]
        for n in range(_nT):
            _mD -= _aA
            _r = r.girar()
            if (r.gane(_r, self.tipo, self.valor)):
                _mD += _aA * r.coef(self.tipo)
                _aA = self.resetApuesta()
                self.hg.append(True)
            else:
                _aA = self.aumentarApuesta(_aA)
                self.hg.append(False)
            self.ha.append(_aA)
            self.hmd.append(_mD)
    
    def primerGanador(self):
        for i in range(1,len(self.hmd)):
            if (i == len(self.hmd)-1):
                _p = 0
                return _p
            if (self.hmd[i-1] <= self.hmd[i]):
                _p = i
                return _p

    def balanceRetirada(self):
        _m = self.hmd[-1] - self.hmd[0]
        return _m

    def resetApuesta(self):
        if (self.e == 'martingala'):
            _a = self.ha[0]
        if (self.e == 'fibonacci'):
            if (len(self.ha) == 1):
                _a = self.ha[0]
            else:
                _a = self.ha[-2]
        if (self.e == 'dalembert'):
            if (self.ha[-1] <= self.ha[0]):
                _a = self.ha[0]
            else:
                _a = self.ha[-1] - self.ha[0]
        return _a
    
    def aumentarApuesta(self, _aA):
        if (self.e == 'martingala'):
            _aA *= 2
        if (self.e == 'fibonacci'):
            if (len(self.ha) != 1):
                _aA += self.ha[-2]
        if (self.e == 'dalembert'):
            _aA += self.ha[0]
        if (_aA > self.am):
            _aA = self.am
        return _aA
    
    def evFrApuesta(self):
        _evFr = []
        _aux = []
        for n in self.hg:
            _aux.append(n)
            _evFr.append(_aux.count(True)/len(_aux))
        return _evFr