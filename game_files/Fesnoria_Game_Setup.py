# import all the modules
from Fesnoria_Hero import Hero

import pygame
from pytmx.util_pygame import load_pygame

import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup


class Game_Setup(object):
    def game_setup(self, map_filename, music_filename):
        # true while running
        self.running = False

        self.screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

        # load keys for animations

        # Straight Keys
        # Right Keys
        self.keyR1 = 8
        self.keyR2 = 8
        self.keyR3 = 8

        # Left Keys
        self.keyL1 = 8
        self.keyL2 = 8
        self.keyL3 = 8

        # Up Keys
        self.keyU1 = 8
        self.keyU2 = 8
        self.keyU3 = 8

        # Down Keys
        self.keyD1 = 8
        self.keyD2 = 8
        self.keyD3 = 8


        # Diagonal Keys
        # Left_Up Keys
        self.keyLU1 = 8
        self.keyLU2 = 8
        self.keyLU3 = 8

        # Left_Down Keys
        self.keyLD1 = 8
        self.keyLD2 = 8
        self.keyLD3 = 8

        # Right_Up Keys
        self.keyRU1 = 8
        self.keyRU2 = 8
        self.keyRU3 = 8

        # Right_Down Keys
        self.keyRD1 = 8
        self.keyRD2 = 8
        self.keyRD3 = 8

        # Allows access to (Up, Down, Left, Right) animations
        self.ani_Cancel = False

        # Stops user input if game input is happening
        self.cancel_user_input = False

        # Stops user input if game input is happening
        self.apply_lighting = False

        # load data from pytmx
        print (map_filename)
        self.tmx_data = load_pygame(map_filename)

        # setup level geometry with simple pygame rects, loaded from pytmx
        self.walls = list()
        for object in self.tmx_data.objects:
            self.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(self.tmx_data)

        # create new renderer (camera)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 2

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the default
        # layer for sprites as 2
        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # loads map changer
        self.map_changer = pygame.image.load("resources/images/Misc/Map_Changer.png").convert()
        self.map_changer_opacity = 0

        # loads lighting
        self.lighting = pygame.image.load("resources/images/Misc/Map_Changer.png").convert()
        self.lighting_opacity = 0

        # loads music
        pygame.mixer.init(44100, -16,2,2048)
        pygame.mixer.music.load(music_filename)
        pygame.mixer.music.play(-1,0.0)

        self.hero = Hero()

        # put the hero in the center of the map
        self.hero.position = self.map_layer.map_rect.center

        # add our hero to the group
        self.group.add(self.hero)

        self.load_objects(map_filename)
        print ("done")



    def load_objects(self, map_filename):
        # forest door north
        if map_filename == 'resources/tmx/Fesnoria Town.tmx':
            self.forest_door_object = self.tmx_data.get_object_by_name("forest door")
            self.forest_door_rect = pygame.Rect(self.forest_door_object.x, self.forest_door_object.y, self.forest_door_object.width, (self.forest_door_object.height + 150))
            self.forest_door_key = 60

        if map_filename == 'resources/tmx/Foral Forest.tmx':
            self.foral_door_object = self.tmx_data.get_object_by_name("Foral Forest Door")
            self.foral_door_rect = pygame.Rect(self.foral_door_object.x, self.foral_door_object.y, self.foral_door_object.width, (self.foral_door_object.height + 150))
            self.forest_door_key_door_key = 60





