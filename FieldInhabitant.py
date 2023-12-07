#Author: Romil Vimalbhai Shah
#Date: 02 Dec 2023
#Description: Field Inhabitant Class
#             This is the first super class, it has creature and veggie as it sub classes.
class FieldInhabitant:

    def __init__(self, field_inhabitant):
        # Member variable representing the text symbol for the inhabitant
        self._field_inhabitant = field_inhabitant

    #Getter method for veggie symbol
    def set_symbol(self, field_inhabitant):
        self._field_inhabitant = field_inhabitant

    #Setter method for the collected veggies list
    def get_symbol(self):
        return "\033[1m" + str(self._field_inhabitant) + "\033[0m"
