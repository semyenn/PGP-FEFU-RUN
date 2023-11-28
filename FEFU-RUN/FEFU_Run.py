import pygame as pg
import random as rd
import sys
import classes

clock = pg.time.Clock()
secure_clock = pg.time.Clock()

pg.init()

width = 600
height = 350

game_name = pg.display.set_caption("FEFU Run")
icon = pg.image.load("images/icon.png")
pg.display.set_icon(icon)
screen = pg.display.set_mode((width, height))
background = pg.image.load("images/bg.jpg").convert()
bg = pg.transform.scale(background, (width, height))
bg_music = pg.mixer.Sound('sounds/bgmusic.mp3')

pos_x = 50
pos_y = 275

moving_sprites = pg.sprite.Group()
player = classes.Player(pos_x, pos_y)
moving_sprites.add(player)

secure_anim = [
    pg.image.load('images/security/security_10000.png').convert_alpha(),
    pg.image.load('images/security/security_10001.png').convert_alpha(),
    pg.image.load('images/security/security_10002.png').convert_alpha(),
    pg.image.load('images/security/security_10003.png').convert_alpha(),
    pg.image.load('images/security/security_10004.png').convert_alpha(),
    pg.image.load('images/security/security_10005.png').convert_alpha(),
    pg.image.load('images/security/security_10006.png').convert_alpha(),
    pg.image.load('images/security/security_10007.png').convert_alpha(),
    pg.image.load('images/security/security_10008.png').convert_alpha(),
    pg.image.load('images/security/security_10009.png').convert_alpha(),
    pg.image.load('images/security/security_10010.png').convert_alpha(),
    pg.image.load('images/security/security_10011.png').convert_alpha(),
    pg.image.load('images/security/security_10012.png').convert_alpha(),
    pg.image.load('images/security/security_10013.png').convert_alpha()
]

player_anim_count = 0
player_speed = 4.75

secure_anim_count = 0
secure_x = 610

bg_x = 0


running = True

is_jump = False
jump_height = 7

while True:
    clock.tick(13)
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))
    screen.blit(secure_anim[secure_anim_count], (secure_x, 280))
    
    moving_sprites.draw(screen)
    moving_sprites.update(0.5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYUP:
            player.animate()

    keys = pg.key.get_pressed()
    
    # if keys[pg.K_LEFT]:
    #     screen.blit(walk_left_anim[player_anim_count], (player_x, 275))
    # else:
    #     screen.blit(walk_right_anim[player_anim_count], (player_x, 275))
    
    if keys[pg.K_LEFT] and pos_x > 50:
        pos_x -= player_speed
    elif keys[pg.K_RIGHT] and pos_x < 150:
        pos_x += player_speed

    if not is_jump:
        if keys[pg.K_UP]:
            is_jump = True    
    else:
        if jump_height >= -7:
            if jump_height > 0:
                pos_y -= (jump_height ** 2) / 1.5
            else:
                pos_y += (jump_height ** 2) / 1.5
            jump_height -= 1
        else:
            is_jump = False
            jump_height = 7

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1
    
    if secure_anim_count == 13:
        secure_anim_count = 0
    else:
        secure_anim_count += 1

    bg_x -= 2
    if bg_x <= -600:
        bg_x = 0

    secure_x -= 10

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
