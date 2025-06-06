import pygame
import random
import math

# Inicialización
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrera de Autos")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Jugadores
PLAYER_SPEED = 5
BOOST_AMOUNT = 3
car_width, car_height = 40, 60

class Car:
    def __init__(self, x, color, is_player=False):
        self.x = x
        self.y = HEIGHT - 100
        self.speed = PLAYER_SPEED
        self.color = color
        self.is_player = is_player
        self.rect = pygame.Rect(self.x, self.y, car_width, car_height)

    def move(self, keys):
        if self.is_player:
            if keys[pygame.K_a] and self.rect.left > 300:
                self.rect.x -= 5
            if keys[pygame.K_d] and self.rect.right < 500:
                self.rect.x += 5
        else:
            self.rect.x += random.choice([-1, 0, 1])

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)

    def update(self, speed):
        self.rect.y += speed

    def draw(self):
        pygame.draw.ellipse(screen, YELLOW, self.rect)

# Crear autos
player = Car(370, RED, True)
npc1 = Car(320, (0, 0, 255))
npc2 = Car(420, (0, 255, 0))
cars = [player, npc1, npc2]

# Monedas
coins = []
spawn_timer = 0

# Fondo en movimiento (carretera)
def draw_road(offset):
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (300, 0, 200, HEIGHT))
    for i in range(20):
        pygame.draw.rect(screen, WHITE, (395, (i * 60 + offset) % HEIGHT, 10, 30))

# Juego principal
offset = 0
start_ticks = pygame.time.get_ticks()
run = True
winner = None
while run:
    clock.tick(60)
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds > 60:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Fondo
    offset += player.speed
    draw_road(offset)

    # Monedas
    spawn_timer += 1
    if spawn_timer > 30:
        coin_x = random.randint(310, 470)
        coins.append(Coin(coin_x, -20))
        spawn_timer = 0

    for coin in coins[:]:
        coin.update(player.speed)
        coin.draw()
        if player.rect.colliderect(coin.rect):
            player.speed += BOOST_AMOUNT
            coins.remove(coin)

    # Autos
    for car in cars:
        car.move(keys)
        car.update()
        car.draw()
        if car.rect.top < 0:
            winner = car
            run = False

    pygame.display.flip()

# Mostrar resultado
font = pygame.font.SysFont(None, 60)
if winner == player:
    text = font.render("Ganaste!", True, RED)
elif winner:
    text = font.render("Perdiste!", True, RED)
else:
    text = font.render("Tiempo agotado!", True, RED)
screen.fill(WHITE)
screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()