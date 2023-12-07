# Author: Romil Vimalbhai Shah
# Date: 06 Dec 2023
# Description: Veggie Class
#              This is a subclass of Creature

from Creature import Creature
import random

class Snake(Creature):

  def __init__(self, x, y):
    super().__init__(x, y, 'S')