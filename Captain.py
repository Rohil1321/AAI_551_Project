#Author: Rishab Sharma
#Date: 02 Dec 2023
#Description: Captain Class
#             It is a sub class of Creature

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        # Calling superclass constructor with x, y coordinates and symbol "V"
        super().__init__(x, y, "Z")
        #Member Variable
        self._veggies_collected = []

    #Function to add a Veggie object to the list of collected veggies
    def addVeggie(self, veggie):
        self._veggies_collected.append(veggie)

    #Getter method for the collected veggies list
    def get_veggies_collected(self):
        return self._veggies_collected

    #Setter method for the collected veggies list
    def set_veggies_collected(self, veggies_collected):
        self._veggies_collected = veggies_collected

    #Getter/setter functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y