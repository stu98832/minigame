class GameApp:
    import pygame as native

    def __init__(self): 
        from engine.input import InputManager
        from engine.time  import Clock

        self.native.init()
        self.window  = self.native.display
        self.input   = InputManager(self)
        self.clock   = Clock()
        self.exiting = False

    def run(self):
        self.initialize()
        self.loop()
        self.quit()
        self.native.quit()

    def loop(self): 
        self.exiting = False
        loop_clock = self.native.time.Clock()
        while not self.exiting:
            if len(self.native.event.get(self.native.QUIT)) > 0:
                break

            self.clock.update()
            self.input.update()
            self.update(self.clock)
            self.render(self.window.get_surface())

            loop_clock.tick(60.0)    

    def initialize(self):
        self.clock.initialize()

    def update(self, clock):
        pass

    def render(self, surface):
        pass

    def quit(self):
        self.exiting = True