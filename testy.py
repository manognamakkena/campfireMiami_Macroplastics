import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Macroplastics")

class bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 10)
        self.speed = 1
        
    def move(self):
        self.rect.x += self.speed
        if self.speed < 15:
            self.speed += 1
    
    def draw(self, surface):
        pygame.draw.rect(surface, "blue", self.rect)

clock = pygame.time.Clock()
bg = pygame.image.load("bg_21.png").convert()
playerSprite = pygame.image.load("ivas.png")

running = True
gravTime = True #bool for measuring if gravity is in effect
playable = False
drawTestSquare = False #test

bulList = []

screx = screen.get_width()
screy = screen.get_height()

dt = 0
scroll = 0
player_y = -40
ymulti = 0 #accelerator for height
boostTS = 0
jumpTS = 0
shootTS = 0
tiles = math.ceil(720 / bg.get_width()) + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pygame.time.get_ticks() - boostTS >= 500:
        gravTime = True
        cdS = pygame.time.get_ticks()
        drawTestSquare = False
    
    for i in range(0, tiles):
        screen.blit(bg, (i * bg.get_width() + scroll,0))
    scroll -= 1.5
    
    if abs(scroll) > bg.get_width():
        scroll = 0
    
    for bul in bulList:
        bul.move()
        bul.draw(screen)
        if bul.rect.x > 1280:
            bulList.remove(bul)
    if drawTestSquare:
        pygame.draw.rect(screen, (255, 0 , 255), pygame.Rect(screx/2 - 40 + random.randint(-20, 20), player_y - 40 + random.randint(-40, 20), 80, 80))
    #pygame.draw.circle(screen, (0, 255, 100), (screx/2, player_y), 40)
    screen.blit(pygame.transform.rotate(playerSprite, -ymulti * 180/20), (screx/2 - playerSprite.get_width()/2, player_y - playerSprite.get_height()/2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pygame.time.get_ticks() - jumpTS > 200 and gravTime:
        ymulti = 25
        jumpTS = pygame.time.get_ticks()
    
    if keys[pygame.K_f] and pygame.time.get_ticks() - shootTS > 300:
        shootTS = pygame.time.get_ticks()
        bulList.append(bullet(screx/2 + 1, player_y)) #make a new bullet from class bullet
    
    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - boostTS > 2000:
        ymulti = -2
        gravTime= False
        boostTS = pygame.time.get_ticks()
        drawTestSquare = True
     
    player_y -= ymulti
    
    if ymulti > -30 and gravTime:
        ymulti -= 1.5
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()