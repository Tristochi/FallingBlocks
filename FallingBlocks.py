import pygame, sys, random

HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)

# Resource handling functions here


class Blocks(pygame.sprite.Sprite):
"""Blocks that will fall from top of screen"""

	def __init__(self, img):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect =  load_png(img)
		self.x = x
		self.y = y
		
	def update(self):

	def newPos(self, x, y):
class BlockGame(object):
"""	Creates block game, controls movement of all blocks. """
	
	
	
	
def main:
	pygame.init()
	size = [WIDTH, HEIGHT]
	screen = pygame.display.set_mode(size)
	
	#Create game instance
	game = BlockGame()

