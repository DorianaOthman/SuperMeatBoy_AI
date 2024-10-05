from os import walk
import pygame

#Opens images for graphics
def import_folder(path, size=1):
    surface_list = []
    full_path = path + ".png" #+ '/' + image
    image_surf = pygame.image.load(full_path).convert_alpha()
    image_surf = pygame.transform.scale(image_surf, (int(image_surf.get_width() * size), int(image_surf.get_height() * size)))
    surface_list.append(image_surf)

    return surface_list
