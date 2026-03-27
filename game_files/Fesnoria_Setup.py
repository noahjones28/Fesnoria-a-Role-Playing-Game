# import all the modules
import pygame

class Setup(object):
    def __init__(self):
        # Setup
        # change window settings
        self.screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
        pygame.display.set_caption('Fesnoria - An epic journey.')

        # define configuration variables here
        self.HERO_MOVE_SPEED = 10  # pixels per second
        self.MAP_FILENAME = 'resources/tmx/Fesnoria Town.tmx'
        self.MUSIC_FILENAME = "resources/music/Forest_Song.mp3"

    def setup_done(self):
        print ("setup complete!")



