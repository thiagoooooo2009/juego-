import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Asteroids con POO")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Amarillo = (255,255,0)

class Asteroide:
    def ___init___(self):
        self.x = random.randint(50, WIDTH -50)
        self.y = 0 
        self.velocidad = random.randint(2, 5)
        self.radio = 20 
        
    def mover(self):
        self.y += self.velocidad 
        
    def dibujar (self, superficie):
        pygame.draw.circle(superficie,WHITE, (self.x, self.y), self.radio)
Asteroide = Asteroide()       
while True:
    screen.fill(BLACK)
    # Posibles entradas del teclado y mouse
    for event in pygame.event.get():
        if event.type == pygame.quit:       
            sys.exit()
    
    Asteroide.mover()
    
    Asteroide.dibujar(screen)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit
sys.exit






