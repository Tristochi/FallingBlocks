import pygame, sys, random

HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)

# Resource handling functions here


class Blocks(pygame.sprite.Sprite):
	""" Blocks that will fall from top of screen """

	def __init__(self, img):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect =  load_png(img)
		self.x = x
		self.y = y
		
	def update(self):
		pass
		
	def newPos(self, x, y):
		pass
		
class BlockGame(object):
	"""	Creates block game, controls movement of all blocks. """
	pass
	
	
	
def main():
	pygame.init()
	size = [WIDTH, HEIGHT]
	screen = pygame.display.set_mode(size)
	
	#Create instance of blocks. Takes path of image as paramater. 
	
	#Create game instance
	
	
	#Game Loop
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			
		
	
		pygame.display.flip()
		
	pygame.quit()
	
if __name__ == "__main__":
	main()
	
