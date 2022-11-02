import pygame 

from settings import *
from player import Player
from overlay import Overlay


class Level:
	""" Level loader and updater """
	def __init__(self):
		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

		self.overlay = Overlay(self.player)
	
	def setup(self):
		self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.all_sprites)

	def run(self, dt):
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)
		self.overlay.display()
		self.all_sprites.update(dt)
