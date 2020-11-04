class Sprite:
    def __init__(self, image, 
            position = (0, 0),
            origin   = (0, 0),
            rotation = 0.0,
            size     = None,
            scale    = None,
            alpha    = 1.0,
            visible  = True,
            enable   = True
        ):
        import pygame.image
        from engine.math import Vector2

        self.image = pygame.image.load(image)
        self.position = Vector2(position)
        self.origin = Vector2(origin)
        self.rotation = rotation
        self.size     = Vector2(self.image.get_size())
        self.alpha    = alpha
        self.scale    = Vector2((1.0, 1.0) if scale == None and size == None else scale if size == None else (size[0] / self.size.x, size[1] / self.size.y))
        self.visible  = visible
        self.enable   = enable

    def update(self, clock):
        if not self.enable:
            return

    def render(self, surface):
        if not self.visible:
            return

        import pygame.transform as transform
        from engine.math import Vector2

        scaled   = transform.scale(self.image, (int(self.size.x*self.scale.x), int(self.size.y*self.scale.y)))
        rotated  = transform.rotate(scaled, -self.rotation)
        org_cent = scaled.get_rect().center
        new_cent = rotated.get_rect().center
        old_origin = Vector2(self.origin.x*self.scale.x, self.origin.y*self.scale.y)
        new_origin = (old_origin - org_cent).rotate(self.rotation) + new_cent

        rotated.set_alpha(self.alpha * 255)
        surface.blit(rotated, self.position - new_origin)