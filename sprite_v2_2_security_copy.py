# IMPORTS
import pygame
# from ABC import all

#@abstractclass
class Position():
    def __init__(self, x, y):
        self.x=x
        self.y=y

#@abstractclass
class Sprite():
    def __init__(self, image, square):
        self.image=image
        self.square=square
        self.health=True

class Minotaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        r_minotaur_image1 = pygame.image.load('graphics/in_game/minotaur1.png').convert_alpha()
        r_minotaur_image2 = pygame.image.load('graphics/in_game/minotaur2.png').convert_alpha()
        r_minotaur_image3 = pygame.image.load('graphics/in_game/minotaur3.png').convert_alpha()
        r_minotaur_image4 = pygame.image.load('graphics/in_game/minotaur4.png').convert_alpha()
        r_minotaur_image5 = pygame.image.load('graphics/in_game/minotaur5.png').convert_alpha()
        r_minotaur_image6 = pygame.image.load('graphics/in_game/minotaur6.png').convert_alpha()
        r_minotaur_image7 = pygame.image.load('graphics/in_game/minotaur7.png').convert_alpha()
        r_minotaur_image8 = pygame.image.load('graphics/in_game/minotaur8.png').convert_alpha()
        r_minotaur_image9 = pygame.image.load('graphics/in_game/minotaur9.png').convert_alpha()
        r_minotaur_image10 = pygame.image.load('graphics/in_game/minotaur10.png').convert_alpha()
        self.r_minotaur_images = [r_minotaur_image1, r_minotaur_image2, r_minotaur_image3, r_minotaur_image4, r_minotaur_image5, r_minotaur_image6, r_minotaur_image7, r_minotaur_image8, r_minotaur_image9, r_minotaur_image10]
        l_minotaur_image1 = pygame.transform.flip(r_minotaur_image1, True, False)
        l_minotaur_image2 = pygame.transform.flip(r_minotaur_image2, True, False)
        l_minotaur_image3 = pygame.transform.flip(r_minotaur_image3, True, False)
        l_minotaur_image4 = pygame.transform.flip(r_minotaur_image4, True, False)
        l_minotaur_image5 = pygame.transform.flip(r_minotaur_image5, True, False)
        l_minotaur_image6 = pygame.transform.flip(r_minotaur_image6, True, False)
        l_minotaur_image7 = pygame.transform.flip(r_minotaur_image7, True, False)
        l_minotaur_image8 = pygame.transform.flip(r_minotaur_image8, True, False)
        l_minotaur_image9 = pygame.transform.flip(r_minotaur_image9, True, False)
        l_minotaur_image10 = pygame.transform.flip(r_minotaur_image10, True, False)
        self.l_minotaur_images = [l_minotaur_image1, l_minotaur_image2, l_minotaur_image3, l_minotaur_image4, l_minotaur_image5, l_minotaur_image6, l_minotaur_image7, l_minotaur_image8, l_minotaur_image9, l_minotaur_image10]
        self.minotaur_frame = self.r_minotaur_images
        self.minotaur_index = 0
        self.image = self.minotaur_frame[self.minotaur_index]
        self.rect = self.image.get_rect(bottomleft = (570,270))
        self.round = 0

    def animation_state(self):
        self.minotaur_index += 0.1
        if self.minotaur_index >= len(self.minotaur_frame):
            self.minotaur_index = 0
        self.image = self.minotaur_frame[int(self.minotaur_index)]
    
    def movement(self):
        movement_list="22222122223333333332222211122121114112114441441444144144444443334443444441111443343344333222334443333322332222122221111411122211"
        i = 0
        print('time: ',i)
        if movement_list[i]==1:
            self.rect.y+=30
        elif movement_list[i]==2:
            self.rect.x-=30
        elif movement_list[i]==3:
            self.rect.y-=30
        else:
            self.rect.x+=30
        if i == len(movement_list):
            self.round += 1
        
    def reset(self):
        self.rect.bottomleft = (570,270)

    def update(self):
        print('min upd')
        self.animation_state()
        #self.movement(player_num_mov)
    
    # movement_list="22222122223333333332222211122121114112114441441444144144444443334443444441111443343344333222334443333322332222122221111411122211"
    # i=0

    # [...]

    # if movement_list[i]==1:
    #     minotaur.sprite.rect.y+=30
    # elif movement_list[i]==2:
    #     minotaur.sprite.rect.x-=30
    # elif movement_list[i]==3:
    #     minotaur.sprite.rect.y-=30
    # else:
    #     minotaur.sprite.rect.x+=30

    # i+=1
    # if i==len(movement_list):
    #     i=0


