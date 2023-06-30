import pygame
from pygame.locals import *
import buttons

pygame.init()

#Definindo uma matriz para realizar a representação do cenário
mat = [
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000090000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000080000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000900000000000',
    '00000000000000000000000000000000000000000000000080080000000000008000000000000000',
    '00000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '00000000000000000000000000000008000000000004500000000004500000090000000000000000',
    '00000000000000000000000000000000000000000003600000000003250000000000000000000000',
    '000000000000000000000000000000000000C0000003600000000003225000000000000000000000',
    '00000000000000000000000000000700000090000003600000000003222500000000000000000000',
    '00000000000000000000000000007700000000000003600000000003222250000000000000000000',
    '00000000000000000000000000077700000000000003600000000003222260000000000000000000',
    '41111111111111111111111111111111111111111112600000000003222225000000041111111115',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
    '32222222222222222222222222222222222222222222600000000003222226000000032222222226',
]

#Definindo a tela e suas dimensões
WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AVIATOR PYDVENTURE')

width_block = WIDTH // 12
height_block = HEIGHT // 16

#Definindo uma função para realizar a tranformação de escala
def scale(sprite):
    transformed_sprite = pygame.transform.scale(sprite,(width_block, height_block))
    return transformed_sprite

#Definindo uma função para realizaar a transformação de escala das telas
def scaleMenu(sprite):
    transformed_sprite = pygame.transform.scale(sprite,(WIDTH,HEIGHT))
    return transformed_sprite

#Carregando imagens de menu
menu = pygame.image.load('Algoritmos/menu.jpg')
menu = scaleMenu(menu)

#Carregando imagens do tutorial
howtoplay = pygame.image.load('Algoritmos/howplaymenu.jpg')
howtoplay = scaleMenu(howtoplay)

#Carregando imagens da tela de derrota
defeat = pygame.image.load('Algoritmos/derrota.jpg')
defeat = scaleMenu(defeat)

#Carregando imagens da tela de vitoria
victory = pygame.image.load('Algoritmos/vitoria.jpg')
victory = scaleMenu(victory)

#Carregando botões
continue_button = pygame.image.load('Algoritmos/continue.png')
howplay = pygame.image.load('Algoritmos/howplay.png')
start_button = pygame.image.load('Algoritmos/play.png')
quit = pygame.image.load('Algoritmos/sair.png')

#Sprite do aviso
notice = pygame.image.load('Algoritmos/notice.png')
ammo_notice = pygame.image.load('Algoritmos/aviator/ammo.png')
face_aviator = pygame.image.load('Algoritmos/aviator/aviator_face.png')

#Sprites do chão
generic_grass = pygame.image.load('Algoritmos/land/Generic Grass 1.png')
generic_grass = scale(generic_grass)

#Sprites das laterais
lateral_ground = pygame.image.load('Algoritmos/land/lateral_ground.png')
lateral_ground = scale(lateral_ground)
lateral_ground_inverted = pygame.transform.flip(lateral_ground, True, False)

#Sprites da terra
corner_ground = pygame.image.load('Algoritmos/land/canto.png')
corner_ground = scale(corner_ground)
corner_ground_inverted = pygame.transform.flip(corner_ground, True, False)

#Sprites das nuvens
big_cloud = pygame.image.load('Algoritmos/clouds/bg_cloud6.png')
medium_cloud = pygame.image.load('Algoritmos/clouds/bg_cloud2.png')
small_cloud = pygame.image.load('Algoritmos/clouds/bg_cloud5.png')
small_cloud2 = pygame.image.load('Algoritmos/clouds/bg_cloud7.png')
small_cloud3 = pygame.image.load('Algoritmos/clouds/bg_cloud8.png')
small_cloud4 = pygame.image.load('Algoritmos/clouds/bg_cloud01.png')

#Sprites do cenario
houses = pygame.image.load('Algoritmos/village/houses.png')
small_box = pygame.image.load('Algoritmos/village/small_box.png')
big_box = pygame.image.load('Algoritmos/village/Big_box.png')
tiles = pygame.image.load('Algoritmos/land/tile.png')
helicopter = pygame.image.load('Algoritmos/aviator/helicopter.png')

