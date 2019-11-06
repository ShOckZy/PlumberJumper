import pygame,sys
from pygame.locals import *
from Tkconstants import FALSE

pygame.init()
menu = pygame.image.load("menu/iniciosinbotones.png")
icon_surf = pygame.image.load("icon.png")
botonjugar = pygame.image.load("menu/botonjugar.png")
botonjugar2 = pygame.image.load("menu/botonjugar2.png")
botonsalir = pygame.image.load("menu/botonsalir.png")
botonsalir2 = pygame.image.load("menu/botonsalir2.png")
botonajustes = pygame.image.load("menu/botonajustes.png")
botonajustes2 = pygame.image.load("menu/botonajustes2.png")
clic = pygame.mixer.Sound("sonidos/clic.ogg")
sonidofondo = pygame.mixer.music.load("sonidos/fondo.mp3")
bala = pygame.image.load("nivel1/arma.png")
reloj = pygame.time.Clock()
aux=1
NEGRO = (0,0,0)

MposX=20
MposY=460

cont=6
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}

parabola={}
salto = False
 
salto_Par=False

pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.25)
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert_alpha()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def teclado():
    teclado = pygame.key.get_pressed()

    global MposX
    global cont, direc,salto, salto_Par
    
    if teclado[K_SPACE] and teclado[K_RIGHT] and salto_Par==False:
        salto_Par=True
    elif teclado[K_SPACE] and teclado[K_LEFT] and salto_Par==False:
        salto_Par=True

    elif teclado[K_RIGHT]and salto==False and salto_Par==False:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]and salto==False and salto_Par==False:
        MposX-=2
        cont+=1
        direc=False
    elif teclado[K_SPACE] and salto==False and salto_Par==False:
        salto=True
    else :
         cont=6

    return
def sprite():

    global cont

    xixf[0]=(190,0,150,159)
    xixf[1]=(30,0,140,159)
    xixf[2]=(190,0,150,159)
    xixf[3]=(350,0,450,159)

    Rxixf[0]=(210,0,150,159)
    Rxixf[1]=(370,0,460,159)
    Rxixf[2]=(210,0,150,159)
    Rxixf[3]=(50,0,150,159)

    p=6

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
class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.sheet = pygame.image.load("nivel1/proyectil.png")
        self.image = bala
        self.rect=self.image.get_rect()


    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x += 5
        screen.blit(self.image,self.rect)

class Boton(pygame.sprite.Sprite):
    def __init__(self,botonjugar,botonjugar2,x=360,y=300):
        self.imagen_normal=botonjugar
        self.imagen_seleccion=botonjugar2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        screen.blit(self.imagen_actual,self.rect)

class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

