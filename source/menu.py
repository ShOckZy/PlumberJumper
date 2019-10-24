import pygame,sys
import pygame
from pygame.locals import *
salir=False
blanco=(0,70,70)


def teclado():
    teclado = pygame.key.get_pressed()

    global salir
    global jugar

    if teclado[K_a]:
        action = juego()
    if teclado[K_s]:
            quit()
# Aqui va todo el codigo de Abdiel
        #juego():
def main():
    pygame.init()
    fuente1=pygame.font.SysFont("Arial",20,True,False)
    texto1=fuente1.render("Presiona A para iniciar el juego",0,(0,0,0))
    texto2=fuente1.render("Presiona S para salir",0,(0,0,0))

    pantalla=pygame.display.set_mode((1080, 720))
    imagen2=pygame.image.load("PI/inicioprueba.png")
    pygame.display.set_caption("Crazy Energy House")
    reloj1=pygame.time.Clock()
    global salir

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True

        reloj1.tick(20)
        pantalla.fill(blanco)
        pantalla.blit(imagen2,(0,0))
        pantalla.blit(texto1,(10,17))
        pantalla.blit(texto2,(10,0))
        teclado()
        pygame.display.update()

    pygame.quit()
main()
