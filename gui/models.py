class BaseEntity:
    def __init__(self, id, x, y, sprite):
        self.id = id
        self.sprite = sprite
        self.x = x
        self.y = y

    def blitme(self, screen):
        """Draw the player at its current location."""
        self.rect = self.sprite.get_rect()
        self.rect.topleft = self.x * 32, self.y * 32
        screen.blit(self.sprite, self.rect)

class Farmer(BaseEntity):
    def __init__(self, id, x, y, sprite):
        BaseEntity.__init__(self, id, x, y, sprite)
    
    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

class Plant(BaseEntity):
    def __init__(self, id, x, y, sprite):
        BaseEntity.__init__(self, id, x, y, sprite)