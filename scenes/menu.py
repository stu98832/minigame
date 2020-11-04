from engine.scene  import Scene
from engine.sprite import Sprite
from engine.math import Rect
from engine.textrender import TextRender, TextAlign
from pygame.font import Font
from pygame.surface import Surface
from pygame.locals import SRCALPHA
import pygame.draw
import scenes

class MenuScene(Scene):
    def __init__(self, app):
        self.app = app
        self.background = Sprite('resources/sky.png', size = (640, 480))
        self.font_btn    = Font('resources/msjh.ttf', 16)
        self.font_title  = Font('resources/msjh.ttf', 32)
        self.text_render = TextRender()
        self.buttons     = [{
            'rect'    : Rect(270, 330, 100, 30),
            'text'    : '開始遊戲',
            'hover'   : False,
            'callback': lambda: self.app.switchScene(scenes.main.MainScene(self.app))
            },{
            'rect'    : Rect(270, 370, 100, 30),
            'text'    : '遊戲說明',
            'hover'   : False,
            'callback': self.onToggleHelp
            }, {   
            'rect'    : Rect(270, 410, 100, 30),
            'text'    : '離開',
            'hover'   : False, 
            'callback': self.app.quit
        }]

        self.title = '飛船撿星星'
        self.title_bg = Surface((640, 60), flags=SRCALPHA)
        pygame.draw.rect(self.title_bg, 'black', self.title_bg.get_rect())
        self.title_bg.set_alpha(128)

        self.help = '''
    一個飛行員在空中盤旋，請盡可能的蒐集星星並躲避隕石!

    遊戲方法：
    上：向前
    下：向後
    左：往左轉
    左：往右轉
'''
        self.help_bg = Surface((480, 220), flags=SRCALPHA)
        pygame.draw.rect(self.help_bg, 'black', self.help_bg.get_rect(), 0, 4)
        self.help_bg.set_alpha(128)

        self.app.input.mouse.on_mouse_down.clear()
        self.app.input.mouse.on_mouse_down.append(self.onMouseDown)
        self.show_help = False

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
        surface.blit(self.title_bg, (0, 0))
        self.text_render.render(surface, self.font_title, self.title, (0, 0, self.title_bg.get_width(), self.title_bg.get_height()), 'white', TextAlign.MiddleCenter)

        if self.show_help:
            surface.blit(self.help_bg, (80, 80))
            self.text_render.render(surface, self.font_btn, self.help, (80, 80, self.help_bg.get_width(), self.help_bg.get_height()), 'white', TextAlign.LeftCenter)

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

    def onToggleHelp(self):
        self.show_help = not self.show_help
