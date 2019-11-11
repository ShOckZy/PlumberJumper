# Se importan modulos
import pygame,sys
from pygame.locals import *
from Tkconstants import FALSE

#Inicializacion de pygame
pygame.init()

#Imagenes del menu
menu = pygame.image.load("menu/iniciosinbotones.png")
icon_surf = pygame.image.load("icon.png")
botonjugar = pygame.image.load("menu/botonjugar.png")
botonjugar2 = pygame.image.load("menu/botonjugar2.png")
botonsalir = pygame.image.load("menu/botonsalir.png")
botonsalir2 = pygame.image.load("menu/botonsalir2.png")
botonajustes = pygame.image.load("menu/botonajustes.png")
botonajustes2 = pygame.image.load("menu/botonajustes2.png")
bala = pygame.image.load("nivel1/arma.png")

#Carga de sonido de fondo y de clic en variables
clic = pygame.mixer.Sound("sonidos/clic.ogg")
sonidofondo = pygame.mixer.music.load("sonidos/fondo.mp3")

#Variable con el tiempo en FPS
reloj = pygame.time.Clock()

#Variables
aux=1 
NEGRO = (0,0,0)
MposX=20
MposY=460
cont=6
direc=True
i=0
xixf={}
Rxixf={}
parabola={}
salto = False
salto_Par=False

#Play de sonidos
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.25)

#Funcion de imagen
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert_alpha()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

#Funcion del teclado
def teclado():

    #Se registra la tecla presionada y se guarda en la variable "teclado"
    teclado = pygame.key.get_pressed()
    
    #Se declara como global la variable MposX con la posicion "x" del personaje plomero
    global MposX

    #Variales de movimiento y salto
    global cont, direc,salto, salto_Par
    
    #Si se preciona la tecla space y la tecla de direccion derecha el salto parabolico va a ser verdadero
    if teclado[K_SPACE] and teclado[K_RIGHT] and salto_Par==False:
        salto_Par=True
    #Si se preciona la tecla space y la tecla de direccion izquierda el salto parabolico va a ser verdadero
    elif teclado[K_SPACE] and teclado[K_LEFT] and salto_Par==False:
        salto_Par=True

    #Si se presiona la tecla de direccion derecha y la posicion "x" de plomero es menor a 1000 pixeles se movera 2 pixeles a la derecha 
    elif teclado[K_RIGHT]and salto==False and salto_Par==False:
        if MposX <=1000:
            MposX+=2
            cont+=1
            direc=True
    #Si se presiona la tecla de direccion izquierda y la posicion "x" de plomero es mayor a 0 pixeles se movera 2 pixeles a la izquierda
    elif teclado[K_LEFT]and salto==False and salto_Par==False:
        if MposX >= 0:
            MposX-=2
            cont+=1
            direc=False
    #Si se presiona la tecla space, el salto sera verdadero
    elif teclado[K_SPACE] and salto==False and salto_Par==False:
        salto=True
    #Si no se cumple ninguna condicion el contador sera igual a 6
    else :
         cont=6

    return

#Funcion sprite con cada movimiento del personaje
def sprite():

    #Se declara cont como global
    global cont
    
    #Seleccion en pixeles de cada movimiento en la imagen con todos los movimientos en direccion normal
    xixf[0]=(190,0,150,159)
    xixf[1]=(30,0,140,159)
    xixf[2]=(190,0,150,159)
    xixf[3]=(350,0,450,159)

    #Seleccion en pixeles de cada movimiento en la imagen con todos los movimientos en direccion reversa
    Rxixf[0]=(210,0,150,159)
    Rxixf[1]=(370,0,460,159)
    Rxixf[2]=(210,0,150,159)
    Rxixf[3]=(50,0,150,159)
    
    p=6

    #Se declara i como global
    global i

    #Seleccion de movimiento en la lista de movimientos
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