def main():
    pygame.init()
    pygame.mixer.music.set_volume(.25)
    pygame.display.set_caption("Plumber Jumper")
    screen = pygame.display.set_mode((1080,720)) 
    pygame.display.set_icon(icon_surf)
    cursor1=cursor()

    boton1=Boton(botonjugar,botonjugar2,360,300)
    boton2=Boton(botonsalir,botonsalir2,360,450)
    boton3=Boton(botonajustes,botonajustes2,50,570)

    #LOOP PRINCIPAL
    while True:
        screen.blit(menu,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    Menujugar()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pygame.quit()
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    Ajustes()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        cursor1.update()
        #movement = pygame.mouse.get_pos()
        #print (movement)
        print (event)
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
        reloj.tick(30)        
def Ajustes():
    pygame.init()

    fondo=pygame.image.load("menuopciones/menuopciones.png")
    botonregresar = pygame.image.load("menujugar/botonregresar.png")
    botonregresar2 = pygame.image.load("menujugar/botonregresar2.png")
    espanol=pygame.image.load("menuopciones/espanol.png")
    espanol2=pygame.image.load("menuopciones/espanol2.png")
    ingles=pygame.image.load("menuopciones/ingles.png")
    ingles2=pygame.image.load("menuopciones/ingles2.png")
    sonidosi=pygame.image.load("menuopciones/sonidosi.png")
    sonidosi2=pygame.image.load("menuopciones/sonidosi2.png")
    sonidono=pygame.image.load("menuopciones/sonidono.png")
    sonidono2=pygame.image.load("menuopciones/sonidono2.png")

    pygame.display.set_caption("Ajustes")
    screen = pygame.display.set_mode((1080,720))
    reloj=pygame.time.Clock()
    cursor1=cursor()
    
    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(espanol,espanol2,430,240)
    boton3=Boton(ingles,ingles2,600,240)
    boton4=Boton(sonidosi,sonidosi2,430,380)
    boton5=Boton(sonidono,sonidono2,600,380)
    boton6=Boton(sonidosi,sonidosi2,430,525)
    boton7=Boton(sonidono,sonidono2,600,525)

    while True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton5.rect):
                    clic.play()
                    clic.set_volume(0)
                if cursor1.colliderect(boton4.rect):
                    clic.play()
                    clic.set_volume(1)
                if cursor1.colliderect(boton6.rect):
                    clic.play()
                    pygame.mixer.music.set_volume(.25)
                if cursor1.colliderect(boton7.rect):
                    clic.play()
                    pygame.mixer.music.set_volume(0)
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
                
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)
        boton5.update(screen,cursor1)
        boton6.update(screen,cursor1)
        boton7.update(screen,cursor1)

        cursor1.update()
        print (event)
        reloj.tick(30)        
        pygame.display.update()


    


def Menujugar():
    
    menujugar = pygame.image.load("menujugar/menujugar.png")
    botonregresar = pygame.image.load("menujugar/botonregresar.png")
    botonregresar2 = pygame.image.load("menujugar/botonregresar2.png")
    miniaturalvl1 = pygame.image.load("menujugar/miniaturalvl1.png")
    miniaturalvl12 = pygame.image.load("menujugar/miniaturalvl1_2.png")
    miniaturalvl2 = pygame.image.load("menujugar/miniaturalvl2.png")
    miniaturalvl22 = pygame.image.load("menujugar/miniaturalvl2_2.png")
    miniaturalvl3 = pygame.image.load("menujugar/miniaturalvl3.png")
    miniaturalvl32 = pygame.image.load("menujugar/miniaturalvl3_2.png")

    cursor1=cursor()

    pygame.init()
    pygame.display.set_caption("Plumber Jumper")
    screen=pygame.display.set_mode((1080,720))

    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(miniaturalvl1,miniaturalvl12,25,220)
    boton3=Boton(miniaturalvl2,miniaturalvl22,378,220)
    boton4=Boton(miniaturalvl3,miniaturalvl32,730,220)

    reloj=pygame.time.Clock()


    while True:
        screen.blit(menujugar,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    nivel1()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)

        print (event)
        reloj.tick(20)
        cursor1.update()
        pygame.display.update()

