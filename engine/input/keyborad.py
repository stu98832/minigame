class Keyborad():
    def __init__(self):
        self.on_keydown = []
        self.on_keyup   = []
        self.key_state  = []
        self.focused = False
        self.key_mod = []

    def update(self):
        from pygame.locals import KEYDOWN, KEYUP
        import pygame.event
        
        self.key_state = pygame.key.get_pressed()
        self.key_mod   = pygame.key.get_mods()
        self.focused   = pygame.key.get_focused()
        
        for e in pygame.event.get([KEYDOWN, KEYUP]):
            if e.type == KEYDOWN:
                for callback in self.on_keydown:
                    callback(e)
            elif e.type == KEYUP:
                for callback in self.on_keyup:
                    callback(e)

    def is_pressed(self, key):
        return self.key_state[key]

    def check_mod(self, mod):
        return (self.key_mod & mod) > 0