#Clase enemigo
class enemigo(pygame.sprite.Sprite):
        #Se inicializa la clase
	def __init__(self,posx,posy):
		pygame.sprite.Sprite.__init__(self)
                
                #Se carga la imagen del primer enemigo en la variable "imagen"
		self.imagen = pygame.image.load('nivel1/Enemigo1.png')

                #Se carga la imagen en un objeto manipulable
		self.rect = self.imagen.get_rect()
                
                #Variables
		self.listaDisparo = []
		self.velocidad = 20
		self.rect.top = posy
		self.rect.left = posx
		self.arriba = True
		self.veloz = 3
        #Funcion para actualizar el enemigo en pantalla
	def dibujar (self,screen):
                
                #Movimiento del enemigo de arriba a abajo y de abajo a arriba
		if self.arriba == True:
			self.rect.top = self.rect.top - self.veloz
			if self.rect.top < 150:
				self.arriba = False
		else:
			self.rect.top = self.rect.top + self.veloz
			if self.rect.top > 400:
				self.arriba = True
                #Se muestra la imagen en la pantalla
		screen.blit(self.imagen, self.rect)

#Clase proyectil
class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    #Inicializacion de la clase
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Se carga la variable "bala" (Con la imagen) en la variable "image"
        self.image = bala
        #Se carga la imagen en un objeto manipulable
        self.rect=self.image.get_rect()

    #Funcion para actualizar el proyectil en pantalla
    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x += 5
        #Se muestra la imagen en la pantalla
        screen.blit(self.image,self.rect)

#Clase boton
class Boton(pygame.sprite.Sprite):
    #Se inicializa la clase boton
    def __init__(self,botonjugar,botonjugar2,x=360,y=300):

        #Se carga la imagen normal del boton
        self.imagen_normal=botonjugar
        #Se carga la imagen de seleccion del boton
        self.imagen_seleccion=botonjugar2
        #Se declara la imagen actual
        self.imagen_actual=self.imagen_normal
        #Se crea un objeto rect con la imagen actual
        self.rect=self.imagen_actual.get_rect()
        #Se declara la posicion "x" y "y" del objeto
        self.rect.left,self.rect.top=(x,y)

    #Funcion para actualizar el boton en pantalla
    def update(self,screen,cursor):
        #Si el cursor colisiona con el objeto "boton", la imagen actual sera la imagen de seleccion
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        #Si no, la imagen actual sera la normal   
        else: self.imagen_actual=self.imagen_normal

        #Se muestra la imagen del boton actual en la pantalla
        screen.blit(self.imagen_actual,self.rect)

#Clase cursor 
class cursor(pygame.Rect):

    #Fucion para inicializar la clase cursor
    def __init__(self):
        #Se crea un objeto de 1x1 pixel de dimension
        pygame.Rect.__init__(self,0,0,1,1)

    #Fucion para actualizar la posicion del objeto dependiendo la posicion del cursor del mouse
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

#Funcion principal o menu
def main():
    #Inicializacion de pygame
    pygame.init()
    #Se define el volumen de la musica de fondo
    pygame.mixer.music.set_volume(.25)
    #Titulo de la ventana
    pygame.display.set_caption("Plumber Jumper")
    #Tamano de la ventana
    screen = pygame.display.set_mode((1080,720)) 
    #Incono de la ventana
    pygame.display.set_icon(icon_surf)
    #Definicion del cursor en una variable
    cursor1=cursor()
    
    #Creacion de botones
    boton1=Boton(botonjugar,botonjugar2,360,300)
    boton2=Boton(botonsalir,botonsalir2,360,450)
    boton3=Boton(botonajustes,botonajustes2,50,570)

    #Loop principal del menu o main
    while True:
        #Fondo del menu o main
        screen.blit(menu,(0,0))
        #Eventos en pygame
        for event in pygame.event.get():
            #Evento de clic
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Si el cursor colisiona con el boton "jugar" se direccionara a la funcion "Menujugar"
                if cursor1.colliderect(boton1.rect):
                    #Sonido de clic
                    clic.play()
                    Menujugar()
                #Si el cursor colisiona con el boton "salir" el programa se cierra
                if cursor1.colliderect(boton2.rect):
                    #Sonido de clic
                    clic.play()
                    pygame.quit()
                #Si el cursor colisiona con el boton "ajustes" se direccionara a la funcion "Ajustes"
                if cursor1.colliderect(boton3.rect):
                    #Sonido de clic
                    clic.play()
                    Ajustes()
            #Cerrar pygame con el boton salir de la ventana
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        #Actualizacion del funciones
        cursor1.update()
        print (event) #Imprimir eventos (Se borrara una vez acabado el juego)
        boton1.update(screen,cursor1) #Actualizacion del boton jugar
        boton2.update(screen,cursor1) #Actualizacion del boton salir
        boton3.update(screen,cursor1) #Actualizacion del boton ajustes
        pygame.display.update() #Actualizacion del display

        #Definicion de FPS
        reloj.tick(30)        