#Sprites das gramas
grass = pygame.image.load('Algoritmos/land/mato.png')
grass = pygame.transform.scale(grass,(192,24))

land = pygame.image.load('Algoritmos/land/ground_2.png')
land = scale(land)

#Sprite do avião 
crashed_plane = pygame.image.load('Algoritmos/aviator/crash_plane.png')
crashed_plane = pygame.transform.scale(crashed_plane,(705,75))

#Carregando soundtracks
game_soundtrack = pygame.mixer.Sound('Algoritmos/audios/game.wav')
jump = pygame.mixer.Sound('Algoritmos/audios/jump.wav')
fire = pygame.mixer.Sound('Algoritmos/audios/fire.wav')
death = pygame.mixer.Sound('Algoritmos/audios/death.wav')
click = pygame.mixer.Sound('Algoritmos/audios/click.wav')
hit = pygame.mixer.Sound('Algoritmos/audios/hit.wav')
chest = pygame.mixer.Sound('Algoritmos/audios/chest.wav')
victory_sound = pygame.mixer.Sound('Algoritmos/audios/victory.wav')
explosion = pygame.mixer.Sound('Algoritmos/audios/explosion.wav')
soundtrack = pygame.mixer.music.load('Algoritmos/audios/menu.ogg')
pygame.mixer.music.play(-1)

