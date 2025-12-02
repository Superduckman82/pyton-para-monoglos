import pygame
import sys

#pantalla

ancho = 800
alto = 800


ventana = pygame.display.set_mode((ancho, alto))
pygame.init()
clock = pygame.time.Clock()

#sprite 

pato = pygame.sprite.Sprite()
pato.image = pygame.image.load("pato.png").convert_alpha()
pato.rect = pygame.Rect(ancho/2, alto/2, 500, 500)
















def game():
    while True:
        clock.tick(60)

        ventana.blit(pato, pato.rect)





        pygame.display.update()       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()











game()