#Funcion a justes
def Ajustes():
    #Inicializacion de pygame
    pygame.init()
    
    #Imagenes del menu de ajustes
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
    
    #Titulo de la ventana
    pygame.display.set_caption("Ajustes")
    #Tamano de la ventana
    screen = pygame.display.set_mode((1080,720))

    #Variable con el reloj
    reloj=pygame.time.Clock()
    #Variable con el cursor
    cursor1=cursor()
    
    #Definicion de botones
    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(espanol,espanol2,430,240)
    boton3=Boton(ingles,ingles2,600,240)
    boton4=Boton(sonidosi,sonidosi2,430,380)
    boton5=Boton(sonidono,sonidono2,600,380)
    boton6=Boton(sonidosi,sonidosi2,430,525)
    boton7=Boton(sonidono,sonidono2,600,525)

    #Loop principal
    while True:
        #Se carga fondo de los ajustes
        screen.blit(fondo,(0,0))
        #Eventos de pygame
        for event in pygame.event.get():
            #Evento clic del mouse
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Si el clic del mouse colisiona con el boton de regresar, se direccionara al menu principal
                if cursor1.colliderect(boton1.rect):
                    #Sonido del clic
                    clic.play()
                    main()
                #Si el clic del mouse colisiona con el boton de "no", se define el sonido con volumen del 0%
                if cursor1.colliderect(boton5.rect):
                    #Sonido del clic
                    clic.play()
                    clic.set_volume(0)
                #Si el clic del mouse colisiona con el boton de "si", se define el sonido con volumen del 100%
                if cursor1.colliderect(boton4.rect):
                    #Sonido del clic
                    clic.play()
                    clic.set_volume(1)
                #Si el clic del mouse colisiona con el boton de "si", se define la musica de fondo con volumen del 25%
                if cursor1.colliderect(boton6.rect):
                    #Sonido del clic
                    clic.play()
                    pygame.mixer.music.set_volume(.25)
                #Si el clic del mouse colisiona con el boton de "no", se define la musica de fondo con volumen del 0%
                if cursor1.colliderect(boton7.rect):
                    #Sonido del clic
                    clic.play()
                    pygame.mixer.music.set_volume(0)
            #Si se da clic al boton salir de la ventana, se termina el programa
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        #Actualizacion de botones
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)
        boton5.update(screen,cursor1)
        boton6.update(screen,cursor1)
        boton7.update(screen,cursor1)
        
        #Actualizacion de la posicion del cursor
        cursor1.update()

        print (event)   #Imprimir los eventos en consola (eliminar al acabar el juego)

        #Definicion de FPS
        reloj.tick(30)    

        #Actualizacion del display (pantalla)
        pygame.display.update()

def Menujugar():
    
    #Imagenes del menu "jugar"
    menujugar = pygame.image.load("menujugar/menujugar.png")
    botonregresar = pygame.image.load("menujugar/botonregresar.png")
    botonregresar2 = pygame.image.load("menujugar/botonregresar2.png")
    miniaturalvl1 = pygame.image.load("menujugar/miniaturalvl1.png")
    miniaturalvl12 = pygame.image.load("menujugar/miniaturalvl1_2.png")
    miniaturalvl2 = pygame.image.load("menujugar/miniaturalvl2.png")
    miniaturalvl22 = pygame.image.load("menujugar/miniaturalvl2_2.png")
    miniaturalvl3 = pygame.image.load("menujugar/miniaturalvl3.png")
    miniaturalvl32 = pygame.image.load("menujugar/miniaturalvl3_2.png")
    
    #Clase cursor en un variable
    cursor1=cursor()

    #Inicializacion de pygame
    pygame.init()

    #Titulo de la ventana
    pygame.display.set_caption("Plumber Jumper")

    #Tamano de la ventana
    screen=pygame.display.set_mode((1080,720))
    
    #Definicion de botones
    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(miniaturalvl1,miniaturalvl12,25,220)
    boton3=Boton(miniaturalvl2,miniaturalvl22,378,220)
    boton4=Boton(miniaturalvl3,miniaturalvl32,730,220)
    
    #Reloj en una variable
    reloj=pygame.time.Clock()

    #Loop principal
    while True: 
        #Se carga el fondo del menu jugar
        screen.blit(menujugar,(0,0))
        #Eventos de pygame
        for event in pygame.event.get():
            #Si se presiona clic del mouse...
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Si se da clic en el boton "regresar" se direccionara a la funcion menu o main
                if cursor1.colliderect(boton1.rect):
                    #Sonido de clic
                    clic.play()
                    main()
                #Si se da clic en el boton "nivel 1" se direccionara a la funcion nivel1
                if cursor1.colliderect(boton2.rect):
                    #Sonido de clic
                    clic.play()
                    nivel1()
            #Si se da clic al boton cerrar de la ventana, terminar programa
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        #Actualizacion de botones
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)

        print (event) #Imprimir eventos en consola (Borrar una vez acabado el juego)

        #Asignacion de FPS
        reloj.tick(20)

        #Actualizacion de posicion del cursor
        cursor1.update()

        #Actualizacion del display (pantalla)
        pygame.display.update()
