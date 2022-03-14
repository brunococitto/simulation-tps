import random
import math

def exponencial(a):
    _u = random.random()
    _x = -(1/a) * math.log(_u)
    return _x