# import all the modules
from Fesnoria_Game_Factors import Game_Factors
from Fesnoria_Setup import Setup

import pygame


class Run(Setup):
    def __init__(self):
        # Allows Game factors to read __init__ of Setup
        super(Run, self).__init__()

    def loop(self):
        """ Run the game loop and all the game factors for eg.(detect keyboard input)
        """
        clock = pygame.time.Clock()
        self.running = True
        self.GF =  Game_Factors()

        try:
            while self.running:
                dt = clock.tick() / 100.

                self.GF.game_input()
                self.GF.handle_input()
                self.GF.keyboard_input()
                self.GF.update(dt)
                self.GF.draw(self.screen)
                pygame.display.flip()

        except KeyboardInterrupt:
            self.running = False