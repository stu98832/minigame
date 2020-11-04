from engine.sprite import Sprite
from engine.math import Vector2, DegToRad
import math

class Star(Sprite):
    def __init__(self, scene):

        super().__init__('resources/star.png', origin=(25, 25), enable = False, visible = False)
        self.scene = scene
        self.radius   = 25

    def isTouched(self, ship):
        if not self.enable or not ship.enable:
            return False

        dvec = self.position - ship.position
        
        if (dvec.length() <= (self.radius+ship.radius)): # ship radius + rock radius
            return True

        return False

    def hide(self):
        self.enable = False
        self.visible = False

    def show(self, position):
        self.position.update(position)
        self.enable = True
        self.visible = True
