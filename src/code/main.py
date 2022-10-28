import pygame, sys
from settings import *
from level import Level


class Game:
	""" Main (game) class """
	def __init__(self):
		""" Setup the game """
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('Voidriver Valley')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		""" Run the game """
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()


if __name__ == '__main__':
	""" Entry point """
	game = Game()
	game.run()
