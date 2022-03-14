import ruleta as r
import numpy as np

class corrida:
    def __init__(self, nT):
        self.nTiradas = nT
        self.resultados = np.random.randint(0, 37, nT)

    def fNum(self, nF):
        _f = np.round(np.count_nonzero(self.resultados == nF)/self.nTiradas, 4)
        return _f
    
    def evFNum(self, nF):
        _eF = []
        _aux = []
        for n in self.resultados:
            _aux.append(n)
            _eF.append(_aux.count(nF)/len(_aux))
        return _eF
    
    def media(self):
        _m = np.round(np.mean(self.resultados),4)
        return _m

    def evMedia(self):
        _eM = []
        _aux = []
        for n in self.resultados:
            _aux.append(n)
            _eM.append(np.mean(_aux))
        return _eM
    
    def std(self):
        _s = np.round(np.std(self.resultados), 4)
        return _s
    
    def evStd(self):
        _eS = []
        _aux = []
        for n in self.resultados:
            _aux.append(n)
            _eS.append(np.std(_aux))
        return _eS

    def var(self):
        _v = np.round(np.var(self.resultados),4)
        return _v
    
    def evVar(self):
        eV = []
        _aux = []
        for n in self.resultados:
            _aux.append(n)
            eV.append(np.var(_aux))
        return eV

