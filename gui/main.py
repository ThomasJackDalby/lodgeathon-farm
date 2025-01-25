"""Chess game, for learning to grab images from a sprite sheet."""

import sys
import requests
import pygame
from spritesheet import SpriteSheet
from models import Farmer, Plant

class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (225, 225, 225)

class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.farmers = {}
        self.plants = {}
        self.next_state_update = 0

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Lodgeathon!")
        self.sprites = SpriteSheet("sprites.bmp")

    def add_farmer(self, id, x, y):
        player_sprite = self.sprites.image_at((0,0,32,32) )
        farmer = Farmer(id, x, y, player_sprite)
        self.farmers[id] = farmer
        return farmer
    
    def add_plant(self, id, x, y):
        plant_sprite = self.sprites.image_at((0,0,32,32) )
        plant = Plant(id, x, y, plant_sprite)
        self.plants[id] = plant
        return plant

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._get_state()
            self._update_screen()

    def _get_state(self):
        self.next_state_update -= 1
        if self.next_state_update > 0: return
        self.next_state_update = 30

        farmers_json = requests.get("http://localhost:8000/farmers").json()
        for farmer_json in farmers_json:
            farmer = self.farmers.get(farmer_json["id"], None)
            if farmer is None: farmer = self.add_farmer(farmer_json["id"], farmer_json["x"], farmer_json["y"])
            farmer.x = farmer_json["x"]
            farmer.y = farmer_json["y"]

        plants_json = requests.get("http://localhost:8000/plants").json()
        for plant_json in plants_json:
            plant = self.plants.get(plant_json["id"], None)
            if plant is None: plant = self.add_plant(plant_json["id"], plant_json["x"], plant_json["y"])
            plant.x = plant_json["x"]
            plant.y = plant_json["y"]

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.farmers[0].move(-1,0)
                elif event.key == pygame.K_DOWN:
                    self.farmers[0].move(1,0)
                elif event.key == pygame.K_LEFT:
                    self.farmers[0].move(0,-1)
                elif event.key == pygame.K_RIGHT:
                    self.farmers[0].move(0,1)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for plant in self.plants.values(): plant.blitme(self.screen)
        for player in self.farmers.values(): player.blitme(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()