def nivel1():
    pygame.init()
    fondo = pygame.image.load("nivel1/nivel1.png")
    barravidapersonaje = pygame.image.load("nivel1/barravidapersonaje.png")     
    barraagua = pygame.image.load("nivel1/barraporcentajeagua.png")
    barratubos = pygame.image.load("nivel1/barratubos.png")
    barraenemigo = pygame.image.load("nivel1/barravidaenemigo.png")
    llavedeagua = pygame.image.load("nivel1/llavedeagua.png")
    
    botonpausa = pygame.image.load("pausa/botonpausa.png")
    botonpausa2 = pygame.image.load("pausa/botonpausa2.png")
    
    agua75= pygame.image.load("nivel1/agua75porciento.png")
    #plomero = pygame.image.load("nivel1/sprite_plomero0inver.png")

    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: Nivel 1")

    #Sprite
    plom = imagen("personajes/plomero/plomeroninja.png",True)
    plom_inv=pygame.transform.flip(plom,True,False);
    #Finsprite

    #Salto
    global salto_Par  
    bajada=False
    bajada_Par=False
    #Finsalto

    reloj1=pygame.time.Clock()

    boton1=Boton(botonpausa,botonpausa2,980,10)

    proyectil = Proyectil()

    cursor1=cursor()
    pygame.mixer.music.set_volume(0)

    lista_proyectiles=pygame.sprite.Group()

    movimientobala=False

    while True:
        sprite()
        teclado()

        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(10,20))
        screen.blit(barraagua,(10,100))
        screen.blit(barratubos,(10,185))
        screen.blit(barraenemigo,(832,80))

        screen.blit(llavedeagua,(970,510))
        #if direc==True:
         #   screen.blit(plom, ( MposX, MposY),(xixf[i]))
        #if direc==False:
         #   screen.blit(plom_inv, ( MposX, MposY),(Rxixf[i]))

        #Movimiento sin salto
        global MposX,MposY,salto
       
        if direc==True and salto==False:
            screen.blit(plom, ( MposX, MposY),(xixf[i]))
   
        if direc==False and salto==False:
            screen.blit(plom_inv, ( MposX, MposY),(Rxixf[i]))
       
       
       #salto normal
        if salto==True and movimientobala==False:            
           
            if direc==True and movimientobala==False:
                screen.blit(plom, ( MposX, MposY),(xixf[2]))
            if direc==False and movimientobala==False:
                screen.blit(plom_inv, ( MposX, MposY),(Rxixf[2]))  
           
            if bajada==False:
                MposY-=4
               
            if bajada==True:
                MposY+=4              
           
            if MposY==340:
                bajada=True
           
            if MposY==460:
                bajada=False
                salto=False
      

        #SALTO PARABOLICO
        if salto_Par==True and direc==True and movimientobala==False:            
           
            screen.blit(plom, ( MposX, MposY),(xixf[2]))
           
            if bajada_Par==False:
                MposY-=3
                MposX+=2
               
            if bajada_Par==True:
                MposY+=3
                MposX+=2
           
            if MposY==340:
                bajada_Par=True
           
            if MposY==460:
                bajada_Par=False
                salto_Par=False
        elif salto_Par==True and direc==FALSE and movimientobala==False:            
           
            screen.blit(plom_inv, ( MposX, MposY),(Rxixf[2]))
           
            if bajada_Par==False:
                MposY-=3
                MposX-=2
               
            if bajada_Par==True:
                MposY+=3
                MposX-=2
           
            if MposY==340:
                bajada_Par=True
           
            if MposY==460:
                bajada_Par=False
                salto_Par=False
        if movimientobala==True:
            screen.blit(plom, ( MposX, MposY),(xixf[1]))
            movimientobala=False
        #Fin salto
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa()
                if event.key == pygame.K_x:
                    movimientobala=True
                    proyectil = Proyectil()
                    proyectil.rect.x= MposX+50
                    proyectil.rect.y= MposY+80
                    lista_proyectiles.add(proyectil)

            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    pausa()
        #proyectil.update(screen)
        lista_proyectiles.update(screen)
        #print (event)
        boton1.update(screen,cursor1)
        reloj1.tick(100)
        cursor1.update()
        pygame.display.update()
def pausa():
    pausado = True
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("nivel1/nivel1.png")
    
    fondopausa = pygame.image.load("pausa/fondopausa.png")
    botoninicio = pygame.image.load("pausa/botoninicio.png")
    botoninicio2 = pygame.image.load("pausa/botoninicio2.png")
    botonplay = pygame.image.load("pausa/botonplay.png")
    botonplay2 = pygame.image.load("pausa/botonplay2.png")
    botonsalir = pygame.image.load("pausa/botonsalir.png")
    botonsalir2 = pygame.image.load("pausa/botonsalir2.png")
    
    #BOTONES DE MENU PAUSA
    boton1=Boton(botoninicio,botoninicio2,350,290)
    boton2=Boton(botonplay,botonplay2,500,290)
    boton3=Boton(botonsalir,botonsalir2,650,290)

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    while pausado:
        screen.blit(fondo,(0,0))
        screen.blit(fondopausa,(300,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pausado = False
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    pygame.quit()
                    sys.exit(0)
       
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        reloj1.tick(30)
        cursor1.update()
        pygame.display.update()
main()



