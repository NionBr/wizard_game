import pygame
from os import listdir
from os.path import join, isfile

def flip_image(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprites(dir1, dir2, width, height, direction = False):
    
    path = join('assets', dir1, dir2)
    images = [image for image in listdir(path) if isfile(join(path, image))]

    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)
            sprites.append(surface)
            
        if direction:
            all_sprites[image.replace('.png', '') + '_right'] = sprites
            all_sprites[image.replace('.png', '') + '_left'] = flip_image(sprites)
        else:
            all_sprites[image.replace('.png', '')] = sprites
        
    return all_sprites

def load_background(image):

    path = join('assets', 'images', 'background')
    image = pygame.image.load(path + '/' + image).convert_alpha()
    image = pygame.transform.scale(image, (image.get_width() * 1.4, image.get_height() * 1.4))
    
    return image


def load_tiles():
    
    path = join('assets', 'images', 'tiles')
    images = [i for i in listdir(path) if isfile(join(path, i))]
    
    all_tiles = []
    for image in images:
        tile = pygame.image.load(join(path, image)).convert_alpha()
        all_tiles.append(tile)
        
    return all_tiles