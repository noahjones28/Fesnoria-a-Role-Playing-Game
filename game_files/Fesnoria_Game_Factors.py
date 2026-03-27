# import all the modules
from Fesnoria_Game_Setup import Game_Setup
from Fesnoria_Game_Events import Game_Events

import pygame
from pygame.locals import *


class Game_Factors(Game_Events):
    def __init__(self):
        # Allows Game factors to read __init__ of Game_Events
        super(Game_Factors, self).__init__()

    def draw(self, surface):
        # center the map/screen on our Hero
        self.group.center(self.hero.rect.center)

        self.hero_pos = self.hero.rect.center

        # draw the map and all sprites
        self.group.draw(surface)

        # displays map changer if switching map
        if self.cancel_user_input == True:
            self.map_changer.set_alpha(self.map_changer_opacity)
            self.map_changer_opacity += 6
            self.screen.blit(self.map_changer, (0, 0))

        # changes lighting depending on map
        if self.apply_lighting == True:
            print (self.lighting_opacity)
            self.screen.blit(self.lighting, (0, 0))

    def game_input(self):
        if self.MAP_FILENAME == 'resources/tmx/Fesnoria Town.tmx':
            self.forest_door_n()

    def handle_input(self):
        if self.cancel_user_input == False:
            """ Handle pygame input events
            """
            poll = pygame.event.poll

            event = poll()
            while event:
                if event.type == QUIT:
                    self.running = False
                    break

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        break

                    elif event.key == K_EQUALS:
                        self.map_layer.zoom += .25

                    elif event.key == K_MINUS:
                        value = self.map_layer.zoom - .25
                        if value > 0:
                            self.map_layer.zoom = value

                # this will be handled if the window is resized
                elif event.type == VIDEORESIZE:
                    #init_screen(event.w, event.h)
                    self.map_layer.set_size((event.w, event.h))

                event = poll()


    def keyboard_input(self):
        if self.cancel_user_input == False:
            pressed = pygame.key.get_pressed()

            # Left_Up, Left_Down, Right_Up, Right_Down
            if pressed[K_LEFT] and pressed[K_UP]:
                # Moves Player Up
                self.hero.velocity[1] = -self.HERO_MOVE_SPEED
                # Moves Player Left
                self.hero.velocity[0] = -self.HERO_MOVE_SPEED
                self.ani_Cancel = True

                # Player animation section
                if self.hero.ani_choice is not "Left_Up/Left_Up_1" and self.hero.ani_choice is not "Left_Up/Left_Up_2" or self.keyLU1 < 8:
                    self.hero.ani_choice = "Left_Up/Left_Up_1"
                    self.keyLU1 -= 1
                    if self.keyLU1 == 0:
                        self.keyLU1 = 8

                elif self.hero.ani_choice == "Left_Up/Left_Up_1" and self.keyLU3 == 8 or self.keyLU2 < 8:
                    self.hero.ani_choice = "Left_Up/Left_Up_2"
                    self.keyLU2 -= 1
                    if self.keyLU2 == 0:
                        self.keyLU2 = 8

                elif self.hero.ani_choice == "Left_Up/Left_Up_2" or self.keyLU3 < 8:
                    self.hero.ani_choice = "Left_Up/Left_Up_1"
                    self.keyLU3 -= 1
                    if self.keyLU3 == 0:
                        self.keyLU3 = 8


            elif pressed[K_LEFT] and pressed[K_DOWN]:
                # Moves Player Down
                self.hero.velocity[1] = self.HERO_MOVE_SPEED
                # Moves Player Left
                self.hero.velocity[0] = -self.HERO_MOVE_SPEED
                self.ani_Cancel = True

                # Player animation section
                if self.hero.ani_choice is not "Left_Down/Left_Down_1" and self.hero.ani_choice is not "Left_Down/Left_Down_2" or self.keyLD1 < 8:
                    self.hero.ani_choice = "Left_Down/Left_Down_1"
                    self.keyLD1 -= 1
                    if self.keyLD1 == 0:
                        self.keyLD1 = 8

                elif self.hero.ani_choice == "Left_Down/Left_Down_1" and self.keyLD3 == 8 or self.keyLD2 < 8:
                    self.hero.ani_choice = "Left_Down/Left_Down_2"
                    self.keyLD2 -= 1
                    if self.keyLD2 == 0:
                        self.keyLD2 = 8

                elif self.hero.ani_choice == "Left_Down/Left_Down_2" or self.keyLD3 < 8:
                    self.hero.ani_choice = "Left_Down/Left_Down_1"
                    self.keyLD3 -= 1
                    if self.keyLD3 == 0:
                        self.keyLD3 = 8


            elif pressed[K_RIGHT] and pressed[K_UP]:
                # Moves Player Up
                self.hero.velocity[1] = -self.HERO_MOVE_SPEED
                # Moves Player Right
                self.hero.velocity[0] = self.HERO_MOVE_SPEED
                self.ani_Cancel = True

                # Player animation section
                if self.hero.ani_choice is not "Right_Up/Right_Up_1" and self.hero.ani_choice is not "Right_Up/Right_Up_2" or self.keyRU1 < 8:
                    self.hero.ani_choice = "Right_Up/Right_Up_1"
                    self.keyRU1 -= 1
                    if self.keyRU1 == 0:
                        self.keyRU1 = 8

                elif self.hero.ani_choice == "Right_Up/Right_Up_1" and self.keyRU3 == 8 or self.keyRU2 < 8:
                    self.hero.ani_choice = "Right_Up/Right_Up_2"
                    self.keyRU2 -= 1
                    if self.keyRU2 == 0:
                        self.keyRU2 = 8

                elif self.hero.ani_choice == "Right_Up/Right_Up_2" or self.keyRU3 < 8:
                    self.hero.ani_choice = "Right_Up/Right_Up_1"
                    self.keyRU3 -= 1
                    if self.keyRU3 == 0:
                        self.keyRU3 = 8


            elif pressed[K_RIGHT] and pressed[K_DOWN]:
               # Moves Player Down
                self.hero.velocity[1] = self.HERO_MOVE_SPEED
                # Moves Player Right
                self.hero.velocity[0] = self.HERO_MOVE_SPEED
                self.ani_Cancel = True

                # Player animation section
                if self.hero.ani_choice is not "Right_Down/Right_Down_1" and self.hero.ani_choice is not "Right_Down/Right_Down_2" or self.keyRD1 < 8:
                    self.hero.ani_choice = "Right_Down/Right_Down_1"
                    self.keyRD1 -= 1
                    if self.keyRD1 == 0:
                        self.keyRD1 = 8

                elif self.hero.ani_choice == "Right_Down/Right_Down_1" and self.keyRD3 == 8 or self.keyRD2 < 8:
                    self.hero.ani_choice = "Right_Down/Right_Down_2"
                    self.keyRD2 -= 1
                    if self.keyRD2 == 0:
                        self.keyRD2 = 8

                elif self.hero.ani_choice == "Right_Down/Right_Down_2" or self.keyRD3 < 8:
                    self.hero.ani_choice = "Right_Down/Right_Down_1"
                    self.keyRD3 -= 1
                    if self.keyRD3 == 0:
                        self.keyRD3 = 8
            else:
                self.ani_Cancel = False

                # Stops player animation from last update
                self.hero.velocity[1] = 0
                self.hero.velocity[0] = 0

                # if no keys are being pressed, this will make the player stand still
                if self.hero.ani_choice == "Left_Up/Left_Up_1" or self.hero.ani_choice == "Left_Up/Left_Up_2":
                    self.hero.ani_choice = "Left_Up/Left_Up_Middle"
                elif self.hero.ani_choice == "Left_Down/Left_Down_1" or self.hero.ani_choice == "Left_Down/Left_Down_2":
                    self.hero.ani_choice = "Left_Down/Left_Down_Middle"
                elif self.hero.ani_choice == "Right_Up/Right_Up_1" or self.hero.ani_choice == "Right_Up/Right_Up_2":
                    self.hero.ani_choice = "Right_Up/Right_Up_Middle"
                elif self.hero.ani_choice == "Right_Down/Right_Down_1" or self.hero.ani_choice == "Right_Down/Right_Down_2":
                    self.hero.ani_choice = "Right_Down/Right_Down_Middle"









            # Up, Down, Left, Right
            # If one of the diagonal keys has been pressed this will cancel the code below.
            if self.ani_Cancel == False:
                if pressed[K_UP]:
                    # Moves Player Up
                    self.hero.velocity[1] = -self.HERO_MOVE_SPEED

                    # Player animation section
                    if self.hero.ani_choice is not "Up/Up_1" and self.hero.ani_choice is not "Up/Up_2" or self.keyU1 < 8:
                        self.hero.ani_choice = "Up/Up_1"
                        self.keyU1 -= 1
                        if self.keyU1 == 0:
                            self.keyU1 = 8

                    elif self.hero.ani_choice == "Up/Up_1" and self.keyU3 == 8 or self.keyU2 < 8:
                        self.hero.ani_choice = "Up/Up_2"
                        self.keyU2 -= 1
                        if self.keyU2 == 0:
                            self.keyU2 = 8

                    elif self.hero.ani_choice == "Up/Up_2" or self.keyU3 < 8:
                        self.hero.ani_choice = "Up/Up_1"
                        self.keyU3 -= 1
                        if self.keyU3 == 0:
                            self.keyU3 = 8



                elif pressed[K_DOWN]:
                    # Moves Player Down
                    self.hero.velocity[1] = self.HERO_MOVE_SPEED

                    # Player animation section
                    if self.hero.ani_choice is not "Down/Down_1" and self.hero.ani_choice is not "Down/Down_2" or self.keyD1 < 8:
                        self.hero.ani_choice = "Down/Down_1"
                        self.keyD1 -= 1
                        if self.keyD1 == 0:
                            self.keyD1 = 8

                    elif self.hero.ani_choice == "Down/Down_1" and self.keyD3 == 8 or self.keyD2 < 8:
                        self.hero.ani_choice = "Down/Down_2"
                        self.keyD2 -= 1
                        if self.keyD2 == 0:
                            self.keyD2 = 8

                    elif self.hero.ani_choice == "Down/Down_2" or self.keyD3 < 8:
                        self.hero.ani_choice = "Down/Down_1"
                        self.keyD3 -= 1
                        if self.keyD3 == 0:
                           self.keyD3 = 8



                elif pressed[K_LEFT]:
                    # Moves Player Left
                    self.hero.velocity[0] = -self.HERO_MOVE_SPEED

                    # Player animation section
                    if self.hero.ani_choice is not "Left/Left_1" and self.hero.ani_choice is not "Left/Left_2" or self.keyL1 < 8:
                        self.hero.ani_choice = "Left/Left_1"
                        self.keyL1 -= 1
                        if self.keyL1 == 0:
                            self.keyL1 = 8

                    elif self.hero.ani_choice == "Left/Left_1" and self.keyL3 == 8 or self.keyL2 < 8:
                        self.hero.ani_choice = "Left/Left_2"
                        self.keyL2 -= 1
                        if self.keyL2 == 0:
                            self.keyL2 = 8

                    elif self.hero.ani_choice == "Left/Left_2" or self.keyL3 < 8:
                        self.hero.ani_choice = "Left/Left_1"
                        self.keyL3 -= 1
                        if self.keyL3 == 0:
                            self.keyL3 = 8


                elif pressed[K_RIGHT]:
                    # Moves Player Right
                    self.hero.velocity[0] = self.HERO_MOVE_SPEED

                    # Player animation section
                    if self.hero.ani_choice is not "Right/Right_1" and self.hero.ani_choice is not "Right/Right_2" or self.keyR1 < 8:
                        self.hero.ani_choice = "Right/Right_1"
                        self.keyR1 -= 1
                        if self.keyR1 == 0:
                            self.keyR1 = 8

                    elif self.hero.ani_choice == "Right/Right_1" and self.keyR3 == 8 or self.keyR2 < 8:
                        self.hero.ani_choice = "Right/Right_2"
                        self.keyR2 -= 1
                        if self.keyR2 == 0:
                            self.keyR2 = 8

                    elif self.hero.ani_choice == "Right/Right_2" or self.keyR3 < 8:
                        self.hero.ani_choice = "Right/Right_1"
                        self.keyR3 -= 1
                        if self.keyR3 == 0:
                            self.keyR3 = 8

                # if no keys are being pressed, this will make the player stand still
                else:
                    if self.hero.ani_choice == "Up/Up_1" or self.hero.ani_choice == "Up/Up_2":
                        self.hero.ani_choice = "Up/Up_Middle"
                    elif self.hero.ani_choice == "Down/Down_1" or self.hero.ani_choice == "Down/Down_2":
                        self.hero.ani_choice = "Down/Down_Middle"
                    elif self.hero.ani_choice == "Left/Left_1" or self.hero.ani_choice == "Left/Left_2":
                        self.hero.ani_choice = "Left/Left_Middle"
                    elif self.hero.ani_choice == "Right/Right_1" or self.hero.ani_choice == "Right/Right_2":
                        self.hero.ani_choice = "Right/Right_Middle"

                # Stops player animation from last update
                if self.hero.ani_choice is not "Up/Up_1" and self.hero.ani_choice is not "Up/Up_2" and self.hero.ani_choice is not "Down/Down_1" and self.hero.ani_choice is not "Down/Down_2":
                    self.hero.velocity[1] = 0
                 # Stops player animation from last update
                if self.hero.ani_choice is not "Left/Left_1" and self.hero.ani_choice is not "Left/Left_2" and self.hero.ani_choice is not "Right/Right_1" and self.hero.ani_choice is not "Right/Right_2":
                    self.hero.velocity[0] = 0








        # if switching map make player walk up automatically
        elif self.cancel_user_input == True:
                                # Moves Player Up
                    self.hero.velocity[1] = -self.HERO_MOVE_SPEED

                    # Player animation section
                    if self.hero.ani_choice is not "Up/Up_1" and self.hero.ani_choice is not "Up/Up_2" or self.keyU1 < 8:
                        self.hero.ani_choice = "Up/Up_1"
                        self.keyU1 -= 1
                        if self.keyU1 == 0:
                            self.keyU1 = 8

                    elif self.hero.ani_choice == "Up/Up_1" and self.keyU3 == 8 or self.keyU2 < 8:
                        self.hero.ani_choice = "Up/Up_2"
                        self.keyU2 -= 1
                        if self.keyU2 == 0:
                            self.keyU2 = 8

                    elif self.hero.ani_choice == "Up/Up_2" or self.keyU3 < 8:
                        self.hero.ani_choice = "Up/Up_1"
                        self.keyU3 -= 1
                        if self.keyU3 == 0:
                            self.keyU3 = 8

    def update(self, dt):
        """ Tasks that occur over time should be handled here
        """
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)