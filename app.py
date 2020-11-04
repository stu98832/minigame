from engine import GameApp
import pygame.mixer
import scenes
import app

class MiniGame(GameApp):
    def initialize(self):
        super().initialize()
        if pygame.mixer.get_init():
            pygame.mixer.music.load('resources/bgm-trap-music.mp3')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(True)
        self.window.set_caption('MiniGame')
        self.window.set_mode((640, 480))
        self.scene = scenes.menu.MenuScene(self)
        self.nextscene = None

    def update(self, clock):
        if (self.nextscene != None):
            self.scene = self.nextscene
            self.nextscene = None

        self.scene.update(clock)

    def render(self, surface):
        self.scene.render(surface)
        self.window.flip()

    def switchScene(self, scene):
        self.nextscene = scene

if __name__ == '__main__':
    app = MiniGame()
    app.run()