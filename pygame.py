import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):
	def __init__(self):
		super(Square, self).__init__()
		self.surf = pygame.Surface((25, 25))
		self.surf.fill((0, 0, 0))
		self.rect = self.surf.get_rect()

pygame.init()
screen = pygame.display.set_mode((700, 600))

square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()
square5 = Square()

gameOn = True

while gameOn:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				gameOn = False
		elif event.type == QUIT:
			gameOn = False
      
	screen.blit(square1.surf, (50, 40))
	screen.blit(square2.surf, (150, 40))
	screen.blit(square3.surf, (300, 40))
	screen.blit(square4.surf, (450, 40))
  	screen.blit(square4.surf, (600, 40))

	pygame.display.flip()