class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        r_runner_image1 = pygame.image.load('graphics/in_game/runner_picture1.png').convert_alpha()
        r_runner_image2 = pygame.image.load('graphics/in_game/runner_picture2.png').convert_alpha()
        r_runner_image3 = pygame.image.load('graphics/in_game/runner_picture3.png').convert_alpha()
        r_runner_image4 = pygame.image.load('graphics/in_game/runner_picture4.png').convert_alpha()
        self.r_runner_images = [r_runner_image1, r_runner_image2, r_runner_image3, r_runner_image4]
        l_runner_image1 = pygame.transform.flip(r_runner_image1, True, False)
        l_runner_image2 = pygame.transform.flip(r_runner_image2, True, False)
        l_runner_image3 = pygame.transform.flip(r_runner_image3, True, False)
        l_runner_image4 = pygame.transform.flip(r_runner_image4, True, False)
        self.l_runner_images = [l_runner_image1, l_runner_image2, l_runner_image3, l_runner_image4]
        r_runner_shotgun1 = pygame.image.load('graphics/in_game/runner_shotgun1.png').convert_alpha()
        r_runner_shotgun2 = pygame.image.load('graphics/in_game/runner_shotgun2.png').convert_alpha()
        r_runner_shotgun3 = pygame.image.load('graphics/in_game/runner_shotgun3.png').convert_alpha()
        r_runner_shotgun4 = pygame.image.load('graphics/in_game/runner_shotgun4.png').convert_alpha()
        self.r_runner_shotgun = [r_runner_shotgun1, r_runner_shotgun2, r_runner_shotgun3, r_runner_shotgun4]
        l_runner_shotgun1 = pygame.transform.flip(r_runner_shotgun1, True, False)
        l_runner_shotgun2 = pygame.transform.flip(r_runner_shotgun2, True, False)
        l_runner_shotgun3 = pygame.transform.flip(r_runner_shotgun3, True, False)
        l_runner_shotgun4 = pygame.transform.flip(r_runner_shotgun4, True, False)
        self.l_runner_shotgun = [l_runner_shotgun1, l_runner_shotgun2, l_runner_shotgun3, l_runner_image4]
        self.runner_frame = self.r_runner_images
        self.runner_index = 0
        self.image = self.runner_frame[self.runner_index]
        self.rect = self.image.get_rect(bottomleft = (30,330))
        self.last_move = 0
        self.cooldown = 200
        self.pos = (30,330)
        self.Shotgun = False
        self.bullets = 0
    
    def get_bullets(self):
        return self.bullets

    def get_shotgun(self):
        self.Shotgun = True
        self.bullets += 2

    def player_input(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if now - self.last_move >= self.cooldown:
            if keys[pygame.K_w]:
                self.rect.y -= 30
                self.last_move = pygame.time.get_ticks()
            elif keys[pygame.K_a]:
                self.rect.x -= 30
                if self.Shotgun:
                    self.runner_frame = self.l_runner_shotgun
                else:
                    self.runner_frame = self.l_runner_images
                self.last_move = pygame.time.get_ticks()
            elif keys[pygame.K_s]:
                self.rect.y += 30
                self.last_move = pygame.time.get_ticks()
            elif keys[pygame.K_d]:
                self.rect.x += 30
                if self.Shotgun:
                    self.runner_frame = self.r_runner_shotgun
                else:
                    self.runner_frame = self.r_runner_images
                self.last_move = pygame.time.get_ticks()

    def animation_state(self):
        self.runner_index += 0.1
        if self.runner_index >= len(self.runner_frame):
            self.runner_index = 0
        self.image = self.runner_frame[int(self.runner_index)]

    def reset(self):
        self.rect.bottomleft = (30,330)


    def return_error(self):
            self.rect.topleft = self.pos


    def update(self):
        self.pos=self.rect.topleft
        self.player_input()
        self.animation_state()


class Wall():
    def __init__(self, position, image):
        self.position=position
        self.image=image

class Door():
    def __init__(self, position, image_door, image_floor):
        self.position=position
        self.image_door=image_door
        self.image_floor=image_floor
        self.image=image_door
        self.open=False

    def open_door(self):
        self.open=True
        self.image=self.image_floor

class Floor():
    def __init__(self, position, image):
        self.position=position
        self.near_square=[]
        self.image = image

    def set_near_square(self, square):
        self.near_square.append(square)

class ShotgunFloor():
    def __init__(self, position, image_shotgun, image_empty):
        self.position=position
        self.near_square=[]
        self.image_shotgun=image_shotgun
        self.image_empty=image_empty
        self.image=image_shotgun

class TorchFloor():
    def __init__(self, position, image):
        self.position=position
        self.near_square=[]
        self.image = image
        self.light=False