class Aviator(pygame.sprite.Sprite):

    #Carregando as sprites para realizar a animação
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_1.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_2.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_3.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_4.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_5.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/run_6.png'))

        self.sprites.append(pygame.image.load('Algoritmos/aviator/look_1.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/look_2.gif'))

        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile000.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile001.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile002.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile003.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile004.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile005.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile006.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile007.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile008.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile009.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile010.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile011.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile012.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile013.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile014.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile015.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile016.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile017.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile018.png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/jump/tile019.png'))

        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_1.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_2.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_3.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_4.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_5.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_6.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_7.gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/walk/walk_8.gif'))

        self.sprites.append(pygame.image.load('Algoritmos/aviator/slide/slide_1 (1).png'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/slide/slide_1 (2).png'))

        #Animar e parar
        self.is_running = False
        self.is_stopped = False

        #Endereço da sprite a ser animada
        self.current = 0
        self.image = self.sprites[self.current]

        #Inversão da sprite e redimensionamento
        self.inverted_sprite = pygame.transform.flip(self.image, True, False)
        self.is_inverted = False
        self.image = pygame.transform.scale(self.image, (39, 51))

        #Gravidade e força setada
        self.gravity = 0.3
        self.gravity_velocity = 0

        self.is_walking = False
        self.walking_active = 0
        self.can_walk = True

        self.slide = False

        self.jumper = False
        self.jump_limit = -120
        self.jump_max = False
        self.jumps_count = 0 

        #Atribuindo um retangulo a sprite
        self.rect = self.image.get_rect()
        self.rect.center = 196,544    

        #Posicao do menininho
        self.aviator_position = 0
        self.aviator_current_position = list(self.rect.center)

        self.direction_bullet = 1
    
    #Definindo os movimentos
    def movements(self):
        key = pygame.key.get_pressed()
        if self.can_walk:    
            if key[K_d]:
                self.direction_bullet = 1
                if key[K_s]:
                    self.slide = True
                    self.is_running = True
                    self.is_inverted = False
                    if self.is_walking:
                        self.slide = False
                        self.aviator_current_position[0] += 2

                    else:        
                        self.aviator_current_position[0] += 10              
                            
                else:
                    self.slide = False
                    self.is_running = True
                    self.is_inverted = False
                    if self.is_walking:
                        self.aviator_current_position[0] += 2

                    else:        
                        self.aviator_current_position[0] += 6     

            elif key[K_a]:
                self.direction_bullet = -1
                if key[K_s]:
                    self.slide = True
                    self.is_running = True
                    self.is_inverted = True
                    if self.is_walking:
                        self.slide = False
                        self.aviator_current_position[0] -= -2
                    
                    else:
                        self.aviator_current_position[0] -= 10
                        
                else:
                    self.slide = False
                    self.is_running = True
                    self.is_inverted = True
                    if self.is_walking:
                        self.aviator_current_position[0] -= 2
                
                    else:
                        self.aviator_current_position[0] -= 6

            else:
                self.is_running = False
                self.slide = False

    #Alternando entre andar e correr        
    def walking (self):
        self.is_walking = True
        self.walking_active += 1
        if self.walking_active > 1:
            self.is_walking = False
            self.walking_active = 0

    #Definindo mecanica de pulo
    def jump(self):
        if self.jumps_count < 2:
            jump.play()
            self.jumps_count += 1
            self.jumper = True
            self.gravity_velocity= -8
            self.aviator_current_position[1] += self.gravity_velocity

        else:
            self.jumper = False

    #Controlando colisões        
    def collision(self,group):
        if self.aviator_current_position[0] <= 0 or self.aviator_current_position[0] >= 4234:
            self.not_moving()

        inicial_position = self.rect.center
        self.rect.center = self.aviator_current_position
        if not pygame.sprite.spritecollide(self,lands,False):
            self.moving()

        else:
            self.jumper = False
            self.rect.center = inicial_position
            self.gravity_velocity = 0
            self.not_moving()
            self.jump_max = False
            self.jumps_count -= 2
            if self.jumps_count < 0:
                self.jumps_count = 0

    
    def moving(self):
        self.rect.center = self.aviator_current_position

    def not_moving(self):
        self.aviator_current_position = list(self.rect.center)

    #Atualização de sprites (animação)
    def update(self):

        self.gravity_velocity += self.gravity
        self.aviator_current_position[0] += self.aviator_position
        self.aviator_current_position[1] += self.gravity_velocity


        if self.gravity_velocity >= self.jump_limit:
            self.jump_max = True
            self.gravity_velocity += self.gravity

        if self.slide:
            self.current += 1
            if self.current >= 37 or self.current < 36:
                self.current = 36

        elif self.jumper:
            #Animação durante o pulo
            self.current += 0.1
            if self.current >= 16 or self.current < 8:
                self.current = 8
           

        elif self.is_running and self.is_walking:
            #A//nimação durante a caminhada
            self.current += 0.2
            if self.current >= 35 or self.current < 28:
                self.current = 28

        elif self.is_running:
            #Animação durante a corrida
            self.current += 0.3
            if self.current >=5:
                self.current = 0

        else:
            #Sprite parada
            self.current += 0.01
            if self.current >= 7 or self.current < 6:
                self.current = 6
           

        self.image = self.sprites[int(self.current)]
        self.image = pygame.transform.scale(self.image, (39, 51))

        if self.is_inverted:
            self.image = pygame.transform.flip(self.image, True, False)

class Boss(pygame.sprite.Sprite):
    #Carregando sprites para animar o final boss
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (2).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (7).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (8).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (9).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (10).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (11).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (12).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (13).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (14).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (15).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (16).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (17).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (18).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (19).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (20).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/final_boss (21).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (7).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (8).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (9).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (10).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bossatk (11).gif'))
        
        #Alternando entre as sprites
        self.current = 0
        self.image = self.sprites[self.current]

        #Invertendo a imagem, caso necessário
        self.inverted_sprite = pygame.transform.flip(self.image, True, False)
        self.is_inverted = False

        #Atribuindo um retangulo à sprite e definindo sua localização
        self.rect = self.image.get_rect()
        self.rect.center = x,530 #2352  455 ---32 20
        self.velocity_x = 7
        self.x = x
        self.direction = 1

        self.can_walk = True

    #Atualização de sprites (animação)
    def update(self):
        if self.can_walk:
            self.current += 0.3
            if self.current > 20:
                self.current = 0

        elif self.can_walk == False:
            self.current += 0.3
            if self.current >= 30 or self.current < 21:
                self.current = 21
    
        self.image = self.sprites[int(self.current)]
        if self.is_inverted:
            self.image = pygame.transform.flip(self.image, True, False)

class Carnivore(pygame.sprite.Sprite):
    #Carregando as sprites
    def __init__(self,lin,col):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (2).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/plant (7).gif'))

        #Alternando entre as sprites
        self.current = 0
        self.image = self.sprites[self.current]

        #Definindo intervalo de ataque
        self.thorn_attack = False

        #Atribuindo um retangulo à sprite e definindo sua localização
        self.rect = self.image.get_rect()

        x = col * width_block + 40
        y = lin * width_block - 360

        self.rect.center = x,y 

    #Atualização de sprites (animação)
    def update(self):
        self.thorn_attack = False
        self.current += 0.1
        if self.current > 6:
            self.thorn_attack = True
            self.current = 0
            if carnivore_life <= 0:
                self.thorn_attack = False
    
        self.image = self.sprites[int(self.current)]

class Bee(pygame.sprite.Sprite):
    #Carregando as sprites
    def __init__(self,lin,col):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (2).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (7).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (8).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (9).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (10).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/bee (11).gif'))

        #Alternando entre as sprites
        self.current = 0
        self.image = self.sprites[self.current]

        #Atribuindo um retangulo à sprite e definindo sua localização
        self.rect = self.image.get_rect()

        x = col * width_block
        y = lin * height_block

        self.rect.center = x,y

    #Atualização de sprites (animação)
    def update(self):
        self.current += 0.3
        if self.current > 10:
            self.current = 0

        self.image = self.sprites[int(self.current)]
        self.image = pygame.transform.flip(self.image, True, False)
    
class Robot(pygame.sprite.Sprite):
    #Carregando as sprites
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (2).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/enemys/enemy (7).gif'))
        
        #Alternando entre as sprites
        self.current = 0
        self.image = self.sprites[self.current]

        #Invertendo a sprite, case necessário
        self.inverted_sprite = pygame.transform.flip(self.image, True, False)
        self.is_inverted = False

        #Atribuindo um retangulo à sprite e definindo sua localização
        self.rect = self.image.get_rect()
        self.rect.center = x,540 #2352  455 ---32 20
        self.velocity_x = 5
        self.x = x
        self.direction = 1

        self.can_walk = True

    #Atualização de sprites (animação)
    def update(self):
        self.current += 0.3
        if self.current > 7:
            self.current = 0

    
        self.image = self.sprites[int(self.current)]
        if self.is_inverted:
            self.image = pygame.transform.flip(self.image, True, False)

class Chest (pygame.sprite.Sprite):
    #Carregando as sprites
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (1).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (2).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (3).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (4).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (5).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (6).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (7).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (8).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (9).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (10).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (11).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (12).gif'))
        self.sprites.append(pygame.image.load('Algoritmos/aviator/Chest/chest (13).gif'))

        #Alternando entre as sprites
        self.current = 0
        self.image = self.sprites[self.current]

        #Atribuindo um retangulo à sprite e definindo sua localização
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        #Sinalizando se o báu ja foi aberto
        self.is_opened = False

    #Atualização de sprites (animação)
    def update(self):
        if self.is_opened:
            self.current += 1
            if self.current >= 12:
                self.current = 12
        else:
            self.current = 0

        self.image = self.sprites[int(self.current)]

class Thorn(pygame.sprite.Sprite):

    def __init__(self,person,direction):
        #Carregando a sprite e atribuindo a ela um retangulo
        super().__init__()
        self.image = pygame.image.load('Algoritmos/enemys/espinho.gif')
        self.rect = pygame.Rect(person.rect.center,(22,14))

        #Velocidade e direção dos projéteis
        self.velocity = 10
        self.direction = direction

    #Atualização de sprites (animação)
    def update(self):
        self.rect.x += self.velocity * self.direction

class Bullet(pygame.sprite.Sprite):
    #Carregando a sprite e atribuindo a ela um retangulo
    def __init__(self,person,direction):
        super().__init__()
        self.image = pygame.image.load('Algoritmos/aviator/ammo.png')
        self.image = pygame.transform.scale(ammo_notice, (15,10))
        self.rect = pygame.Rect(person.rect.center,(15,10))

        #Sinalizando colisões
        self.collide = False

        #Sinalizando se existe munição disponivel
        self.ammo_avaible = True

        #Velocidade e direção dos projéteis
        self.velocity = 10
        self.direction = direction

    #Atualização de sprites (animação)
    def update(self):
        self.rect.x += self.velocity * self.direction
            
        if ammo_available <= 0:
            self.ammo_avaible = False
        
class Camera:
    #Criando um range de visão
    def __init__(self, size, position):
        self.window = pygame.Rect (position, size)
        self.position = position
        self.slide_x = 0
        self.slide_y = 0
        self.fill_image = pygame.Surface(self.window.size)
        self.fill_image.fill((95, 205, 228))
        self.scene_draw = pygame.Surface(self.window.size)


    def player_view(self, rect):
        return self.window.colliderect(rect)
    
    #Definindo as posições do range de visão (aviador)
    def moving (self, position):
        self.window.center = position
        self.slide_x = self.window.x
        self.slide_y = self.window.y

    #Limpa a tela de fundo
    def scene_screen(self): 
        self.scene_draw.blit(self.fill_image, (0,0))

    #Desenha a "camera"
    def draw(self, screen): 
        screen.blit(self.scene_draw, self.position)
        pygame.draw.rect(screen, (0,0,0), (self.position, self.window.size), 1)
        
    #Desenha as sprites no cenário
    def sprites_draw(self, group):
        #Cenário
        self.scene_draw.blit(crashed_plane, (0 - self.slide_x, 500- self.slide_y))
        self.scene_draw.blit(big_cloud,(114 - self.slide_x, 200- self.slide_y))
        self.scene_draw.blit(notice, (210 - self.slide_x, 350 - self.slide_y))
        self.scene_draw.blit(medium_cloud,(888 - self.slide_x, 350- self.slide_y))
        self.scene_draw.blit(small_cloud,(644 - self.slide_x, 200- self.slide_y))
        self.scene_draw.blit(small_cloud3,(1400 - self.slide_x, 400- self.slide_y))
        self.scene_draw.blit(small_cloud4,(1500 - self.slide_x, 200- self.slide_y))
       # self.scene_draw.blit(small_cloud,(1650 - self.slide_x, 380- self.slide_y))

        self.scene_draw.blit(small_cloud,(2350 - self.slide_x, 180- self.slide_y))
        self.scene_draw.blit(big_cloud,(1700 - self.slide_x, 170- self.slide_y))
        self.scene_draw.blit(small_cloud3,(2300 - self.slide_x, 150- self.slide_y))
        self.scene_draw.blit(small_cloud4,(2600 - self.slide_x, 100- self.slide_y))

        self.scene_draw.blit(small_cloud,(3850 - self.slide_x, 180- self.slide_y))
        self.scene_draw.blit(big_cloud,(3100 - self.slide_x, -20 - self.slide_y))
        self.scene_draw.blit(small_cloud3,(3500 - self.slide_x, 290- self.slide_y))
        self.scene_draw.blit(small_cloud4,(3790 - self.slide_x, 250- self.slide_y))

        self.scene_draw.blit(helicopter,(4100 - self.slide_x, 517- self.slide_y))

        self.scene_draw.blit(houses,(688 - self.slide_x, 189- self.slide_y))
        self.scene_draw.blit(grass,(514 - self.slide_x, 547- self.slide_y))

        for sprite in group:
            if self.player_view(sprite.rect):
                self.scene_draw.blit(sprite.image, (sprite.rect.x - self.slide_x, sprite.rect.y - self.slide_y))
                           
class Land(pygame.sprite.Sprite):
    #Carregando as sprites
    def __init__(self, line, col, current,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(generic_grass)
        self.sprites.append(land)
        self.sprites.append(lateral_ground)
        self.sprites.append(lateral_ground_inverted)
        self.sprites.append(corner_ground)
        self.sprites.append(corner_ground_inverted)
        self.sprites.append(grass)
        self.sprites.append(small_box)
        self.sprites.append(tiles)
        self.image = self.sprites[current]

        #Atribuindo suas posições
        x = col * width_block
        y = line * height_block
        
        #Atribuindo um retangulo às sprites
        self.rect = pygame.Rect((x,y),(width,height))    

#Criando grupos para diferentes sprites
thorns = pygame.sprite.Group()        
lands = pygame.sprite.Group()
hero = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bees = pygame.sprite.Group()
enemys = pygame.sprite.Group()
carnivore = pygame.sprite.Group()
chests1 = pygame.sprite.Group()
chests2 = pygame.sprite.Group()

#Criando variáveis para utilizar as classes
aviator = Aviator()
boss = Boss(4090)
enemy = Robot(1632)
chest1 = Chest(1943,470)
chest2 = Chest(3391,200)
bullet = Bullet(aviator,aviator.direction_bullet)

#Adicionando classes em grupos 
hero.add(aviator)
boss_group.add(boss)
enemys.add(enemy)
chests1.add(chest1)
chests2.add(chest2)

#Definindo a vida de cada mob
boss_life = 20
bees_life = 2
carnivore_life = 2
enemys_life = 2

#Configurando estilo de texto
font = pygame.font.SysFont('arial', 14, True, False)

#Definindo a vida e munição disponível do aviador
ammo_available = 10
life_count = 12

#Strings de representação
life_string = '█'
pause = '(P) para pausar'


#Configurando funcionalidade dos botões (buttons.py)
button = pygame.sprite.Group()

start_defeat = buttons.Buttons(240,280,start_button)
quit_button_defeat = buttons.Buttons(240,360,quit)
start_victory = buttons.Buttons(240,280,start_button)
quit_button_victory = buttons.Buttons(240,360,quit)
start = buttons.Buttons(330,230,start_button)
howplay = buttons.Buttons(330,310,howplay)
quit_button = buttons.Buttons(330,390,quit)
continue_option = buttons.Buttons(330,230,continue_button)

#Adicionando os botões em um grupo
button.add(continue_option)
button.add(start)
button.add(start_defeat)
button.add(start_victory)
button.add(howplay)
button.add(quit_button)
button.add(quit_button_defeat)
button.add(quit_button_victory)

#Definindo dimensões da camera
camera = Camera((WIDTH, HEIGHT), (0,0))


#Definindo função para representação de objetos
def sprites_add(lin,col,idx,w=width_block,h=height_block):
    ground = Land(lin,col,idx,w,h)
    return lands.add(ground)

#Atribuindo certa sprite para cada char presente na matriz
for lin, line in enumerate(mat):
    for col, char in enumerate(line):
        if char == '1':
            sprites_add(lin,col,0)
        if char == '2':
            sprites_add(lin,col,1)
        if char == '3':
            sprites_add(lin,col,2)
        if char == '4':
            sprites_add(lin,col,4)
        if char == '5':
            sprites_add(lin,col,5)
        if char == '6':
            sprites_add(lin,col,3)
        if char == '7':
            sprites_add(lin,col,7)
        if char == '8':
            bee = Bee(lin,col)
            bees.add(bee)
        if char == '9':
            sprites_add(lin,col,8,96)
        if char == 'C':
            carnivore_plant = Carnivore(lin,col)
            carnivore.add(carnivore_plant)
            thorn = Thorn(carnivore_plant, -1)
            thorns.add(thorn)

#Sinalizando telas
main_menu = True
play = False
howtoplay_check = False
pause_check = False
flag_pause = False

#Clock (fps)
clock = pygame.time.Clock()

run = True

#Laço do jogo
while run:
    #Tela de menu
    if main_menu:
        game_soundtrack.stop()
        pygame.mixer.music.unpause()
        screen.blit(menu,(0,0))

        if start.draw(screen):
            click.play()
            main_menu = False
            pygame.mixer.music.pause()
            game_soundtrack.play(-1)
            game_soundtrack.set_volume(0.2)

        if howplay.draw(screen):
            click.play()
            howtoplay_check = True
            main_menu = False

        if quit_button.draw(screen):
            run = False

    #Tela de pause
    elif pause_check:
        flag_pause = True
        screen.blit(menu,(0,0))
        if continue_option.draw(screen):
            click.play()
            pause_check = False
        if howplay.draw(screen):
            click.play()
            howtoplay_check = True
            pause_check = False
        if quit_button.draw(screen):
            run = False

    #Tela de ajuda
    elif howtoplay_check:
        screen.blit(howtoplay,(0,0))
    
    #Tela do jogo
    elif life_count > 0 and boss_life > 0:
        clock.tick(60)
        
        ammo = f':{ammo_available}'
        life = f'{int(life_count)*life_string}'
        
        pause_instruction = f'{pause}'

        text_pause = font.render(pause_instruction, True, ((97,23,39)))
        text_ammo = font.render(ammo, True, ((0,0,0)))
        text_life = font.render(life, True,((255,0,0)))

        #Verificando comandos
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            elif event.type == KEYDOWN:
                if event.key == K_m:
                    aviator.walking()
                if event.key == K_SPACE or event.key == K_w:
                    aviator.jump()
                    jump.set_volume(0.5)
                if event.key == K_n:
                    if bullet.ammo_avaible:
                        bullet = Bullet(aviator, aviator.direction_bullet)
                        bullet_group.add(bullet)
                        ammo_available -= 1 
                        fire.play()
        
        #Verificando ataque da Carnivore
        if carnivore_plant.thorn_attack:
            thorn = Thorn(carnivore_plant, -1)
            thorns.add(thorn)

        #Desenhando cenário
        camera.scene_screen()
        camera.sprites_draw(lands) 

        if bullet.collide == False:
            camera.sprites_draw(bullet_group) 

        camera.sprites_draw(bees)
        camera.sprites_draw(chests1)
        camera.sprites_draw(chests2)
        camera.sprites_draw(thorns)
        camera.sprites_draw(carnivore) 
        camera.sprites_draw(enemys)
        camera.sprites_draw(boss_group)
        camera.sprites_draw(hero)  
        camera.draw(screen)
        aviator.collision(lands)
        aviator.movements()

        #Atualizando sprites
        hero.update() 
        bullet_group.update()
        carnivore.update()
        thorns.update()
        enemy.update()
        boss.update()
        chests1.update()
        chests2.update()
        bees.update()
        
        #Definindo direção de projéteis
        for shoot in bullet_group:
            if shoot.rect.centerx > aviator.rect.centerx + 320:
                shoot.kill()
            elif shoot.rect.centerx < aviator.rect.centerx - 320:
                shoot.kill()

        for shoot in thorns:
            if shoot.rect.centerx > aviator.rect.centerx + 320:
                shoot.kill()
            elif shoot.rect.centerx < aviator.rect.centerx - 320:
                shoot.kill()

        #Definindo direção dos mobs
        for enemy in enemys:
            if enemy.can_walk:
                enemy.rect.x += enemy.velocity_x * enemy.direction  # atualiza a coordenada x
                if enemy.rect.x >= (enemy.x + 600) or enemy.rect.x <= enemy.x - 50:
                    enemy.direction *= -1 
                    if enemy.rect.x >= (enemy.x + 600):
                        enemy.is_inverted = True
                    if enemy.rect.x <= enemy.x:
                        enemy.is_inverted = False

        for boss in boss_group:
            if boss.can_walk:
                boss.rect.x += boss.velocity_x * boss.direction  # atualiza a coordenada x
                if boss.rect.x >= (boss.x + 30) or boss.rect.x <= boss.x - 500:
                    boss.direction *= -1 
                    if boss.rect.x >= (boss.x + 30):
                        boss.is_inverted = False
                    if boss.rect.x <= boss.x:
                        boss.is_inverted = True
                
        #Definindo ponto central da camera       
        camera.moving(aviator.rect.center)

        #Desenhando informes do personagem 
        screen.blit(face_aviator, (0,0))
        screen.blit(text_life, (50,15))
        screen.blit(ammo_notice, (49,32))
        screen.blit(text_ammo, (70,36))
        screen.blit(text_pause, (520,10))

        #Verificando colisões
        if pygame.sprite.groupcollide(hero,enemys,False,False):
            enemy.can_walk = False
            hit.play()
            hit.set_volume(0.2)
            life_count -= 0.1
            if life_count <= 0:
                pygame.sprite.groupcollide(hero, enemys, True, False)
        else:
            enemy.can_walk = True

        if pygame.sprite.groupcollide(hero,chests1,False,False):
            if chest1.is_opened == False:
                chest.play()
            chest1.is_opened = True
            chest.set_volume(0.2)
            if chest1.is_opened and ammo_available <= 20:
                ammo_available += 5
                bullet.ammo_avaible = True
            if chest1.is_opened and life_count < 12:
                life_count += 4

        if pygame.sprite.groupcollide(hero,chests2,False,False):
            if chest2.is_opened == False:
                chest.play()
            chest2.is_opened = True
            chest.set_volume(0.2)
            if chest2.is_opened and ammo_available <= 20:
                ammo_available += 5
                bullet.ammo_avaible = True
            if chest2.is_opened and life_count < 12:
                life_count += 4

        if pygame.sprite.groupcollide(hero,boss_group,False,False):
            boss.can_walk = False
            life_count -= 0.2
            hit.play()
            hit.set_volume(0.2)
            if life_count <=0:
                pygame.sprite.groupcollide(hero,boss_group,True,False)
        else:
            boss.can_walk = True
        
        if pygame.sprite.groupcollide(bullet_group,boss_group,False,False):
            bullet.collide = True
            if boss_life <= 0:
                pygame.sprite.groupcollide(bullet_group,boss_group,True,True)
            boss_life -= 0.3

        if pygame.sprite.groupcollide(hero,bees,False,False):
            hit.play()
            hit.set_volume(0.2)
            if life_count <= 0:
                pygame.sprite.groupcollide(hero,bees,True,False)
            life_count -= 0.3

        if pygame.sprite.groupcollide(bullet_group,enemys,False,False):
            bullet.collide = True
            if enemys_life <= 0:
                explosion.play()
                pygame.sprite.groupcollide(bullet_group,enemys,True,True)
            enemys_life -= 0.1

        if pygame.sprite.groupcollide(bees,bullet_group,False,False):
            bullet.collide = True
            if bees_life <= 0:
                explosion.play()
                pygame.sprite.groupcollide(bullet_group,bees,True,True)
            bees_life -= 0.2

        if pygame.sprite.groupcollide(hero,carnivore,False,False):
            hit.play()
            hit.set_volume(0.2)
            if life_count <= 0:
                pygame.sprite.groupcollide(carnivore,hero,False,True)
            life_count -= 0.3

        if pygame.sprite.groupcollide(hero,thorns,False,False):
            hit.play()
            hit.set_volume(0.2)
            if life_count <= 0:
                pygame.sprite.groupcollide(thorns,hero,True,True)
            life_count -= 0.5

        if pygame.sprite.groupcollide(bullet_group,carnivore,False,False):
            bullet.collide = True
            if carnivore_life <= 0:
                explosion.play()
                carnivore_plant.thorn_attack = False
                pygame.sprite.groupcollide(bullet_group,carnivore,True,True)
            carnivore_life -= 0.1

        pygame.sprite.groupcollide(bullet_group,lands, True, False)

        #Verificando queda
        if aviator.rect.y >= 831:
            life_count = 0
        
       
    #Verificando condições de vitória/derrota
    elif boss_life <= 0:
        screen.blit(victory,(0,0))
        victory_sound.play()
        if quit_button_victory.draw(screen):
            run = False
    else:
        screen.blit(defeat,(0,0))
        death.play()
        if quit_button_defeat.draw(screen):
            run = False
    
    #Verificando comandos
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:
            if event.key == K_v:
                click.play()
                if howtoplay_check:
                    if flag_pause:
                        howtoplay_check = False
                        pause_check = True
                    else:
                        howtoplay_check = False
                        main_menu = True

            if event.key == K_p:
                click.play()
                pause_check = True
                main_menu = False

            if event.key == K_m:
                aviator.walking()

            if event.key == K_SPACE or event.key == K_w:
                aviator.jump()
                jump.set_volume(0.5)

            if event.key == K_n:
                if bullet.ammo_avaible:
                    bullet = Bullet(aviator, aviator.direction_bullet)
                    bullet_group.add(bullet)
                    ammo_available -= 1 
                    fire.play()

    #Atualização de tela     
    pygame.display.flip()

pygame.quit()