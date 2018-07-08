#!/usr/bin/python
import pygame
import sys
import pygame.locals
from pygame.constants import *
from pygame.mixer import music
from Cursor import CURSOR
from gi.repository import Gtk

#pygame.init()
x=1200
y=900
ocultar = 1


class interfaz():
    
    def __init__(self):
        
        self.Portada = pygame.image.load("img/Portada.png")
        self.menu = pygame.image.load("img/Menu.jpg")
        self.bienvenida = pygame.image.load("img/Bienvenida.png")
        self.ayuda = pygame.image.load("img/interfaz_Ayuda.png")
        self.ayuda_actividad = pygame.image.load("img/AYUDA_1.png")
        self.cir = pygame.image.load("img/Circulo.png")
        self.circ = pygame.image.load("img/circulo_centro.png")
        self.cirr = pygame.image.load("img/circulo_radio.png")
        self.triang = pygame.image.load("img/Triangulo.png")
        self.triangv = pygame.image.load("img/triangulo_vertice.png")
        self.triangl = pygame.image.load("img/triangulo_lado.png")
        self.trianga = pygame.image.load("img/triangulo_altura.png")
        self.triangb = pygame.image.load("img/triangulo_base.png")
        self.triangcla = pygame.image.load("img/triangulo_clasificacion.png")
        self.bienvecir = pygame.image.load("img/portada_actividad_cir.png")
        self.preg1_cir = pygame.image.load("img/actividad1_circulo/Actividad_Circulo.png")
        self.preg1_cirbien = pygame.image.load("img/actividad1_circulo/Actividad_Circulo_bien.png")
        self.preg1_cirmalo1 = pygame.image.load("img/actividad1_circulo/Actividad_Circulo_malo_1.png")
        self.preg1_cirmalo2 = pygame.image.load("img/actividad1_circulo/Actividad_Circulo_malo_2.png")
        self.preg2_cir = pygame.image.load("img/actividad2_circulo/Actividad_Circulo_2.png")
        self.preg2_cirbien = pygame.image.load("img/actividad2_circulo/Actividad_Circulo_2_bien.png")
        self.preg2_cirmalo1 = pygame.image.load("img/actividad2_circulo/Actividad_Circulo_2_malo_1.png")
        self.preg2_cirmalo2 = pygame.image.load("img/actividad2_circulo/Actividad_Circulo_2_malo_2.png")
        self.preg3_cir = pygame.image.load("img/actividad3_circulo/ACTV_3.png")
        self.preg3_cirbien = pygame.image.load("img/actividad3_circulo/ACTV_3_bien.png")
        self.preg3_cirmalo1 = pygame.image.load("img/actividad3_circulo/ACTV_3_malo_1.png")
        self.preg3_cirmalo2 = pygame.image.load("img/actividad3_circulo/ACTV_3_malo_2.png")
        self.preg4_cir = pygame.image.load("img/actividad4_circulo/ACTV_3_circunferencia.png")
        self.preg4_cirbien = pygame.image.load("img/actividad4_circulo/ACTV_3_circunferencia_bien.png")
        self.preg4_cirmalo1 = pygame.image.load("img/actividad4_circulo/ACTV_3_circunferencia_malo_1.png")
        self.preg4_cirmalo2 = pygame.image.load("img/actividad4_circulo/ACTV_3_circunferencia_malo_2.png")
        self.preg5_cir = pygame.image.load("img/actividad5_circulo/ACTV_3_radio.png")
        self.preg5_cirbien = pygame.image.load("img/actividad5_circulo/ACTV_3_radio_Bien.png")
        self.preg5_cirmalo1 = pygame.image.load("img/actividad5_circulo/ACTV_3_radio_malo_1.png")
        self.preg5_cirmalo2 = pygame.image.load("img/actividad5_circulo/ACTV_3_radio_malo_2.png")
        self.preg6_cir = pygame.image.load("img/actividad6_circulo/Actividad_circulo_4.png")
        self.preg6_cirbien = pygame.image.load("img/actividad6_circulo/Actividad_circulo_4_bien.png")
        self.preg6_cirmalo1 = pygame.image.load("img/actividad6_circulo/Actividad_circulo_4_malo.png")
        self.preg6_cirmalo2 = pygame.image.load("img/actividad6_circulo/Actividad_circulo_4_malo_2.png")
        self.pregfin_cir = pygame.image.load("img/final_actividades_cir.png")
        self.triangequi =pygame.image.load("img/triangulo_Equilatero.png")
        self.triangiso =pygame.image.load("img/triangulo_Isosceles.png")
        self.triangesca =pygame.image.load("img/triangulo_escaleno.png")
        self.triangbien = pygame.image.load("img/portada_actividad_triangulo.png")
        self.preg1_triang = pygame.image.load("img/actividad1_triangulo/actividad_1_Triangulo.png")
        self.preg1_triangbien = pygame.image.load("img/actividad1_triangulo/actividad_1_Triangulo_bien.png")
        self.preg1_triangmalo1 = pygame.image.load("img/actividad1_triangulo/actividad_1_Triangulo_malo_1.png")
        self.preg1_triangmalo2 = pygame.image.load("img/actividad1_triangulo/actividad_1_Triangulo_malo_2.png")
        self.preg2_triang = pygame.image.load("img/actividad2_triangulo/actividad_1_Triangulo.png")
        self.preg2_triangbien = pygame.image.load("img/actividad2_triangulo/actividad_1_Triangulo_bien.png")
        self.preg2_triangmalo1 = pygame.image.load("img/actividad2_triangulo/actividad_1_Triangulo_malo_1.png")
        self.preg2_triangmalo2 = pygame.image.load("img/actividad2_triangulo/actividad_1_Triangulo_malo_2.png")
        self.preg3_triang = pygame.image.load("img/actividad3_triangulo/actividad_1_Triangulo.png")
        self.preg3_triangbien = pygame.image.load("img/actividad3_triangulo/actividad_1_Triangulo_bien.png")
        self.preg3_triangmalo1 = pygame.image.load("img/actividad3_triangulo/actividad_1_Triangulo_malo_1.png")
        self.preg3_triangmalo2 = pygame.image.load("img/actividad3_triangulo/actividad_1_Triangulo_malo_2.png")
        self.preg4_triang = pygame.image.load("img/actividad4_triangulo/actividad_1_Triangulo.png")
        self.preg4_triangbien = pygame.image.load("img/actividad4_triangulo/actividad_1_Triangulo_bien.png")
        self.preg4_triangmalo1 = pygame.image.load("img/actividad4_triangulo/actividad_1_Triangulo_malo_1.png")
        self.preg4_triangmalo2 = pygame.image.load("img/actividad4_triangulo/actividad_1_Triangulo_malo_2.png")
        self.preg5_triang = pygame.image.load("img/actividad5_triangulo/actividad_1_Triangulo.png")
        self.preg5_triangbien = pygame.image.load("img/actividad5_triangulo/actividad_1_Triangulo_bien.png")
        self.preg5_triangmalo1 = pygame.image.load("img/actividad5_triangulo/actividad_1_Triangulo_mal.png")
        self.preg5_triangmalo2 = pygame.image.load("img/actividad5_triangulo/actividad_1_Triangulo_ma_2l.png")
        self.preg6_triang = pygame.image.load("img/actividad6_triangulo/actividad_1_Triangulo.png")
        self.preg6_triangbien = pygame.image.load("img/actividad6_triangulo/actividad_1_Triangulo_bien.png")
        self.preg6_triangmalo1 = pygame.image.load("img/actividad6_triangulo/actividad_1_Triangulo_malo_1.png")
        self.preg6_triangmalo2 = pygame.image.load("img/actividad6_triangulo/actividad_1_Triangulo_malo_2.png")
        self.preg7_triang = pygame.image.load("img/actividad7_triangulo/actividad_1_Triangulo.png")
        self.preg7_triangbien = pygame.image.load("img/actividad7_triangulo/actividad_1_Triangulo.png_bien.png")
        self.preg7_triangmalo1 = pygame.image.load("img/actividad7_triangulo/actividad_1_Triangulo.png_malo_1.png")
        self.preg7_triangmalo2 = pygame.image.load("img/actividad7_triangulo/actividad_1_Triangulo.png_malo_2.png")
        self.pregfin_triang = pygame.image.load("img/portada_actividad_triangulo_final.png")
        self.cuadra =pygame.image.load("img/Cuadrado.png")
        self.cuadral =pygame.image.load("img/cuadrado_lado.png")
        self.cuadrav =pygame.image.load("img/cuadrado_vertice.png")
        self.rect =pygame.image.load("img/rectangulo.png")
        self.rectv =pygame.image.load("img/Regtangulo_vertice.png")
        self.rombo =pygame.image.load("img/Rombo_lado.png")
        self.rombov =pygame.image.load("img/Rombo_vertice.png")
        self.trapecio =pygame.image.load("img/Trapecio_lado.png")
        self.trapeciov =pygame.image.load("img/Trapecio_vertice.png")
        
        
        self.preg1_rect = pygame.image.load("img/actividad1_rectangulo/actividad_cuadrado_1.png")
        self.preg1_rectgbien = pygame.image.load("img/actividad1_rectangulo/actividad_cuadrado_Bien.png")
        self.preg1_rectmalo1 = pygame.image.load("img/actividad1_rectangulo/actividad_cuadrado_malo_1.png")
        self.preg1_rectmalo2 = pygame.image.load("img/actividad1_rectangulo/actividad_cuadrado_malo_2.png") 
        self.preg2_rect = pygame.image.load("img/actividad2_rectangulo/actividad_cuadrado_1.png")
        self.preg2_rectgbien = pygame.image.load("img/actividad2_rectangulo/actividad_cuadrado_bien.png")
        self.preg2_rectmalo1 = pygame.image.load("img/actividad2_rectangulo/actividad_cuadrado_mal.png")
        self.preg2_rectmalo2 = pygame.image.load("img/actividad2_rectangulo/actividad_cuadrado_mal_2.png")
        self.preg3_rect = pygame.image.load("img/actividad3_rectangulo/actividad_cuadrado_3.png")
        self.preg3_rectgbien = pygame.image.load("img/actividad3_rectangulo/actividad_cuadrado_Bien.png")
        self.preg3_rectmalo1 = pygame.image.load("img/actividad3_rectangulo/actividad_cuadrado_mal.png")
        self.preg3_rectmalo2 = pygame.image.load("img/actividad3_rectangulo/actividad_cuadrado_mal_2.png")
        self.preg4_rect = pygame.image.load("img/actividad4_rectangulo/actividad_cuadrado_4.png")
        self.preg4_rectgbien = pygame.image.load("img/actividad4_rectangulo/actividad_cuadrado_bien.png")
        self.preg4_rectmalo1 = pygame.image.load("img/actividad4_rectangulo/actividad_cuadrado_malo.png")
        self.preg5_rect = pygame.image.load("img/actividad5_rectangulo/actividad_cuadrado_5.png")
        self.preg5_rectgbien = pygame.image.load("img/actividad5_rectangulo/actividad_cuadrado_bien.png")
        self.preg5_rectmalo1 = pygame.image.load("img/actividad5_rectangulo/actividad_cuadrado_malo_1.png")
        self.preg5_rectmalo2 = pygame.image.load("img/actividad5_rectangulo/actividad_cuadrado_malo_2.png")
        self.preg6_rect = pygame.image.load("img/actividad6_rectangulo/actividad_cuadrado_6.png")
        self.preg6_rectgbien = pygame.image.load("img/actividad6_rectangulo/actividad_cuadrado_bien.png")
        self.preg6_rectmalo1 = pygame.image.load("img/actividad6_rectangulo/actividad_cuadrado_malo_1.png")
        self.preg6_rectmalo2 = pygame.image.load("img/actividad6_rectangulo/actividad_cuadrado_malo_2.png")
        
        self.ladrar = pygame.mixer.Sound("sonido/ladrar.ogg")
        
         
    def inter_principal(self, superficie):
        superficie.blit(self.Portada, (0,0))
        
        
        
    
    def poscision_elementos_1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 459 and x_mouse <= 712) and (y_mouse > 580 and y_mouse < 634) :
            ocultar= 39
            
                
        elif (x_mouse > 459 and x_mouse <= 712) and (y_mouse > 681 and y_mouse < 738):
            ocultar =13 
                    
        elif (x_mouse > 462 and x_mouse <= 712) and (y_mouse > 711 and y_mouse < 799):
            sys.exit(0)
                    
    def interfaz_ayuda(self, superficie):
        
        superficie.blit(self.ayuda, (0,0))
        
        
    def poscision_elementos_ayuda(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()

        if(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =1                   
                    
            
        
    def interfaz_menu(self, superficie):
        
        superficie.blit(self.menu, (0,0))
        
        
        
    def poscision_elementos_menu(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 94 and x_mouse <= 320) and (y_mouse > 809 and y_mouse < 860):
            ocultar = 1
        elif (x_mouse > 125 and x_mouse <= 298) and (y_mouse > 232 and y_mouse < 420):
            ocultar=3
            
            
        elif (x_mouse > 421 and x_mouse <= 865) and (y_mouse > 529 and y_mouse < 720):
            ocultar=6
        
        elif (x_mouse > 616 and x_mouse <=1149) and (y_mouse > 322 and y_mouse < 400):
            ocultar=73
        
            
    def interfaz_circulo(self, superficie):
        
        superficie.blit(self.cir, (0,0))
        
        
    def poscision_elementos_circulo(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
            
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =2
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =4
            
 
    def interfaz_circuloc(self, superficie):
        
        superficie.blit(self.circ, (0,0))
        
        
    def poscision_elementos_circuloc(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =3
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =5
            
            
    def interfaz_circulor(self, superficie):
        
        superficie.blit(self.cirr, (0,0))
        
        
    def poscision_elementos_circulor(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =4
            
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =12
       
    
    def interfaz_triangulo(self, superficie):
        
        superficie.blit(self.triang, (0,0))
        
        
    def poscision_elementos_triangulo(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =2
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =7
            
    
    def interfaz_triangulol(self, superficie):
        
        superficie.blit(self.triangl, (0,0))
        
        
    def poscision_elementos_triangulol(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =6
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =8
            
            
    def interfaz_triangulov(self, superficie):
        
        superficie.blit(self.triangv, (0,0))
        
        
    def poscision_elementos_triangulov(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =7
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =9
    
    def interfaz_trianguloa(self, superficie):
        
        superficie.blit(self.trianga, (0,0))
        
        
    def poscision_elementos_trianguloa(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =8
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =10
            
            
    def interfaz_triangulob(self, superficie):
        
        superficie.blit(self.triangb, (0,0))
        
        
    def poscision_elementos_triangulob(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =9
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =11
            
    def interfaz_triangulocla(self, superficie):
        
        superficie.blit(self.triangcla, (0,0))
        
        
    def poscision_elementos_triangulocla(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =10
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =40
            
    def interfaz_circulobienvenida(self, superficie):
        
        superficie.blit(self.bienvecir, (0,0))
        
        
    def poscision_elementos_circulobienvenida(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =5
        
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =14
            
            
    def interfaz_preg1_cir(self, superficie):
        
        superficie.blit(self.preg1_cir, (0,0))
        
        
    def poscision_elementos_preg1_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =15
            self.ladrar.play()
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =16
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =17
            
            
    def interfaz_preg1_cir_bien(self, superficie):
        
        superficie.blit(self.preg1_cirbien, (0,0))
        
        
    def poscision_elementos_preg1_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =18
            
    def interfaz_preg1_cir_malo1(self, superficie):
        
        superficie.blit(self.preg1_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg1_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =14
            
    def interfaz_preg1_cir_malo2(self, superficie):
        
        superficie.blit(self.preg1_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg1_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =14
    def interfaz_preg2_cir(self, superficie):
        
        superficie.blit(self.preg2_cir, (0,0))
        
        
    def poscision_elementos_preg2_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =21
            
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =20
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =19
            self.ladrar.play()  
            
    def interfaz_preg2_cir_bien(self, superficie):
        
        superficie.blit(self.preg2_cirbien, (0,0))
        
        
    def poscision_elementos_preg2_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =22
            
    def interfaz_preg2_cir_malo1(self, superficie):
        
        superficie.blit(self.preg2_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg2_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =18
            
    def interfaz_preg2_cir_malo2(self, superficie):
        
        superficie.blit(self.preg2_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg2_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =18
    
    def interfaz_preg3_cir(self, superficie):
        
        superficie.blit(self.preg3_cir, (0,0))
        
        
    def poscision_elementos_preg3_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 495 and x_mouse<= 744) and (y_mouse >218 and y_mouse < 251):
            ocultar = 23
            self.ladrar.play()
            
        elif(x_mouse > 107 and x_mouse<= 390) and (y_mouse >390 and y_mouse < 434):
            ocultar =24
            
        elif(x_mouse > 793 and x_mouse<= 1100) and (y_mouse >591 and y_mouse < 635):
            ocultar =25
            
              
    def interfaz_preg3_cir_bien(self, superficie):
        
        superficie.blit(self.preg3_cirbien, (0,0))
        
        
    def poscision_elementos_preg3_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =26
    
    def interfaz_preg3_cir_malo1(self, superficie):
        
        superficie.blit(self.preg3_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg3_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =22
            
    def interfaz_preg3_cir_malo2(self, superficie):
        
        superficie.blit(self.preg3_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg3_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =22
            
    def interfaz_preg4_cir(self, superficie):
        
        superficie.blit(self.preg4_cir, (0,0))
        
        
    def poscision_elementos_preg4_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 107 and x_mouse<= 390) and (y_mouse >390 and y_mouse < 434):
            ocultar = 27
            self.ladrar.play()
            
        elif(x_mouse > 495 and x_mouse<= 744) and (y_mouse >218 and y_mouse < 251):
            ocultar =28
            
        elif(x_mouse > 793 and x_mouse<= 1100) and (y_mouse >591 and y_mouse < 635):
            ocultar =29
            
    def interfaz_preg4_cir_bien(self, superficie):
        
        superficie.blit(self.preg4_cirbien, (0,0))
        
        
    def poscision_elementos_preg4_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =30
    
    def interfaz_preg4_cir_malo1(self, superficie):
        
        superficie.blit(self.preg4_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg4_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =26
            
    def interfaz_preg4_cir_malo2(self, superficie):
        
        superficie.blit(self.preg4_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg4_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =26
            
    def interfaz_preg5_cir(self, superficie):
        
        superficie.blit(self.preg5_cir, (0,0))
        
        
    def poscision_elementos_preg5_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 793 and x_mouse<= 1100) and (y_mouse >591 and y_mouse < 635):
            ocultar = 31
            self.ladrar.play()
            
        elif(x_mouse > 107 and x_mouse<= 390) and (y_mouse >390 and y_mouse < 434):
            ocultar =32
            
        elif(x_mouse > 495 and x_mouse<= 744) and (y_mouse >218 and y_mouse < 251):
            ocultar =33
            
    def interfaz_preg5_cir_bien(self, superficie):
        
        superficie.blit(self.preg5_cirbien, (0,0))
        
        
    def poscision_elementos_preg5_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =34
        
    def interfaz_preg5_cir_malo1(self, superficie):
        
        superficie.blit(self.preg5_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg5_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =30
            
    def interfaz_preg5_cir_malo2(self, superficie):
        
        superficie.blit(self.preg5_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg5_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =30
            
    def interfaz_preg6_cir(self, superficie):
        
        superficie.blit(self.preg6_cir, (0,0))
        
        
    def poscision_elementos_preg6_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 200 and x_mouse<= 375) and (y_mouse >305 and y_mouse < 490):
            ocultar = 35
            self.ladrar.play()
            
        elif(x_mouse > 530 and x_mouse<= 680) and (y_mouse >296 and y_mouse < 497):
            ocultar =36
            
        elif(x_mouse > 767 and x_mouse<= 1100) and (y_mouse >323 and y_mouse < 455):
            ocultar =37
            
    def interfaz_preg6_cir_bien(self, superficie):
        
        superficie.blit(self.preg6_cirbien, (0,0))
        
        
    def poscision_elementos_preg6_cir_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =38
    
    def interfaz_preg6_cir_malo1(self, superficie):
        
        superficie.blit(self.preg6_cirmalo1, (0,0))
        
        
    def poscision_elementos_preg6_cir_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =34
    
    def interfaz_preg6_cir_malo2(self, superficie):
        
        superficie.blit(self.preg6_cirmalo2, (0,0))
        
        
    def poscision_elementos_preg6_cir_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =34
            
    def interfaz_pregfin_cir(self, superficie):
        
        superficie.blit(self.pregfin_cir, (0,0))
        
        
    def poscision_elementos_pregfin_cir(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 222 and x_mouse<= 525) and (y_mouse >837and y_mouse < 893):
            ocultar =2
    
    def interfaz_Bienvenida(self, superficie):
        
        superficie.blit(self.bienvenida, (0,0))
        
        
    def poscision_elementos_Bienvenida(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse >36 and x_mouse<= 335) and (y_mouse >816and y_mouse < 880):
            ocultar =2
    
    def interfaz_trianguloequi(self, superficie):
        
        superficie.blit(self.triangequi, (0,0))
        
        
    def poscision_elementos_trianguloequi(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =11
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =41
    
    def interfaz_trianguloiso(self, superficie):
        
        superficie.blit(self.triangiso, (0,0))
        
        
    def poscision_elementos_trianguloiso(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =40
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =42
            
    def interfaz_trianguloesca(self, superficie):
        
        superficie.blit(self.triangesca, (0,0))
        
        
    def poscision_elementos_trianguloesca(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =41
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =43
    
    def interfaz_triangulobienve(self, superficie):
        
        superficie.blit(self.triangbien, (0,0))
        
        
    def poscision_elementos_triangulobienve(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =42
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =44
    
    def interfaz_preg1_triang(self, superficie):
        
        superficie.blit(self.preg1_triang, (0,0))
        
        
    def poscision_elementos_preg1_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 600) and (y_mouse >314 and y_mouse < 383):
            ocultar =45
            self.ladrar.play()
            
        elif(x_mouse > 647 and x_mouse<= 1115) and (y_mouse >315 and y_mouse < 378):
            ocultar =46
        
        elif(x_mouse > 385 and x_mouse<= 825) and (y_mouse >420 and y_mouse < 483):
            ocultar =47
        
    def interfaz_preg1_triang_bien(self, superficie):
        
        superficie.blit(self.preg1_triangbien, (0,0))
        
        
    def poscision_elementos_preg1_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =48
            
            
    def interfaz_preg1_triang_malo1(self, superficie):
        
        superficie.blit(self.preg1_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg1_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =44
            
    def interfaz_preg1_triang_malo2(self, superficie):
        
        superficie.blit(self.preg1_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg1_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =44
    
    def interfaz_preg2_triang(self, superficie):
        
        superficie.blit(self.preg2_triang, (0,0))
        
        
    def poscision_elementos_preg2_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 600) and (y_mouse >314 and y_mouse < 383):
            ocultar =49
            self.ladrar.play()
            
        elif(x_mouse > 647 and x_mouse<= 1115) and (y_mouse >315 and y_mouse < 378):
            ocultar =50
        
        elif(x_mouse > 385 and x_mouse<= 825) and (y_mouse >420 and y_mouse < 483):
            ocultar =51
            
    def interfaz_preg2_triang_bien(self, superficie):
        
        superficie.blit(self.preg2_triangbien, (0,0))
        
        
    def poscision_elementos_preg2_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =52
            
    def interfaz_preg2_triang_malo1(self, superficie):
        
        superficie.blit(self.preg2_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg2_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =48
    
    def interfaz_preg2_triang_malo2(self, superficie):
        
        superficie.blit(self.preg2_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg2_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =48
            
    def interfaz_preg3_triang(self, superficie):
        
        superficie.blit(self.preg3_triang, (0,0))
        
        
    def poscision_elementos_preg3_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 600) and (y_mouse >314 and y_mouse < 383):
            ocultar =54
            
        elif(x_mouse > 647 and x_mouse<= 1115) and (y_mouse >315 and y_mouse < 378):
            ocultar =55
        
        elif(x_mouse > 385 and x_mouse<= 825) and (y_mouse >420 and y_mouse < 483):
            ocultar =53
            self.ladrar.play()
            
    def interfaz_preg3_triang_bien(self, superficie):
        
        superficie.blit(self.preg3_triangbien, (0,0))
        
        
    def poscision_elementos_preg3_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =56
    
    def interfaz_preg3_triang_malo1(self, superficie):
        
        superficie.blit(self.preg3_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg3_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =52
    
    def interfaz_preg3_triang_malo2(self, superficie):
        
        superficie.blit(self.preg3_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg3_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =52
            
    def interfaz_preg4_triang(self, superficie):
        
        superficie.blit(self.preg4_triang, (0,0))
        
        
    def poscision_elementos_preg4_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 600) and (y_mouse >314 and y_mouse < 383):
            ocultar =58
            
        elif(x_mouse > 647 and x_mouse<= 1115) and (y_mouse >315 and y_mouse < 378):
            ocultar =57
            self.ladrar.play()
        
        elif(x_mouse > 385 and x_mouse<= 825) and (y_mouse >420 and y_mouse < 483):
            ocultar =59
    
    def interfaz_preg4_triang_bien(self, superficie):
        
        superficie.blit(self.preg4_triangbien, (0,0))
        
        
    def poscision_elementos_preg4_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =60
    
    def interfaz_preg4_triang_malo1(self, superficie):
        
        superficie.blit(self.preg4_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg4_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =56
    
    def interfaz_preg4_triang_malo2(self, superficie):
        
        superficie.blit(self.preg4_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg4_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =56
            
    def interfaz_preg5_triang(self, superficie):
        
        superficie.blit(self.preg5_triang, (0,0))
        
        
    def poscision_elementos_preg5_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 183 and x_mouse<= 455) and (y_mouse >318 and y_mouse < 503):
            ocultar =61
            self.ladrar.play()
            
        elif(x_mouse > 614 and x_mouse<= 723) and (y_mouse >254 and y_mouse < 514):
            ocultar =62
        
        elif(x_mouse > 855 and x_mouse<= 1095) and (y_mouse >262 and y_mouse < 503):
            ocultar =63
    
    def interfaz_preg5_triang_bien(self, superficie):
        
        superficie.blit(self.preg5_triangbien, (0,0))
        
        
    def poscision_elementos_preg5_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =64
    
    def interfaz_preg5_triang_malo1(self, superficie):
        
        superficie.blit(self.preg5_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg5_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =60
            
    def interfaz_preg5_triang_malo2(self, superficie):
        
        superficie.blit(self.preg5_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg5_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =60
    
    def interfaz_preg6_triang(self, superficie):
        
        superficie.blit(self.preg6_triang, (0,0))
        
        
    def poscision_elementos_preg6_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 183 and x_mouse<= 455) and (y_mouse >318 and y_mouse < 503):
            ocultar =66
            
        elif(x_mouse > 548 and x_mouse<= 790) and (y_mouse >257 and y_mouse < 497):
            ocultar =65
        
        elif(x_mouse > 960 and x_mouse<= 1058) and (y_mouse >265 and y_mouse < 505):
            ocultar =67
    
    def interfaz_preg6_triang_bien(self, superficie):
        
        superficie.blit(self.preg6_triangbien, (0,0))
        
        
    def poscision_elementos_preg6_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =68
    
    def interfaz_preg6_triang_malo1(self, superficie):
        
        superficie.blit(self.preg6_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg6_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =64
            
    def interfaz_preg6_triang_malo2(self, superficie):
        
        superficie.blit(self.preg6_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg6_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =64
            
    def interfaz_preg7_triang(self, superficie):
        
        superficie.blit(self.preg7_triang, (0,0))
        
        
    def poscision_elementos_preg7_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 270 and x_mouse<= 364) and (y_mouse >258 and y_mouse < 503):
            ocultar =69
            
        elif(x_mouse > 474 and x_mouse<= 777) and (y_mouse >290 and y_mouse < 497):
            ocultar =70
        
        elif(x_mouse > 850 and x_mouse<= 1080) and (y_mouse >258 and y_mouse < 500):
            ocultar =71
        
        
    def interfaz_preg7_triang_bien(self, superficie):
        
        superficie.blit(self.preg7_triangbien, (0,0))
        
        
    def poscision_elementos_preg7_triang_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =72
    
    def interfaz_preg7_triang_malo1(self, superficie):
        
        superficie.blit(self.preg7_triangmalo1, (0,0))
        
        
    def poscision_elementos_preg7_triang_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =68
            
    def interfaz_preg7_triang_malo2(self, superficie):
        
        superficie.blit(self.preg7_triangmalo2, (0,0))
        
        
    def poscision_elementos_preg7_triang_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =68
            
    def interfaz_pregfin_triang(self, superficie):
        
        superficie.blit(self.pregfin_triang, (0,0))
        
        
    def poscision_elementos_pregfin_triang(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 32 and x_mouse<= 330) and (y_mouse > 822 and y_mouse < 878):
            ocultar =2
            
    def interfaz_cuadra(self, superficie):
        
        superficie.blit(self.cuadra, (0,0))
        
        
    def poscision_elementos_cuadra(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =2
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =74
            
    def interfaz_cuadral(self, superficie):
        
        superficie.blit(self.cuadral, (0,0))
        
        
    def poscision_elementos_cuadral(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =73
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =75
            
    def interfaz_cuadrav(self, superficie):
        
        superficie.blit(self.cuadrav, (0,0))
        
        
    def poscision_elementos_cuadrav(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =74
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =76
            
    def interfaz_rect(self, superficie):
        
        superficie.blit(self.rect, (0,0))
        
        
    def poscision_elementos_rect(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =75
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =77
            
    def interfaz_rectv(self, superficie):
        
        superficie.blit(self.rectv, (0,0))
        
        
    def poscision_elementos_rectv(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =76
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =78
            
    def interfaz_rombo(self, superficie):
        
        superficie.blit(self.rombo, (0,0))
    
    def poscision_elementos_rombo(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =77
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =79
    
    def interfaz_rombov(self, superficie):
        
        superficie.blit(self.rombov, (0,0))
    
    def poscision_elementos_rombov(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =78
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =80
            
    def interfaz_trapecio(self, superficie):
        
        superficie.blit(self.trapecio, (0,0))
    
    def poscision_elementos_trapecio(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =79
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =81
    
    def interfaz_trapeciov(self, superficie):
        
        superficie.blit(self.trapeciov, (0,0))
    
    def poscision_elementos_trapeciov(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =80
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =82
            
    def interfaz_reclobienve(self, superficie):
        
        superficie.blit(self.triangbien, (0,0))
        
        
    def poscision_elementos_recbienve(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 49 and x_mouse<= 341) and (y_mouse >26 and y_mouse < 79):
            ocultar =81
            
        elif(x_mouse > 79 and x_mouse<= 379) and (y_mouse >815 and y_mouse < 870):
            ocultar =83
    
    def interfaz_preg1_rect(self, superficie):
        
        superficie.blit(self.preg1_rect, (0,0))
        
        
    def poscision_elementos_preg1_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =85
            
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =84
            self.ladrar.play()
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =86
    
    def interfaz_preg1_rect_bien(self, superficie):
        
        superficie.blit(self.preg1_rectgbien, (0,0))
        
        
    def poscision_elementos_preg1_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =87
            
    def interfaz_preg1_rect_malo1(self, superficie):
        
        superficie.blit(self.preg1_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg1_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =83
            
    def interfaz_preg1_rect_malo2(self, superficie):
        
        superficie.blit(self.preg1_rectmalo2, (0,0))
        
        
    def poscision_elementos_preg1_rect_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =83
            
    def interfaz_preg2_rect(self, superficie):
        
        superficie.blit(self.preg2_rect, (0,0))
        
        
    def poscision_elementos_preg2_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =88
            self.ladrar.play()
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =89
            
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =90
    
    def interfaz_preg2_rect_bien(self, superficie):
        
        superficie.blit(self.preg2_rectgbien, (0,0))
        
        
    def poscision_elementos_preg2_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =91
            
    def interfaz_preg2_rect_malo1(self, superficie):
        
        superficie.blit(self.preg2_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg2_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =87
            
    def interfaz_preg2_rect_malo2(self, superficie):
        
        superficie.blit(self.preg2_rectmalo2, (0,0))
        
        
    def poscision_elementos_preg2_rect_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =87
            
    def interfaz_preg3_rect(self, superficie):
        
        superficie.blit(self.preg3_rect, (0,0))
        
        
    def poscision_elementos_preg3_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =92
            self.ladrar.play()
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =93
            
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =94
    
    def interfaz_preg3_rect_bien(self, superficie):
        
        superficie.blit(self.preg3_rectgbien, (0,0))
        
        
    def poscision_elementos_preg3_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =95
            
    def interfaz_preg3_rect_malo1(self, superficie):
        
        superficie.blit(self.preg3_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg3_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =91
            
    def interfaz_preg3_rect_malo2(self, superficie):
        
        superficie.blit(self.preg3_rectmalo2, (0,0))
        
        
    def poscision_elementos_preg3_rect_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =91
            
    def interfaz_preg4_rect(self, superficie):
        
        superficie.blit(self.preg4_rect, (0,0))
        
        
    def poscision_elementos_preg4_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 129 and x_mouse<= 603) and (y_mouse >300 and y_mouse < 490):
            ocultar =96
            self.ladrar.play()
        elif(x_mouse > 647 and x_mouse<= 1128) and (y_mouse >303 and y_mouse < 488):
            ocultar =97
            
    def interfaz_preg4_rect_bien(self, superficie):
        
        superficie.blit(self.preg4_rectgbien, (0,0))
        
        
    def poscision_elementos_preg4_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =98
    
    def interfaz_preg4_rect_malo1(self, superficie):
        
        superficie.blit(self.preg4_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg4_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =95
            
    def interfaz_preg5_rect(self, superficie):
        
        superficie.blit(self.preg5_rect, (0,0))
        
        
    def poscision_elementos_preg5_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar =99
            self.ladrar.play()
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =100
            
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =101
    
    def interfaz_preg5_rect_bien(self, superficie):
        
        superficie.blit(self.preg5_rectgbien, (0,0))
        
        
    def poscision_elementos_preg5_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =102
    
    def interfaz_preg5_rect_malo1(self, superficie):
        
        superficie.blit(self.preg5_rectmalo2, (0,0))
        
        
    def poscision_elementos_preg5_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =98
            
    def interfaz_preg5_rect_malo2(self, superficie):
        
        superficie.blit(self.preg5_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg5_rect_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =98
            
    def interfaz_preg6_rect(self, superficie):
        
        superficie.blit(self.preg6_rect, (0,0))
        
        
    def poscision_elementos_preg6_rect(self, superficie):
        global ocultar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 136 and x_mouse<= 603) and (y_mouse >316 and y_mouse < 383):
            ocultar = 104
            
        elif(x_mouse > 410 and x_mouse<= 871) and (y_mouse >431 and y_mouse < 501):
            ocultar =103
            self.ladrar.play()
            
        elif(x_mouse > 646 and x_mouse<= 1113) and (y_mouse >319 and y_mouse < 384):
            ocultar =105
            
    def interfaz_preg6_rect_bien(self, superficie):
        
        superficie.blit(self.preg6_rectgbien, (0,0))
        
        
    def poscision_elementos_preg6_rect_bien(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 467 and x_mouse<= 762) and (y_mouse >800 and y_mouse < 859):
            ocultar =72
    
    def interfaz_preg6_rect_malo1(self, superficie):
        
        superficie.blit(self.preg6_rectmalo1, (0,0))
        
        
    def poscision_elementos_preg6_rect_malo1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =102
            
    def interfaz_preg6_rect_malo2(self, superficie):
        
        superficie.blit(self.preg6_rectmalo2, (0,0))
        
        
    def poscision_elementos_preg6_rect_malo2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if(x_mouse > 551 and x_mouse<= 650) and (y_mouse >800 and y_mouse < 888):
            ocultar =102
    
    
            
            
def main():
    global ocultar
    x_mouse, y_mouse = pygame.mouse.get_pos()
    ventana = pygame.display.set_mode((x,y))
    
    cursor = pygame.cursors.compile(CURSOR)
    pygame.mouse.set_cursor((32,32), (1,1), *cursor)
    
    pygame.mixer.music.load("sonido/intro.ogg")
    pygame.mixer.music.play(10)
    prin=interfaz()    

    while True:
        while Gtk.events_pending():
            Gtk.main_iteration()
        x_mouse, y_mouse = pygame.mouse.get_pos()
       
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if(ocultar==1):
                    prin.poscision_elementos_1(ventana)
                    if (x_mouse > 1043 and x_mouse<= 1099) and (y_mouse >17 and y_mouse < 76):
                        pygame.mixer.music.unpause()
                    elif (x_mouse > 1136 and x_mouse<= 1178) and (y_mouse >19 and y_mouse < 73):
                        pygame.mixer.music.pause()
                elif(ocultar==2):
                    prin.poscision_elementos_menu(ventana)
                elif(ocultar==3):
                    prin.poscision_elementos_circulo(ventana)
                elif(ocultar==4):
                    prin.poscision_elementos_circuloc(ventana)
                elif(ocultar==5):
                    prin.poscision_elementos_circulor(ventana)
                elif(ocultar==6):
                    prin.poscision_elementos_triangulo(ventana)
                elif(ocultar==7):
                    prin.poscision_elementos_triangulol(ventana)
                elif(ocultar==8):
                    prin.poscision_elementos_triangulov(ventana)  
                elif(ocultar==9):
                    prin.poscision_elementos_trianguloa(ventana)
                elif(ocultar==10):
                    prin.poscision_elementos_triangulob(ventana)
                elif(ocultar==11):
                    prin.poscision_elementos_triangulocla(ventana)
                elif(ocultar==12):
                    prin.poscision_elementos_circulobienvenida(ventana)
                elif(ocultar==13):
                    prin.poscision_elementos_ayuda(ventana)
                elif(ocultar==14):
                    prin.poscision_elementos_preg1_cir(ventana)
                elif(ocultar==15):
                    prin.poscision_elementos_preg1_cir_bien(ventana)
                elif(ocultar==16):
                    prin.poscision_elementos_preg1_cir_malo1(ventana)
                elif(ocultar==17):
                    prin.poscision_elementos_preg1_cir_malo2(ventana)
                elif(ocultar==18):
                    prin.poscision_elementos_preg2_cir(ventana)
                elif(ocultar==19):
                    prin.poscision_elementos_preg2_cir_bien(ventana)
                elif(ocultar==20):
                    prin.poscision_elementos_preg2_cir_malo1(ventana)
                elif(ocultar==21):
                    prin.poscision_elementos_preg2_cir_malo2(ventana)
                elif(ocultar==22):
                    prin.poscision_elementos_preg3_cir(ventana)
                elif(ocultar==23):
                    prin.poscision_elementos_preg3_cir_bien(ventana)
                elif(ocultar==24):
                    prin.poscision_elementos_preg3_cir_malo1(ventana)
                elif(ocultar==25):
                    prin.poscision_elementos_preg3_cir_malo2(ventana)
                elif(ocultar==26):
                    prin.poscision_elementos_preg4_cir(ventana)
                elif(ocultar==27):
                    prin.poscision_elementos_preg4_cir_bien(ventana)
                elif(ocultar==28):
                    prin.poscision_elementos_preg4_cir_malo1(ventana)
                elif(ocultar==29):
                    prin.poscision_elementos_preg4_cir_malo2(ventana)
                elif(ocultar==30):
                    prin.poscision_elementos_preg5_cir(ventana)
                elif(ocultar==31):
                    prin.poscision_elementos_preg5_cir_bien(ventana)
                elif(ocultar==32):
                    prin.poscision_elementos_preg5_cir_malo1(ventana)
                elif(ocultar==33):
                    prin.poscision_elementos_preg5_cir_malo2(ventana)
                elif(ocultar==34):
                    prin.poscision_elementos_preg6_cir(ventana)
                elif(ocultar==35):
                    prin.poscision_elementos_preg6_cir_bien(ventana)
                elif(ocultar==36):
                    prin.poscision_elementos_preg6_cir_malo1(ventana)
                elif(ocultar==37):
                    prin.poscision_elementos_preg6_cir_malo2(ventana)
                elif(ocultar==38):
                    prin.poscision_elementos_pregfin_cir(ventana)
                elif(ocultar==39):
                    prin.poscision_elementos_Bienvenida(ventana)
                elif(ocultar==40):
                    prin.poscision_elementos_trianguloequi(ventana)
                elif(ocultar==41):
                    prin.poscision_elementos_trianguloiso(ventana)
                elif(ocultar==42):
                    prin.poscision_elementos_trianguloesca(ventana)
                elif(ocultar==43):
                    prin.poscision_elementos_triangulobienve(ventana)
                elif(ocultar==44):
                    prin.poscision_elementos_preg1_triang(ventana)
                elif(ocultar==45):
                    prin.poscision_elementos_preg1_triang_bien(ventana)
                elif(ocultar==46):
                    prin.poscision_elementos_preg1_triang_malo1(ventana)
                elif(ocultar==47):
                    prin.poscision_elementos_preg1_triang_malo2(ventana)
                elif(ocultar==48):
                    prin.poscision_elementos_preg2_triang(ventana)
                elif(ocultar==49):
                    prin.poscision_elementos_preg2_triang_bien(ventana)
                elif(ocultar==50):
                    prin.poscision_elementos_preg2_triang_malo1(ventana)
                elif(ocultar==51):
                    prin.poscision_elementos_preg2_triang_malo2(ventana)
                elif(ocultar==52):
                    prin.poscision_elementos_preg3_triang(ventana)
                elif(ocultar==53):
                    prin.poscision_elementos_preg3_triang_bien(ventana)
                elif(ocultar==54):
                    prin.poscision_elementos_preg3_triang_malo1(ventana)
                elif(ocultar==55):
                    prin.poscision_elementos_preg3_triang_malo2(ventana)
                elif(ocultar==56):
                    prin.poscision_elementos_preg4_triang(ventana)
                elif(ocultar==57):
                    prin.poscision_elementos_preg4_triang_bien(ventana)
                elif(ocultar==58):
                    prin.poscision_elementos_preg4_triang_malo1(ventana)
                elif(ocultar==59):
                    prin.poscision_elementos_preg4_triang_malo2(ventana)
                elif(ocultar==60):
                    prin.poscision_elementos_preg5_triang(ventana)
                elif(ocultar==61):
                    prin.poscision_elementos_preg5_triang_bien(ventana)
                elif(ocultar==62):
                    prin.poscision_elementos_preg5_triang_malo1(ventana)
                elif(ocultar==63):
                    prin.poscision_elementos_preg5_triang_malo2(ventana)
                elif(ocultar==64):
                    prin.poscision_elementos_preg6_triang(ventana)
                elif(ocultar==65):
                    prin.poscision_elementos_preg6_triang_bien(ventana)
                elif(ocultar==66):
                    prin.poscision_elementos_preg6_triang_malo1(ventana)
                elif(ocultar==67):
                    prin.poscision_elementos_preg6_triang_malo2(ventana)
                elif(ocultar==68):
                    prin.poscision_elementos_preg7_triang(ventana)
                elif(ocultar==69):
                    prin.poscision_elementos_preg7_triang_bien(ventana)
                elif(ocultar==70):
                    prin.poscision_elementos_preg7_triang_malo1(ventana)
                elif(ocultar==71):
                    prin.poscision_elementos_preg7_triang_malo2(ventana) 
                elif(ocultar==72):
                    prin.poscision_elementos_pregfin_triang(ventana)
                elif(ocultar==73):
                    prin.poscision_elementos_cuadra(ventana)
                elif(ocultar==74):
                    prin.poscision_elementos_cuadral(ventana)
                elif(ocultar==75):
                    prin.poscision_elementos_cuadrav(ventana)
                elif(ocultar==76):
                    prin.poscision_elementos_rect(ventana)
                elif(ocultar==77):
                    prin.poscision_elementos_rectv(ventana)
                elif(ocultar==78):
                    prin.poscision_elementos_rombo(ventana)
                elif(ocultar==79):
                    prin.poscision_elementos_rombov(ventana)
                elif(ocultar==80):
                    prin.poscision_elementos_trapecio(ventana)
                elif(ocultar==81):
                    prin.poscision_elementos_trapeciov(ventana)
                elif(ocultar==82):
                    prin.poscision_elementos_recbienve(ventana)
                elif(ocultar==83):
                    prin.poscision_elementos_preg1_rect(ventana)
                elif(ocultar==84):
                    prin.poscision_elementos_preg1_rect_bien(ventana)
                elif(ocultar==85):
                    prin.poscision_elementos_preg1_rect_malo1(ventana)
                elif(ocultar==86):
                    prin.poscision_elementos_preg1_rect_malo2(ventana)
                elif(ocultar==87):
                    prin.poscision_elementos_preg2_rect(ventana)
                elif(ocultar==88):
                    prin.poscision_elementos_preg2_rect_bien(ventana)
                elif(ocultar==89):
                    prin.poscision_elementos_preg2_rect_malo1(ventana)
                elif(ocultar==90):
                    prin.poscision_elementos_preg2_rect_malo2(ventana)
                elif(ocultar==91):
                    prin.poscision_elementos_preg3_rect(ventana)
                elif(ocultar==92):
                    prin.poscision_elementos_preg3_rect_bien(ventana)
                elif(ocultar==93):
                    prin.poscision_elementos_preg3_rect_malo1(ventana)
                elif(ocultar==94):
                    prin.poscision_elementos_preg3_rect_malo2(ventana)
                elif(ocultar==95):
                    prin.poscision_elementos_preg4_rect(ventana) 
                elif(ocultar==96):
                    prin.poscision_elementos_preg4_rect_bien(ventana) 
                elif(ocultar==97):
                    prin.poscision_elementos_preg4_rect_malo1(ventana)
                elif(ocultar==98):
                    prin.poscision_elementos_preg5_rect(ventana)
                elif(ocultar==99):
                    prin.poscision_elementos_preg5_rect_bien(ventana)
                elif(ocultar==100):
                    prin.poscision_elementos_preg5_rect_malo1(ventana)
                elif(ocultar==101):
                    prin.poscision_elementos_preg5_rect_malo2(ventana)
                elif(ocultar==102):
                    prin.poscision_elementos_preg6_rect(ventana) 
                elif(ocultar==103):
                    prin.poscision_elementos_preg6_rect_bien(ventana)
                elif(ocultar==104):
                    prin.poscision_elementos_preg6_rect_malo1(ventana)
                elif(ocultar==105):
                    prin.poscision_elementos_preg6_rect_malo2(ventana) 
            elif eventos.type == KEYDOWN:
                
                if eventos.key == K_ESCAPE:
                    
                    sys.exit(0)        
            
                                      
        if(ocultar==1):
            prin.inter_principal(ventana)
           
        elif (ocultar==2):
            prin.interfaz_menu(ventana)
        elif (ocultar==3):
            prin.interfaz_circulo(ventana)
        elif (ocultar==4):
            prin.interfaz_circuloc(ventana)
        elif (ocultar==5):
            prin.interfaz_circulor(ventana)
        elif (ocultar==6):
            prin.interfaz_triangulo(ventana)
        elif (ocultar==7):
            prin.interfaz_triangulol(ventana)
        elif (ocultar==8):
            prin.interfaz_triangulov(ventana)
        elif (ocultar==9):
            prin.interfaz_trianguloa(ventana)
        elif (ocultar==10):
            prin.interfaz_triangulob(ventana)
        elif (ocultar==11):
            prin.interfaz_triangulocla(ventana)
        elif (ocultar==12):
            prin.interfaz_circulobienvenida(ventana)
        elif (ocultar==13):
            prin.interfaz_ayuda(ventana)
        elif (ocultar==14):
            prin.interfaz_preg1_cir(ventana)
        elif (ocultar==15):
            prin.interfaz_preg1_cir_bien(ventana)
        elif (ocultar==16):
            prin.interfaz_preg1_cir_malo1(ventana)
        elif (ocultar==17):
            prin.interfaz_preg1_cir_malo2(ventana)
        elif (ocultar==18):
            prin.interfaz_preg2_cir(ventana)
        elif (ocultar==19):
            prin.interfaz_preg2_cir_bien(ventana)
        elif (ocultar==20):
            prin.interfaz_preg2_cir_malo1(ventana)
        elif (ocultar==21):
            prin.interfaz_preg2_cir_malo2(ventana)
        elif (ocultar==22):
            prin.interfaz_preg3_cir(ventana)
        elif (ocultar==23):
            prin.interfaz_preg3_cir_bien(ventana)
        elif (ocultar==24):
            prin.interfaz_preg3_cir_malo1(ventana)
        elif (ocultar==25):
            prin.interfaz_preg3_cir_malo2(ventana)
        elif (ocultar==26):
            prin.interfaz_preg4_cir(ventana)
        elif (ocultar==27):
            prin.interfaz_preg4_cir_bien(ventana)
        elif (ocultar==28):
            prin.interfaz_preg4_cir_malo1(ventana)
        elif (ocultar==29):
            prin.interfaz_preg4_cir_malo2(ventana)
        elif (ocultar==30):
            prin.interfaz_preg5_cir(ventana)
        elif (ocultar==31):
            prin.interfaz_preg5_cir_bien(ventana)
        elif (ocultar==32):
            prin.interfaz_preg5_cir_malo1(ventana)
        elif (ocultar==33):
            prin.interfaz_preg5_cir_malo2(ventana)
        elif (ocultar==34):
            prin.interfaz_preg6_cir(ventana)
        elif (ocultar==35):
            prin.interfaz_preg6_cir_bien(ventana)
        elif (ocultar==36):
            prin.interfaz_preg6_cir_malo1(ventana)
        elif (ocultar==37):
            prin.interfaz_preg6_cir_malo2(ventana)
        elif (ocultar==38):
            prin.interfaz_pregfin_cir(ventana)
        elif (ocultar==39):
            prin.interfaz_Bienvenida(ventana)
        elif (ocultar==40):
            prin.interfaz_trianguloequi(ventana)
        elif (ocultar==41):
            prin.interfaz_trianguloiso(ventana)
        elif (ocultar==42):
            prin.interfaz_trianguloesca(ventana)
        elif (ocultar==43):
            prin.interfaz_triangulobienve(ventana)
        elif (ocultar==44):
            prin.interfaz_preg1_triang(ventana)
        elif (ocultar==45):
            prin.interfaz_preg1_triang_bien(ventana)
        elif (ocultar==46):
            prin.interfaz_preg1_triang_malo1(ventana)
        elif (ocultar==47):
            prin.interfaz_preg1_triang_malo2(ventana)
        elif (ocultar==48):
            prin.interfaz_preg2_triang(ventana)
        elif (ocultar==49):
            prin.interfaz_preg2_triang_bien(ventana)
        elif (ocultar==50):
            prin.interfaz_preg2_triang_malo1(ventana)
        elif (ocultar==51):
            prin.interfaz_preg2_triang_malo2(ventana)
        elif (ocultar==52):
            prin.interfaz_preg3_triang(ventana)
        elif (ocultar==53):
            prin.interfaz_preg3_triang_bien(ventana)
        elif (ocultar==54):
            prin.interfaz_preg3_triang_malo1(ventana)
        elif (ocultar==55):
            prin.interfaz_preg3_triang_malo2(ventana)
        elif (ocultar==56):
            prin.interfaz_preg4_triang(ventana)
        elif (ocultar==57):
            prin.interfaz_preg4_triang_bien(ventana)
        elif (ocultar==58):
            prin.interfaz_preg4_triang_malo1(ventana)
        elif (ocultar==59):
            prin.interfaz_preg4_triang_malo2(ventana)
        elif (ocultar==60):
            prin.interfaz_preg5_triang(ventana)
        elif (ocultar==61):
            prin.interfaz_preg5_triang_bien(ventana)
        elif (ocultar==62):
            prin.interfaz_preg5_triang_malo1(ventana)
        elif (ocultar==63):
            prin.interfaz_preg5_triang_malo2(ventana)
        elif (ocultar==64):
            prin.interfaz_preg6_triang(ventana)
        elif (ocultar==65):
            prin.interfaz_preg6_triang_bien(ventana)
        elif (ocultar==66):
            prin.interfaz_preg6_triang_malo1(ventana)
        elif (ocultar==67):
            prin.interfaz_preg6_triang_malo2(ventana)
        elif (ocultar==68):
            prin.interfaz_preg7_triang(ventana)
        elif (ocultar==69):
            prin.interfaz_preg7_triang_bien(ventana)
        elif (ocultar==70):
            prin.interfaz_preg7_triang_malo1(ventana)
        elif (ocultar==71):
            prin.interfaz_preg7_triang_malo2(ventana)
        elif (ocultar==72):
            prin.interfaz_pregfin_triang(ventana)
        elif (ocultar==73):
            prin.interfaz_cuadra(ventana)
        elif (ocultar==74):
            prin.interfaz_cuadral(ventana)
        elif (ocultar==75):
            prin.interfaz_cuadrav(ventana)
        elif (ocultar==76):
            prin.interfaz_rect(ventana)
        elif (ocultar==77):
            prin.interfaz_rectv(ventana)
        elif (ocultar==78):
            prin.interfaz_rombo(ventana)
        elif (ocultar==79):
            prin.interfaz_rombov(ventana)
        elif (ocultar==80):
            prin.interfaz_trapecio(ventana)
        elif (ocultar==81):
            prin.interfaz_trapeciov(ventana)
        elif (ocultar==82):
            prin.interfaz_reclobienve(ventana)
        elif (ocultar==83):
            prin.interfaz_preg1_rect(ventana)
        elif (ocultar==84):
            prin.interfaz_preg1_rect_bien(ventana)
        elif (ocultar==85):
            prin.interfaz_preg1_rect_malo1(ventana)
        elif (ocultar==86):
            prin.interfaz_preg1_rect_malo2(ventana)
        elif (ocultar==87):
            prin.interfaz_preg2_rect(ventana)
        elif (ocultar==88):
            prin.interfaz_preg2_rect_bien(ventana)
        elif (ocultar==89):
            prin.interfaz_preg2_rect_malo1(ventana)
        elif (ocultar==90):
            prin.interfaz_preg2_rect_malo2(ventana)
        elif (ocultar==91):
            prin.interfaz_preg3_rect(ventana)
        elif (ocultar==92):
            prin.interfaz_preg3_rect_bien(ventana)
        elif (ocultar==93):
            prin.interfaz_preg3_rect_malo1(ventana)
        elif (ocultar==94):
            prin.interfaz_preg3_rect_malo2(ventana)
        elif (ocultar==95):
            prin.interfaz_preg4_rect(ventana)
        elif (ocultar==96):
            prin.interfaz_preg4_rect_bien(ventana)
        elif (ocultar==97):
            prin.interfaz_preg4_rect_malo1(ventana)
        elif (ocultar==98):
            prin.interfaz_preg5_rect(ventana)
        elif (ocultar==99):
            prin.interfaz_preg5_rect_bien(ventana)
        elif (ocultar==100):
            prin.interfaz_preg5_rect_malo1(ventana)
        elif (ocultar==101):
            prin.interfaz_preg5_rect_malo2(ventana)
        elif (ocultar==102):
            prin.interfaz_preg6_rect(ventana)
        elif (ocultar==103):
            prin.interfaz_preg6_rect_bien(ventana)
        elif (ocultar==104):
            prin.interfaz_preg6_rect_malo1(ventana)
        elif (ocultar==105):
            prin.interfaz_preg6_rect_malo2(ventana)
        pygame.display.update()
                    
if __name__ == '__main__':
    main()
