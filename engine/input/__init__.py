class InputManager():
    def __init__(self, app):
        from engine.input.keyborad import Keyborad
        from engine.input.mouse import Mouse
        
        self.app = app
        self.keyborad = Keyborad()
        self.mouse = Mouse()

    def update(self):
        self.keyborad.update()
        self.mouse.update()
