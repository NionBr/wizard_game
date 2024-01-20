import pygame
from utils.load_images import load_tiles
from scripts.tile import Tile

class Level:
    def __init__(self, screen: pygame.Surface):
                
        self.tiles = load_tiles()
        self.level_map = []
        self.screen = screen
        self.level_config()
        
    def level_config(self):
        for i in range(self.screen.get_width() // self.tiles[1].get_width() + 100):
            if i == 0:
                tile = Tile(self.tiles[1], -20, self.screen.get_height() - self.tiles[1].get_height())
                self.level_map.append(tile)
            else:
                tile = Tile(self.tiles[2], self.tiles[2].get_width() * i + 27, self.screen.get_height() - self.tiles[1].get_height() + 12)
                self.level_map.append(tile)
                tile_0 = Tile(self.tiles[0], self.tiles[2].get_width() * i + 27, self.screen.get_height() - self.tiles[1].get_height() + 12 + self.tiles[2].get_height())
                self.level_map.append(tile_0)
                
    def draw(self):
        for i in range(len(self.level_map)):
            self.screen.blit(self.level_map[i].image, self.level_map[i].rect)