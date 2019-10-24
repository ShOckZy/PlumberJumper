#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
 
# Constantes
top=True
arriba=True
movimiento=True
WIDTH = 1080
HEIGHT = 720
MposX =10
MposY = 520
movimientomenos=False
posX = 10
posY=10
cont=10
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}
#===========================================================

#=================Imagenes====================================
Bala = pygame.image.load("bala1.png")
fondo = pygame.image.load("fondoinicio.png")
burbuja = pygame.image.load("burbuja/burbuja1.png")
#================================================================
#======================Enemigo===================================  
def enemigo():
    global posX
    global movimiento
    if (movimiento == True ):
        if(posX <=1000):
            posX+=3
        else:
            movimiento=False
    if (movimiento==False):
        if (posX>=10):
                posX-=3
        elif (posX<10):
          movimiento=True
    return 
#================================================================
#======================BALA======================================
    

#======================TECLADO===================================
#================================================================
def teclado():
    teclado = pygame.key.get_pressed()
     
    global MposX,MposY
    global cont, direc
   
    
    if teclado[K_RIGHT]:
        if MposX <=1000:
            MposX+=3
            cont+=1
            direc=True
    elif teclado[K_LEFT]:
        if MposX >0:
            MposX-=3
            cont+=1
            direc=False
    elif teclado[K_q]:
        if  arriba == True:
            MposY-=30

    return
   
#===================SPRITE===============================
#========================================================
def sprite():
 
    global cont
 
    xixf[0]=(0,0,70,100)
    xixf[1]=(100,0,73,100)
    xixf[2]=(200,0,76,100)
    xixf[3]=(300,0,79,100)

    Rxixf[0]=(300,0,79,100)
    Rxixf[1]=(200,0,76,100)
    Rxixf[2]=(100,0,73,100)
    Rxixf[3]=(0,0,70,100)
 
   
    p=8
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
        cont=0
   
    return
 

def main(): 
    pygame.init() 

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump")
   
 
       
    plomero = pygame.image.load("plomero/plomero.png")  
    
    plomero_inv=pygame.transform.flip(plomero,True,False);
     
    clock = pygame.time.Clock()
   
 
    # el bucle principal del juego
    while True:
       
        time = clock.tick(60)
        pygame.display.flip()       
       
        sprite()
        teclado()
        enemigo()       
        screen.blit(fondo, (0, 0))
        if (top==True):
            screen.blit(Bala, (0,700))

        if (movimiento==True):
            screen.blit(burbuja, (posX, 50))
      
        if (movimiento==False):
            screen.blit(burbuja, (posX, 50))
      
        if direc==True:
            screen.blit(plomero, ( MposX, MposY),(xixf[i]))
            
        if direc==False:
            screen.blit(plomero_inv, ( MposX, MposY),(Rxixf[i]))
   
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    return 0
 
 
 
 
if __name__ == '__main__':
    main()