import pygame
from pygame.locals import *
from random import randrange
 
def main():
	pygame.init()
	# TODO 1: initialise a window for display, set the argument size (width, height)
	screen = pygame.display.set_mode((  ,  ))
	# TODO 2: set the window caption
	pygame.display.set_caption(" ... ")
	clock = pygame.time.Clock()
 
	# Init
	# (nothing atm)
	
	# Game Loop
	while True:
		# Input
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					return
		# Logic
		# (nothing atm)
		
		# Render
		# TODO 3: fill the screen with a random rgb color
		r = randrange(0,255)
		g =
		b =
		screen.fill((r, , ))
		
		pygame.display.flip()
		
		clock.tick(1)
 
if __name__ == "__main__":
	main()
