from engine.scene  import Scene
from engine.sprite import Sprite
from engine.math import Rect
from engine.textrender import TextRender, TextAlign
from pygame.font import Font, SysFont
from pygame.surface import Surface
from pygame.locals import SRCALPHA
from pygame.mixer import Sound
import pygame.draw
import scenes

class ResultScene(Scene):
    def __init__(self, app, result):
        self.app = app
        self.result = result
        self.background = Sprite('resources/sky.png', size = (640, 480))
        self.start_icon = Sprite('resources/star.png', origin=(25, 25), size=(50, 50), position = (250, 210))
        self.font_btn    = Font('resources/msjh.ttf', 16)
        self.font_score  = SysFont('consolas', 32)
        self.font_title  = Font('resources/msjh.ttf', 32)
        self.text_render = TextRender()
        self.buttons     = [{
            'rect'    : Rect(210, 390, 100, 40),
            'text'    : '重新開始',
            'hover'   : False,
            'callback': lambda: self.app.switchScene(scenes.main.MainScene(self.app))
            }, {   
            'rect'    : Rect(330, 390, 100, 40),
            'text'    : '回到主畫面',
            'hover'   : False, 
            'callback': lambda: self.app.switchScene(scenes.menu.MenuScene(self.app))
        }]

        self.title = '遊戲結果'
        self.title_bg = Surface((240, 70), flags=SRCALPHA)
        pygame.draw.rect(self.title_bg, 'black', self.title_bg.get_rect(), 0, 4)
        self.title_bg.set_alpha(128)

        self.result_bg = Surface((240, 210), flags=SRCALPHA)
        pygame.draw.rect(self.result_bg, 'black', self.result_bg.get_rect(), 0, 4)
        self.result_bg.set_alpha(128)

        self.app.input.mouse.on_mouse_down.clear()
        self.app.input.mouse.on_mouse_down.append(self.onMouseDown)

        if pygame.mixer.get_init():
            self.ending_sound = Sound('resources/cheering.mp3')
            self.ending_sound.play()

    def update(self, clock):
        mouse = self.app.input.mouse

        topest_index = -1
        for i in range(len(self.buttons)):
            self.buttons[i]['hover'] = False
            if self.buttons[i]['rect'].collidepoint(mouse.mouse_position):
                topest_index = i

        if topest_index >= 0:
            self.buttons[topest_index]['hover'] = True

    def render(self, surface):
        self.background.render(surface)

        for btn in self.buttons:
            self.renderButton(surface, btn)

        # title
        surface.blit(self.title_bg, (200, 70))
        self.text_render.render(surface, self.font_title, self.title, (200, 70, self.title_bg.get_width(), self.title_bg.get_height()), 'white', TextAlign.MiddleCenter)

        surface.blit(self.result_bg, (200, 160))
        self.start_icon.render(surface)
        surface.blit(self.font_score.render('×{0}'.format(self.result['score']), True, 'white'), (280, 196))


    def onMouseDown(self, e):
        topest_btn = None

        for btn in self.buttons:
            if btn['rect'].collidepoint(e.pos):
                topest_btn = btn

        if topest_btn != None:
            topest_btn['callback']()

    def renderButton(self, surface, btn):
        pygame.draw.rect(surface, 'gray' if btn['hover'] else 'white', btn['rect'], 0, 4)
        self.text_render.render(surface, self.font_btn, btn['text'], btn['rect'], 'black', TextAlign.MiddleCenter)
        pygame.draw.rect(surface, 'black', btn['rect'], 2, 4)