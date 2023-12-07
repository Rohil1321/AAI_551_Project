#Author: Romil Vimalbhai Shah
#Date: 02 Dec 2023
#Description: Veggie Class
#             It is a sub class of Field Inhabitant

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, field_inhabitant, points):
        super().__init__(field_inhabitant)
        self._name = name
        self._points = points

    # String function to print the Symbol, Name and Points
    def __str__(self):
        return f"Symbol: {self.setFieldInhabitant()}, Name: {self._name}, Points: {self._points}"

    # Getter/setter functions for name and points
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points