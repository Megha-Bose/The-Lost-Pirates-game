import random, os.path, math

import pygame
from pygame.locals import *

pygame.init()
largeFont = pygame.font.SysFont('comicsans', 30)
lFont = pygame.font.SysFont('comicsans', 60)
llFont = pygame.font.SysFont('comicsans', 100)

#setting the background screen
def setscreen():
	screen = pygame.display.set_mode((1400,950))
	pygame.display.set_caption("The Lost Pirates")
	icon = pygame.image.load('./data/boat.png')
	pygame.display.set_icon(icon)
	screen.fill((42,191,220))
	pygame.draw.rect(screen, [168, 130, 27], [0, 0, 1400, 60], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 150, 1400, 50], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 300, 1400, 50], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 450, 1400, 50], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 600, 1400, 50], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 750, 1400, 50], 0)
	pygame.draw.rect(screen, [168, 130, 27], [0, 890, 1400, 60], 0)

#showing end screen
def endscreen(llFont,lFont,score1,score2):
    screen = pygame.display.set_mode((1400,950))
    screen.fill((42,191,220))
    msg = llFont.render('GAME OVER', 1, (255,0,0))
    screen.blit(msg,(500,300))
    if score1>score2:
        winner1 = lFont.render('WINNER: PLAYER 1', 1, (0,0,0))
        screen.blit(winner1,(520,400))
    elif score2>score1:
        winner2 = lFont.render('WINNER: PLAYER 2', 1, (0,0,0))
        screen.blit(winner2,(520,400))
    else:
        tie = lFont.render('TIE', 1, (0,0,0))
        screen.blit(tie,(520,400))
    pygame.display.update()
    pygame.time.delay(3000)

#Player1 class declaration
class Player1(pygame.sprite.Sprite):
	images = []
	vx = 0
	vy = 0
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./data/pirate1.png')
		self.rect = self.image.get_rect()

		self.rect.center = pos

#Player2 class declaration
class Player2(pygame.sprite.Sprite):
	images = []
	vx = 0
	vy = 0
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./data/pirate2.png')
		self.rect = self.image.get_rect()

		self.rect.center = pos

#class of moving obstacles
class Movingobs(pygame.sprite.Sprite):
	images = ['./data/ship1.png', './data/crab.png', './data/ship2.png', './data/seahorse.png','./data/whale.png', './data/ship3.png']
	vx = 0
	def __init__(self, pos, num):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(self.images[num])
		self.rect = self.image.get_rect()

		self.rect.center = pos

#class of fixed obstacles
class Fixedobs(pygame.sprite.Sprite):
	images = ['./data/rock.png', './data/police.png', './data/urchin.png']
	def __init__(self, pos, num):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(self.images[num])
		self.rect = self.image.get_rect()

		self.rect.center = pos

#showing explosion
class Explosion(pygame.sprite.Sprite):
    images = ['./data/explosion1.gif']
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(self.images[0])
        self.rect = actor.rect.center
