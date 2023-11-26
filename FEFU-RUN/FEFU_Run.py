import pygame as pg
import random as rd

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

walk_left_anim = [
    pg.image.load('images/walk/WalkSide0000.png').convert_alpha(),
    pg.image.load('images/walk/WalkSide0001.png').convert_alpha(),
    pg.image.load('images/walk/WalkSide0002.png').convert_alpha(),
    pg.image.load('images/walk/WalkSide0003.png').convert_alpha()
]

walk_right_anim = [

]

jump_anim = [

]

die_anim = [

]

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

flying_entity_anim = [

]

player_anim_count = 0
player_speed = 4.75
player_x = 50
player_y = 275

secure_anim_count = 0
secure_x = 610

bg_x = 0


running = True

is_jump = False
jump_height = 7

while running:
    clock.tick(13)
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))
    screen.blit(secure_anim[secure_anim_count], (secure_x, 280))

    screen.blit(walk_left_anim[player_anim_count], (player_x, player_y))

    keys = pg.key.get_pressed()
    
    # if keys[pg.K_LEFT]:
    #     screen.blit(walk_left_anim[player_anim_count], (player_x, 275))
    # else:
    #     screen.blit(walk_right_anim[player_anim_count], (player_x, 275))
    
    if keys[pg.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pg.K_RIGHT] and player_x < 150:
        player_x += player_speed

    if not is_jump:
        if keys[pg.K_UP]:
            is_jump = True    
    else:
        if jump_height >= -7:
            if jump_height > 0:
                player_y -= (jump_height ** 2) / 1.5
            else:
                player_y += (jump_height ** 2) / 1.5
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
