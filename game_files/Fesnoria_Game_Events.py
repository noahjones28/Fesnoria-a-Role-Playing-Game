# import all the modules
from Fesnoria_Setup import Setup
from Fesnoria_Game_Setup import Game_Setup

import pygame
from pygame.locals import *


class Game_Events(Setup, Game_Setup):
    def __init__(self):
        # Allows Game Events to read __init__ of Setup
        super(Game_Events, self).__init__()

        # Allows Game Events to read __init__ of Game_Setup
        super(Game_Events, self).game_setup(self.MAP_FILENAME, self.MUSIC_FILENAME)

    def refresh(self):
        # Allows Game Events to read __init__ of Game_Setup
        super(Game_Events, self).game_setup(self.MAP_FILENAME, self.MUSIC_FILENAME)

    def forest_door_n(self):
        pressed = pygame.key.get_pressed()

        # zoom out when leaving
        if pygame.Rect.colliderect(self.forest_door_rect, self.hero.feet) and pressed[K_UP] and self.forest_door_key <=65 and self.forest_door_key >= 0:
            self.forest_door_key -= 1
            self.map_layer.zoom -= .0175
            print (self.forest_door_key)

        # zoom in when entering
        elif pygame.Rect.colliderect(self.forest_door_rect, self.hero.feet) and pressed[K_DOWN] and self.forest_door_key <=65 and self.forest_door_key >= 0:
            self.forest_door_key += 1
            self.map_layer.zoom += .0175
            print (self.forest_door_key)

        # once the door has been activated displays map_changer in Draw section of Game_Factors and cancel user input
        if self.forest_door_key <1 and self.forest_door_key >-50:
            print (self.forest_door_key)
            self.forest_door_key -= 1
            self.cancel_user_input = True

        # refresh
        if self.forest_door_key == -50:
            print (self.forest_door_key)
            # changes map
            self.MAP_FILENAME = 'resources/tmx/Foral Forest.tmx'

            # resets cancel_user_input
            self.cancel_user_input = False

            # resets game
            GS = Game_Setup()
            GS.game_setup(self.MAP_FILENAME, self.MUSIC_FILENAME)
            self.refresh()

            # applies lighting for next map
            self.apply_lighting = True
            self.lighting_opacity = 125
            self.lighting.set_alpha(self.lighting_opacity)



