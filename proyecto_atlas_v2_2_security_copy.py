# Proyecto Atlas versión 2
# Venga campeones que nosotros podemos!


# IMPORTS

import pygame
from sys import exit
from sprite_v2_2_security_copy import *

# FUNCTIONS

def calc_pos(id):
    n=id%40
    m=id//40
    if n == 0:
        n=40
        m-=1
    x=(n-1)*30
    y=m*30
    return Position(x,y)


def calc_square(position):
    Q=4*position[1]/3
    R=1+position[0]/30
    return int(Q+R)

# def collision_sprite():
# 	if pygame.sprite.collide_rect(runner.sprite.rect, minotaur.sprite.rect):
# 		return False
# 	else: return True

def main():

    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption('Proyecto Atlas')
    clock = pygame.time.Clock()

    game_active = False
    game_menu = False

    # Main menu screen
    main_menu_title_font = pygame.font.Font('fonts/Pixeltype.ttf', 110)
    main_menu_subtitle_font = pygame.font.Font('fonts/Pixeltype.ttf',75)
    main_menu_credits_font = pygame.font.Font('fonts/Pixeltype.ttf',35)
    game_name_text = main_menu_title_font.render('Proyecto Atlas',False,(221,221,221))
    game_name_text_rectangle = game_name_text.get_rect(center = (600,240))
    game_subtitle_text = main_menu_subtitle_font.render('Press space to play',False,(255,48,48))
    game_subtitle_text_rectangle = game_subtitle_text.get_rect(center = (600,380))
    game_credits_text = main_menu_credits_font.render('Created by G. Lahuerta, M. Bosom, E. Sanchez & A. Donaire', False, (221,221,221))
    game_credits_text_rectangle = game_credits_text.get_rect(bottomleft = (50,560))
    main_menu_background_surface = pygame.image.load('graphics/main_menu/rock_background2.png').convert()
    player_main_menu = pygame.image.load('graphics/in_game/runner_picture1.png').convert_alpha()
    player_main_menu = pygame.transform.rotozoom(player_main_menu, 0, 6)
    player_main_menu_rectangle = player_main_menu.get_rect(topleft=(100,220))
    minotaur_main_menu = pygame.image.load('graphics/in_game/minotaur1.png').convert_alpha()
    minotaur_main_menu = pygame.transform.rotozoom(minotaur_main_menu, 0, 6)
    minotaur_main_menu_rectangle = minotaur_main_menu.get_rect(topleft=(900,200))

    # In game
    in_game_font = pygame.font.Font('fonts/Pixeltype.ttf',45)
    game_background_surface = pygame.image.load('graphics/in_game/game_background5.png').convert()
    max_light=5
    bullets=0
    light=[]
    start_time = 0
    
    def display_candles_left():
        candles_left = 5-len(light)
        candles_left_text = in_game_font.render(f'Candles left: {candles_left}',False,(200,200,200))
        candles_left_text_rect = candles_left_text.get_rect(topleft=(100,18))
        screen.blit(candles_left_text, candles_left_text_rect)
    
    def display_seconds_elapsed():
        seconds_elapsed = int(pygame.time.get_ticks()/1000) - start_time
        seconds_elapsed_text = in_game_font.render(f'Seconds elapsed: {seconds_elapsed}',False,(200,200,200))
        seconds_elapsed_text_rect = seconds_elapsed_text.get_rect(topleft=(370,18))
        screen.blit(seconds_elapsed_text, seconds_elapsed_text_rect)
    
    def display_bullets():
        bullets_text = in_game_font.render(f'Bullets: {bullets}',False,(200,200,200))
        bullets_text_rect = bullets_text.get_rect(topleft=(700,18))
        screen.blit(bullets_text, bullets_text_rect)

    # Esc menu
    game_esc_menu_surface = pygame.image.load('graphics/in_game/esc_menu2.png').convert()
    esc_menu_font = pygame.font.Font('fonts/Pixeltype.ttf', 90)
    esc_menu_text = esc_menu_font.render('Game paused...',False,(221,221,221))
    esc_menu_text_rectangle = esc_menu_text.get_rect(center = (600,75))

    continue_text = main_menu_subtitle_font.render('Resume',False,(255,48,48))
    continue_text_rectangle = continue_text.get_rect(center = (175,200))

    restart_text = main_menu_subtitle_font.render('Restart',False,(255,48,48))
    restart_text_rectangle = restart_text.get_rect(center = (175,300))

    exit_text = main_menu_subtitle_font.render('Exit',False,(255,48,48))
    exit_text_rectangle = exit_text.get_rect(center = (175,400))


    # Groups
    player = pygame.sprite.GroupSingle()
    player.add(Runner())

    minotaur = pygame.sprite.GroupSingle()
    minotaur.add(Minotaur())


    # Maze generation
    dic_square={}
    handler = open('Nivel1', "r")
    text=handler.read()
    text=text.split("\n")
    for line in text:
        line=line.split(" ")
        if len(line)>1:
            key=int(line[0])
            if line[1]=="C":
                dic_square[key]=Floor(calc_pos(key),pygame.transform.scale(pygame.image.load('graphics/in_game/path_image3.png'), (30,30)))
                for square in line[2:]:
                    dic_square[key].near_square.append(int(square))
            elif line[1]=="T":
                dic_square[key]=TorchFloor(calc_pos(key),pygame.transform.scale(pygame.image.load('graphics/in_game/floor_candle1.png'), (30,30)))
                for square in line[2:]:
                    dic_square[key].near_square.append(int(square))
            elif line[1]=="D":
                dic_square[key]=Door(calc_pos(key),pygame.transform.scale(pygame.image.load('graphics/in_game/path_image3.png'), (30,30)),pygame.transform.scale(pygame.image.load('graphics/in_game/path_image3.png'), (30,30)))
            elif line[1]=="E":
                dic_square[key]=ShotgunFloor(calc_pos(key),pygame.transform.scale(pygame.image.load('graphics/in_game/shotgunfloor.png'), (30,30)),pygame.transform.scale(pygame.image.load('graphics/in_game/path_image3.png'), (30,30)))
                for square in line[2:]:
                    dic_square[key].near_square.append(int(square))



    while True:
        now = pygame.time.get_ticks()
        square=calc_square(player.sprite.rect.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                game_menu = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_menu = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_text_rectangle.collidepoint(event.pos):
                    game_menu = False
                if restart_text_rectangle.collidepoint(event.pos):
                    player.sprite.reset()
                    minotaur.sprite.reset()
                    game_menu = False
                    bullets=0
                    light = []
                    seconds_elapsed = seconds_elapsed - int(pygame.time.get_ticks()/1000)
                if exit_text_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    exit()

            if square in dic_square.keys():
                if (type(dic_square[square])==TorchFloor) and (event.type == pygame.KEYDOWN) and (event.key == pygame.K_e) and (len(light)<max_light):
                    light.append(square)

            if (not player.sprite.Shotgun) and (square in dic_square.keys()) and (type(dic_square[square])==ShotgunFloor) and (event.type == pygame.KEYDOWN) and (event.key == pygame.K_e):
                player.sprite.Shotgun=True
                bullets += 2


        if game_active:
            # start_time = int(pygame.time.get_ticks()/1000)
            if game_menu:
                screen.blit(game_esc_menu_surface,(0,0))
                screen.blit(esc_menu_text, esc_menu_text_rectangle)
                screen.blit(continue_text, continue_text_rectangle)
                screen.blit(restart_text, restart_text_rectangle)
                screen.blit(exit_text, exit_text_rectangle)


            else:
                error=True
                while error:
                    try:
                        screen.blit(game_background_surface,(0,0))

                        square=calc_square(player.sprite.rect.topleft)

                        screen.blit(dic_square[square].image,(dic_square[square].position.x,dic_square[square].position.y))
                        for i in dic_square[square].near_square:
                            for j in dic_square[i].near_square:
                                screen.blit(dic_square[j].image,(dic_square[j].position.x,dic_square[j].position.y))
                            screen.blit(dic_square[i].image,(dic_square[i].position.x,dic_square[i].position.y))

                        for i in light:
                            screen.blit(dic_square[i].image,(dic_square[i].position.x,dic_square[i].position.y))
                            for j in dic_square[i].near_square:
                                screen.blit(dic_square[j].image,(dic_square[j].position.x,dic_square[j].position.y))
                                for z in dic_square[j].near_square:
                                    screen.blit(dic_square[z].image,(dic_square[z].position.x,dic_square[z].position.y))

                        x0=minotaur.sprite.rect.x-player.sprite.rect.x
                        y0=minotaur.sprite.rect.y-player.sprite.rect.y

                        draw_min=False
                        if ((x0*x0+y0*y0)**0.5 <= 60) :
                            draw_min=True
                        else:
                            for i in light:
                                x0=minotaur.sprite.rect.x-dic_square[i].position.x
                                y0=minotaur.sprite.rect.y-dic_square[i].position.y

                                if ((x0*x0+y0*y0)**0.5 <= 60) :
                                    draw_min=True

                        if draw_min:
                            minotaur.draw(screen)
                        
                        minotaur.update()
                        player.draw(screen)
                        player.update()
                        display_candles_left()
                        display_seconds_elapsed()
                        display_bullets()
                        # game_active = collision_sprite()

                        error=False
                    except :
                        player.sprite.return_error()
                        continue

        else:
            # The main menu screen is shown
            screen.blit(main_menu_background_surface,(0,0))
            screen.blit(game_name_text, game_name_text_rectangle)
            screen.blit(game_subtitle_text, game_subtitle_text_rectangle)
            screen.blit(game_credits_text, game_credits_text_rectangle)
            screen.blit(player_main_menu, player_main_menu_rectangle)
            screen.blit(minotaur_main_menu, minotaur_main_menu_rectangle)
            

        pygame.display.update()
        clock.tick(60)




# MAIN
if __name__ == '__main__':
    main()