#Funcion del primer nivel
def nivel1():

    #Inicializacion de pygame
    pygame.init()
    
    #Imagenes del nivel 1
    fondo = pygame.image.load("nivel1/nivel1.png")
    barravidapersonaje = pygame.image.load("nivel1/barravidapersonaje.png")     
    barraagua = pygame.image.load("nivel1/barraporcentajeagua.png")
    barratubos = pygame.image.load("nivel1/barratubos.png")
    barraenemigo = pygame.image.load("nivel1/barravidaenemigo.png")
    llavedeagua = pygame.image.load("nivel1/llavedeagua.png")
    botonpausa = pygame.image.load("pausa/botonpausa.png")
    botonpausa2 = pygame.image.load("pausa/botonpausa2.png")
    agua75= pygame.image.load("nivel1/agua75porciento.png")
    
    #Tamano de la ventana
    screen = pygame.display.set_mode((1080,720))
    #Titulo de la ventana
    pygame.display.set_caption("Plumber Jumper: Nivel 1")

    #Imagen del personaje "plomero"
    plom = imagen("personajes/plomero/plomeroninja.png",True)
    #Imagen del personaje "plomero" invertida de forma horizontal
    plom_inv=pygame.transform.flip(plom,True,False);

    #Clase enemigo en una variable
    enemigo1= enemigo(800, 400)

    #Variables del salto
    global salto_Par  
    bajada=False
    bajada_Par=False
    
    #Variable con el reloj
    reloj1=pygame.time.Clock()
    
    #Boton "pausa" del nivel 1
    boton1=Boton(botonpausa,botonpausa2,980,10)

    #Clase proyectil en variable
    proyectil = Proyectil()

    #Clase cursor en variable
    cursor1=cursor()

    #Cancelacion de la musica de fondo
    pygame.mixer.music.set_volume(0)

    #Creacion del grupo con la lista de proyectiles del personaje "plomero"
    lista_proyectiles=pygame.sprite.Group()

    #Variables
    movimientobala=False
    x=0
    vidaenemigo = 100

    #Loop principal
    while True:
        
        #Implementacion de la funcion "sprite", o funcion del personaje "plomero"
        sprite()
        #Implementacion de la funcion "teclado" o funcion que tomara los eventos que usen botones del teclado
        teclado()

        #Carga de imagenes
        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(10,20))
        screen.blit(barraagua,(10,100))
        screen.blit(barratubos,(10,185))
        screen.blit(barraenemigo,(832,80))
        screen.blit(llavedeagua,(970,510))

        #Asignacion de variables como globales
        global MposX,MposY,salto
        
        #Si la direccion del plomero es normal y no se realiza ningun tipo de salto, se cargara la imagen normal del plomero
        if direc==True and salto==False and salto_Par==False and movimientobala==False:
            screen.blit(plom, ( MposX, MposY),(xixf[i]))
   
        #Si la direccion del plomero es invertida y no se realiza ningun tipo de salto, se cargara la imagen invertida del plomero
        if direc==False and salto==False and salto_Par==False and movimientobala==False:
            screen.blit(plom_inv, ( MposX, MposY),(Rxixf[i]))
       
       
    #salto normal:
        #Si se realiza el salto normal pero no el salto parabolico...
        if salto==True and salto_Par==False:            
            
            #Si la direccion del plomero es normal, se cargara la segunda posicion del personaje normal
            if direc==True and "movimientobala==False":
                screen.blit(plom, ( MposX, MposY),(xixf[1]))
            #Si la direccion del plomero es invertida, se cargara la segunda posicion del personaje invertida
            if direc==False and "movimientobala==False":
                screen.blit(plom_inv, ( MposX, MposY),(Rxixf[1]))  

           #Si el personaje "plomero" no va bajada, se restara 5 pixeles a la posicion "y" del personaje
            if bajada==False:
                MposY-=5
            
           #Si el personaje "plomero" va bajada, se sumara 5 pixeles a la posicion "y" del personaje
            if bajada==True:
                MposY+=5              
           #Si la posicion "y" del "plomero" esta en 340 pixeles, el "plomero" va a ir en bajada
            if MposY==340:
                bajada=True
           
           #Si la posicion "y" del "plomero" esta en 460 pixeles, el "plomero" va a ir en subida
            if MposY==460:
                bajada=False
                #Despues de ejecutar el salto, el salto se volvera falso, es decir, no saltara
                salto=False
      

    #Salto parabolico:
        #Si se realiza el salto parabolico pero no el normal y la posicion del plomero es normal...
        if salto_Par==True and salto==False and direc==True and "movimientobala==False":            
            
            #Se cargara la imagen normal del plomero en la segunda posicion
            screen.blit(plom, ( MposX, MposY),(xixf[1]))
           
           #Si el personaje "plomero" no esta de bajada se restaran 5 pixeles a la posicion "y" y se sumaran 4 pixeles a la posicion "x"
            if bajada_Par==False:
                MposY-=5
                MposX+=4
               
           #Si el personaje "plomero" esta de bajada se sumaran 5 pixeles a la posicion "y" y se sumaran 4 pixeles a la posicion "x"
            if bajada_Par==True:
                MposY+=5
                MposX+=4
           #Si la posicion "y" del "plomero" esta en 340 pixeles, el "plomero" va a ir en bajada
            if MposY==340:
                bajada_Par=True
           #Si la posicion "y" del "plomero" esta en 460 pixeles, el "plomero" no ejecutara ningun salto
            if MposY==460:
                bajada_Par=False
                salto_Par=False
        #Sino, si se ejecuta el salto parabolico pero no el salto y la direccion del personaje es inversa...
        elif salto_Par==True and salto==False and direc==FALSE and "movimientobala==False":            
           
            #Se cargara la imagen normal del plomero en la segunda posicion
            screen.blit(plom_inv, ( MposX, MposY),(Rxixf[1]))
            
            #Si el personaje "plomero" no va de bajada, se restaran 5 pixeles a las posicion "y" y 4 pixeles a la posicion "x"
            if bajada_Par==False:
                MposY-=5
                MposX-=4

            #Si no el personaje "plomero" no va de bajada, se restaran 5 pixeles a las posicion "y" y 4 pixeles a la posicion "x"
            if bajada_Par==True:
                MposY+=5
                MposX-=4
           
            #Si la posicion "y" del "plomero" esta en 340 pixeles, el "plomero" va a ir en bajada parabolica
            if MposY==340:
                bajada_Par=True
           
            #Si la posicion "y" del "plomero" esta en 460 pixeles, el "plomero" no ejecutara ningun salto
            if MposY==460:
                bajada_Par=False
                salto_Par=False

    #Movimiento de personaje cuando se dispara:
        #Si la direccion del personaje es normal cuando se dispara y no se ejecuta ningun salto se ejecutara la segunda posicion del personaje
        if direc==True and movimientobala==True and salto==False and salto_Par==False:
            screen.blit(plom, ( MposX, MposY),(xixf[1]))
            if proyectil.rect.x==x+150:
                movimientobala=False
        #Si la direccion del personaje es inversa cuando se dispara y no se ejecuta ningun salto se ejecutara la segunda posicion del personaje
        if direc==False and movimientobala==True and salto==False and salto_Par==False:
            screen.blit(plom_inv, ( MposX, MposY),(Rxixf[1]))  
            if proyectil.rect.x==x+150:
                movimientobala=False

        #En eventos de pygame...
        for event in pygame.event.get():
            #Si se selecciona el boton salir de la ventana, se termina el programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            #Si se se presiona alguna tecla del teclado...
            if event.type == pygame.KEYDOWN:

                #Si se presiona la tecla "esc" se direccionara a la funcion con el menu de pausa
                if event.key == pygame.K_ESCAPE:
                    pausa()
                #Si se presiona la tecla "x" se ejecutara el disparo
                if event.key == pygame.K_x:

                    #Se inicia el movimiento de la bala
                    movimientobala=True

                    #Se define la variable con la clase del proyectil
                    proyectil = Proyectil()

                    #Se manda la posicion "x" y "y" de la bala a la clase proyectil, la posicion es la misma que la del "plomero"
                    proyectil.rect.x= MposX+50
                    x = proyectil.rect.x
                    proyectil.rect.y= MposY+80

                    #Se crea una agrega el proyectil a la lista
                    lista_proyectiles.add(proyectil)
            #Si se da clic con el mouse...
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Si se da clic con el cursor en el boton de pausa, estos colisionan y se direcciona a la funcion "pausa" con el menu de pausa
                if cursor1.colliderect(boton1.rect):
                    #Sonido de clic
                    clic.play()
                    pausa()
       
        #Actualizar la imagen del enemigo
        enemigo1.dibujar(screen)

        #Actualizar las imagenes de los proyectiles
        lista_proyectiles.update(screen)

        #Actualizar el boton de pausa
        boton1.update(screen,cursor1)

        #Asignacion de los FPS
        reloj1.tick(100)

        #Actualizacion de la ubicacion del cursor
        cursor1.update()

        #Actualizacion del display (pantalla)
        pygame.display.update()

