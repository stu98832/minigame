from engine.scene  import Scene
from engine.sprite import Sprite
from engine.time import Timer
from engine.math import Vector2
from pygame.font import SysFont
from pygame.surface import Surface
from pygame.locals import SRCALPHA
from pygame.mixer import Sound
import pygame.draw 
import objects
import scenes
import random

class MainScene(Scene):
    def __init__(self, app):
        self.app        = app
        self.background = Sprite('resources/sky.png', size = (640, 480))
        self.ship       = objects.ship.Ship(self)
        self.star       = objects.star.Star(self)
        self.start_icon = Sprite('resources/star.png', origin=(25, 25), size=(25, 25), position = (30, 30))
        self.ship.position.update(320, 240)
        self.font_score = SysFont('consolas', 16)
        self.rocks      = []
        self.gameover   = False
        self.result     = {
            'score': 0
        }
        self.result_bg = Surface((100, 35), flags=SRCALPHA)
        pygame.draw.rect(self.result_bg, 'black', self.result_bg.get_rect(), 0, 4)
        self.result_bg.set_alpha(128)

        self.rock_timer = Timer(
            active=True,
            loop = True,
            delay = 3,
            callback=self.genRock
        )

        self.star_timer = Timer(
            delay = 5,
            callback = self.genStar
        )

        if pygame.mixer.get_init():
            self.start_hit_sound = Sound('resources/beep.ogg')

        self.genStar()

    def update(self, clock):
        self.star_timer.update(clock)
        self.rock_timer.update(clock)
        self.ship.update(clock)
        self.star.update(clock)
        for rock in self.rocks:
            rock.update(clock)

        if not self.gameover:
            self.removeOutsideRock()

            if self.ship.position.x < 0:
                self.ship.position.x = 0
                self.ship.speed = 0
            if self.ship.position.x > 640:
                self.ship.position.x = 640
                self.ship.speed = 0
            if self.ship.position.y < 0:
                self.ship.position.y = 0
                self.ship.speed = 0
            if self.ship.position.y > 480:
                self.ship.position.y = 480
                self.ship.speed = 0

            for rock in self.rocks:
                if rock.isTouched(self.ship):
                    self.app.switchScene(scenes.result.ResultScene(self.app, self.result))
                    return

            if self.star.isTouched(self.ship):
                self.result['score'] += 1
                self.star.hide()
                self.star_timer.start()
                
                if pygame.mixer.get_init():
                    self.start_hit_sound.play()

                if self.result['score'] % 5 == 0:
                    self.rock_timer.stop()
                    self.rock_timer.delay -= 0.1
                    self.rock_timer.start()

        

    def render(self, surface):
        self.background.render(surface)
        self.ship.render(surface)
        self.star.render(surface)

        for rock in self.rocks:
            rock.render(surface)

        # score UI
        surface.blit(self.result_bg, (10, 12))
        self.start_icon.render(surface)
        surface.blit(self.font_score .render(str(self.result['score']), True, 'yellow'), (50, 22))

    def genStar(self):
        self.star.show((30 + 580 * random.random(), 30 + 420 * random.random()))

    def genRock(self):
        direction = random.randint(0, 3)
        position = Vector2(
            600 * random.random() if direction % 2 == 0 else -25 if direction == 1 else 665,
            400 * random.random() if direction % 2 == 1 else -25 if direction == 0 else 505)
        dp = self.ship.position + (-50 + 100*random.random(), -50 + 100*random.random()) - position
        angle = Vector2().angle_to(dp)
        speed = 50 + (100 if random.random() <= 0.3 else 0)
        rock  = objects.rock.Rock(self, 
            move_angle = angle, 
            position   = position,
            speed = speed)
        self.rocks.append(rock)

    def removeOutsideRock(self):
        remove_array = []
        for rock in self.rocks:
            if rock.velocity.x < 0 and rock.position.x < -25 or \
               rock.velocity.x > 0 and rock.position.x > 665 or \
               rock.velocity.y < 0 and rock.position.y < -25 or \
               rock.velocity.y > 0 and rock.position.y > 505:
                remove_array.append(rock)

        for item in remove_array:
            self.rocks.remove(item)
