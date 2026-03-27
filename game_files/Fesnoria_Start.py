# import all the modules
from Fesnoria_Setup import Setup
from Fesnoria_Game_Setup import Game_Setup
from Fesnoria_Run_Loop import Run

import pygame
S = Setup()

if __name__ == "__main__":

    try:
        setup = Setup()
        setup.setup_done()

        gamesetup = Game_Setup()
        gamesetup.game_setup(S.MAP_FILENAME, S.MUSIC_FILENAME)

        run = Run()
        run.loop()
    except:
        pygame.quit()
        raise