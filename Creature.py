#Author: Rishab Sharma
#Date: 02 Dec 2023
#Description: Creature Class
#             It is a sub class of Field Inhabitant and it has its own sub classes, Captain and Rabbit

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, field_inhabitant):
        super().__init__(field_inhabitant)
        self._x = x
        self._y = y

    #Getter/Setter Functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y