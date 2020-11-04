from engine.sprite import Sprite
from engine.math import Vector2, DegToRad
import math

class Rock(Sprite):
    def __init__(self, scene, move_angle = 0.0, position = (0, 0), speed = 20.0):

        super().__init__('resources/rock.png', origin=(25, 25), position = position)
        self.scene = scene
        self.velocity = Vector2(math.cos(DegToRad(move_angle)), math.sin(DegToRad(move_angle))) * speed
        self.radius   = 25

    def update(self, clock):
        self.rotation += 150 * clock.elapsed
        self.position += self.velocity * clock.elapsed

    def isTouched(self, ship):
        dvec = self.position - ship.position
        
        if (dvec.length() <= (self.radius+ship.radius)): # ship radius + rock radius
            return True

        return False