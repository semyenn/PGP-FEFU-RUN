import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width=19, height=42):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_walking = False
        self.is_jumping = False
        self.walkside_sprites = [
            pg.image.load('images/walk/WalkSide0000.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0001.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0002.png').convert_alpha(),
            pg.image.load('images/walk/WalkSide0003.png').convert_alpha()
        ]
        self.jumping_sprites = [
            pg.image.load('images/jump/Jump0000.png').convert_alpha(),
            pg.image.load('images/jump/Jump0001.png').convert_alpha(),
            pg.image.load('images/jump/Jump0002.png').convert_alpha()
        ]
        self.current_sprite = 0
        self.current_sprite_jumping = 0
        self.image = self.walkside_sprites[self.current_sprite]
        self.image = self.jumping_sprites[self.current_sprite]

        self.rect = pg.Rect(self.pos_x, self.pos_y, width, height)

    def walk(self):
        self.is_walking = True

    def jump(self):
        self.is_jumping = True

    def update(self, speed, speed_jumping):
        if self.is_walking is True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.walkside_sprites):
                self.current_sprite = 0
                self.is_walking = False

        elif self.is_jumping is True:
            self.current_sprite_jumping += speed_jumping

            if self.current_sprite_jumping >= len(self.jumping_sprites):
                self.current_sprite_jumping = 0
                self.is_jumping = False

            for temp in range(20):  # Delay the falling down as loops are very fast
                if temp <= 10:
                    self.rect.y -= 0.5
                elif temp > 10:
                    self.rect.y += 0.5


class Ground():
    def __init__(self,speed=-5):
        self.image = pg.image.load("images/Ground.png").convert_alpha()
        self.image1 = pg.image.load("images/Ground.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()
        self.rect.bottom = 350
        self.rect1.bottom = 350
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        .blit(self.image, self.rect)
        .blit(self.image1, self.rect1)

    def update_ground(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right
