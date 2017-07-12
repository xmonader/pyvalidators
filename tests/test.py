from validators.extensions.string import *
from validators.extensions.numeric import *


class Point:
    def __init__(self, x, y, name):
        self._x = x
        self._y = y
        self._name = name
    
    @Upper
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @ValidatingProperty
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val

    @Int
    def y(self):
        return self._x

    @y.setter
    def y(self, val):
        self._x = val


p  = Point(3, 4, "CIRCLE")

print(p)
p.x = "dmdm"
p.y = 9
p.name = "AHMED"
p.name = "ahmed"