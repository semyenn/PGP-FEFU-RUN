import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.walkside_sprites = [
            pg.image.load('images/walk/WalkSide0000.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0001.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0002.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0003.png').convert_alpha()
        ]
        self.current_sprite = 0
        self.image = self.walkside_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating is True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.walkside_sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.walkside_sprites[int(self.current_sprite)]
