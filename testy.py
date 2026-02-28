import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))

class bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 10)
        initSpeed = 3
    #x = screen.get_width()/2 #initial firing position
    
    def spawn(yI): #bullet and effects?
        bullet = pygame.Rect(x, yI, 30, 10)
        [pygame.draw.rect(screen, "black", bullet), pygame.Rect(bullet.x - 10, yI + random.randint(-5, 5), 10, 10)]
    
    def move():
        x += initSpeed

clock = pygame.time.Clock()
running = True
dt = 0
player_y = screen.get_height()/2
player_color = (0, 100, 50)
ymulti = 0 #accelerator for height
gravTime = True #bool for measuring if gravity is in effect
boostTS = 0
jumpTS = 0
shootTS = 0
drawTestSquare = False #test
list = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pygame.time.get_ticks() - boostTS >= 500:
        gravTime = True
        cdS = pygame.time.get_ticks()
        drawTestSquare = False
    
    screen.fill((0, 200, 255))
    if drawTestSquare:
        pygame.draw.rect(screen, (255, 0 , 255), pygame.Rect(screen.get_width()/2 - 40 + random.randint(-20, 20), player_y - 40 + random.randint(-40, 20), 80, 80))
    pygame.draw.circle(screen, player_color, (screen.get_width()/2, player_y), 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pygame.time.get_ticks() - jumpTS > 200 and gravTime:
        ymulti = 20
        jumpTS = pygame.time.get_ticks()
    
    if keys[pygame.K_f] and pygame.time.get_ticks() - shootTS > 300:
        shootTS = pygame.time.get_ticks()
        list.append(bullet. #make a new bullet from class bullet
    
    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - boostTS > 2000:
        ymulti = -2
        gravTime= False
        boostTS = pygame.time.get_ticks()
        drawTestSquare = True
     
    player_y -= ymulti
    
    if ymulti > -30 and gravTime:
        ymulti -= 2
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()