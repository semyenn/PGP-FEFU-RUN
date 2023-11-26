import pygame
from pygame import *

MOVE_SPEED = 7
WIDTH = 19
HEIGHT = 42
COLOR = "#888888"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = +MOVE_SPEED
        if not(left or right):
            self.xvel = 0
        self.rect.x += self.xvel

    def draw(self, screen):
        screen.blit(self.image,  (self.rect.x, self.rect.y))


#Эти строчки нужны для движения
#
#if e.type == KEYDOWN and e.key == K_LEFT:
#   left = True
#if e.type == KEYDOWN and e.key == K_RIGHT:
#   right = True
#
# e.type == KEYUP and e.key == K_RIGHT:
#   right = False
#if e.type == KEYUP and e.key == K_LEFT:
#    left = False#
