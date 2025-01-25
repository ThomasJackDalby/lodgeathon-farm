class Farmer:
    def __init__(self, id, game, sprite):
        self.id = id
        self.image = sprite
        self.name = ''
        self.color = ''
        self.screen = game.screen

        # Start at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the player at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
    
    def move(self,delta_x,delta_y):
        self.x += delta_x
        self.y += delta_y

