class Mouse():
    def __init__(self):
        from engine.math import Vector2

        self.on_mouse_down = []
        self.on_mouse_up = []
        self.on_mouse_move = []
        self.on_wheel_move = []
        self.focused = False
        self.mouse_state = []
        self.mouse_position = Vector2(0, 0)

    def update(self):
        from engine.math import Vector2
        from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL
        import pygame.mouse

        self.mouse_state    = pygame.mouse.get_pressed()
        self.mouse_position = Vector2(pygame.mouse.get_pos())
        self.focused        = pygame.mouse.get_focused()

        for e in pygame.event.get([MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL]):
            if e.type == MOUSEBUTTONDOWN:
                for callback in self.on_mouse_down:
                    callback(e)
            elif e.type == MOUSEBUTTONUP:
                for callback in self.on_mouse_up:
                    callback(e)
            elif e.type == MOUSEMOTION:
                for callback in self.on_mouse_move:
                    callback(e)
            elif e.type == MOUSEWHEEL:
                for callback in self.on_wheel_move:
                    callback(e)

    def pressed(self, btn):
        return self.mouse_state[btn] if btn in self.mouse_state else False