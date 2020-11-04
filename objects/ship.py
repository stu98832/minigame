from engine.sprite import Sprite
from engine.math import Vector2, DegToRad
import math
import app

class Ship(Sprite):
    SPEED_LIMIT = 350.0

    def __init__(self, scene):

        super().__init__('resources/spaceship.png', origin=(128, 128), size = (64, 64))
        self.scene    = scene
        self.speed    = 0
        self.velocity = Vector2(0, 0)
        self.radius   = 16

    def update(self, clock):
        import engine.input.keys as keys

        self.position += self.velocity * clock.elapsed
        
        keyborad = self.scene.app.input.keyborad
        if keyborad.is_pressed(keys.K_UP):
            self.speed += 200 * clock.elapsed
        if keyborad.is_pressed(keys.K_DOWN):
            self.speed -= 200 * clock.elapsed
        if keyborad.is_pressed(keys.K_RIGHT):
            self.rotation += 150 * clock.elapsed
        if keyborad.is_pressed(keys.K_LEFT):
            self.rotation -= 150 * clock.elapsed

        self.velocity.x = self.speed * math.cos(DegToRad(self.rotation))
        self.velocity.y = self.speed * math.sin(DegToRad(self.rotation))

        if abs(self.speed) > self.SPEED_LIMIT:
            self.speed = -self.SPEED_LIMIT if self.speed < 0 else self.SPEED_LIMIT

