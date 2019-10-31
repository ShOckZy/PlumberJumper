import pygame, sys
from pygame.locals import *
from source.classes import *

# Aqui se define la funcion principal
def main():
    pygame.init()
    eventos = pygame.event.get()
    fondo = pygame.image.load(principal.fondo)
    ventana = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("test")
    reloj = pygame.time.Clock()
    salir = False
    blanco=(0,70,70)

    def Teclado():
        evento = pygame.key.get_pressed()
        if evento[K_a]:
            quit()

    while salir!=True:
        reloj.tick(48)
        Teclado()
        ventana.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
        pygame.display.update()
    pygame.quit()

#La funcion principal es ejecutada aqui
main()