#Funcion con el menu de pausa
def pausa():

    #El juego esta pausado
    pausado = True

    #Tamano de la ventana
    screen = pygame.display.set_mode((1080,720))

    #Imagenes del menu de pausa
    fondo = pygame.image.load("nivel1/nivel1.png")
    fondopausa = pygame.image.load("pausa/fondopausa.png")
    botoninicio = pygame.image.load("pausa/botoninicio.png")
    botoninicio2 = pygame.image.load("pausa/botoninicio2.png")
    botonplay = pygame.image.load("pausa/botonplay.png")
    botonplay2 = pygame.image.load("pausa/botonplay2.png")
    botonsalir = pygame.image.load("pausa/botonsalir.png")
    botonsalir2 = pygame.image.load("pausa/botonsalir2.png")
    
    #Botones del menu de pausa
    boton1=Boton(botoninicio,botoninicio2,350,290)
    boton2=Boton(botonplay,botonplay2,500,290)
    boton3=Boton(botonsalir,botonsalir2,650,290)
    
    #Definicion de variable con la clase del cursor
    cursor1=cursor()

    #Definicion de variable con el reloj
    reloj1=pygame.time.Clock()

    #Mientras en juego este pausado...
    while pausado:

        #Carga de la imagen de fondo
        screen.blit(fondo,(0,0))

        #Carga del cuadro del menu de pausa
        screen.blit(fondopausa,(300,250))

        #En eventos de pygame...
        for event in pygame.event.get():

            #Si se selecciona el boton de salir de la ventana, el programa termina
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            #Si se selecciona alguna tecla...
            if event.type == pygame.KEYDOWN:

                #Si se selecciona la tecla "Esc" se saldra del menu de pausa
                if event.key == pygame.K_ESCAPE:
                    pausado = False
            #Si se selecciona el clic del mouse...
            if event.type==pygame.MOUSEBUTTONDOWN:

                #Si se da clic con el mouse en el boton de inicio, estos colisionan y se direccionara al menu principal o main
                if cursor1.colliderect(boton1.rect):
                    #Sonido de clic
                    clic.play()
                    main()

                #Si se da clic con el mouse en el boton de jugar, estos colisionan y se cerrara el menu de pausa
                if cursor1.colliderect(boton2.rect):
                    #Sonido de clic
                    clic.play()
                    pausado = False

                #Si se da clic con el mouse en el boton de salir, estos colisionan y se termina el programa
                if cursor1.colliderect(boton3.rect):
                    #Sonido de clic
                    clic.play()
                    pygame.quit()
                    sys.exit(0)

        #Actualizacion de las imagenes de los botones
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)

        #Asignacion de los FPS
        reloj1.tick(30)

        #Actualizacion de la ubicacion del cursor
        cursor1.update()

        #Actualizacion del display (pantalla)
        pygame.display.update()

#Se llama a la funcion principal o main
main()



