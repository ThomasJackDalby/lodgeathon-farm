"""Chess game, for learning to grab images from a sprite sheet."""

import sys
from spritesheet import SpriteSheet
from player import Player

import pygame

class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (225, 225, 225)


class Game:
    """Overall class to manage game assets and behaviour."""


    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.player_list = []

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("my game")

        self.sprites = SpriteSheet("tmw_desert_spacing.png")
        player_sprite = self.sprites.image_at( (0,0,32,32) )
        self.player_list.append(Player(self, player_sprite))

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            #self._get_state()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.player_list[0].move(-1,0)
                elif event.key == pygame.K_DOWN:
                    self.player_list[0].move(1,0)
                elif event.key == pygame.K_LEFT:
                    self.player_list[0].move(0,-1)
                elif event.key == pygame.K_RIGHT:
                    self.player_list[0].move(0,1)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for player in self.player_list:
            player.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()