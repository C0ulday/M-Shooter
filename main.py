import math
import pygame
from jeu import Jeu
pygame.init()




WIDTH = 1000
HEIGHT = 472
fps = 60

#### AFFICHAGE
pygame.display.set_caption("M-Shooter")

# Background
background = pygame.image.load("assets/environnement/back.png")
sol = pygame.image.load("assets/environnement/tiles.png")

running = True

timer = pygame.time.Clock()
font = pygame.font.Font("assets/font/BPdots.otf")

class Player:
    def __init__(self):
        self.max_health = 100
        self.health = 100
        self.score = 0

# Le jeu

le_jeu = Jeu()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

while running :

    timer.tick(fps)
    screen.blit(background, (0,0))
    screen.blit(sol, (0,0))
   
    #le_jeu.all_zombies_sprites.draw(screen)
    #le_jeu.all_zombies_sprites.update(WIDTH,HEIGHT)

    le_jeu.viseur_sprites.update()
    le_jeu.viseur_sprites.draw(screen)

    le_jeu.aigles_sprites.draw(screen)
    le_jeu.aigles_sprites.update()
   
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()