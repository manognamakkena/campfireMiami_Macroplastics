import sys
import os
import math
import random
import pygame

def resource_path():
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Macroplastics")    

class bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 10)
        self.speed = 1
        
    def move(self):
        self.rect.x += self.speed
        if self.speed < 15:
            self.speed += .5
    
    def draw(self, surface):
        pygame.draw.rect(surface, "black", self.rect)
        pygame.draw.rect(surface, (200, 200, 255), pygame.Rect(self.rect.x - 10 + random.randint(-20, 30), self.rect.y + random.randint(-20, 30), 9, 9))

class sBul():
    def __init__(self, x, y):
        self.Rect = pygame.Rect(x, y, 30, 10)
        self.speed = 10
        
    def move(self):
        self.Rect.x -= self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 255), self.Rect)
        pygame.draw.rect(surface, (200, 200, 255), pygame.Rect(self.Rect.x + 40 + random.randint(-20, 30), self.Rect.y + random.randint(-20, 30), 9, 9))
        

class obstacle():
    def __init__(self, y):
        self.hb = pygame.Rect(self.x, self.y, 60, 60)

class squid():
    def __init__(self, y, speed, sprite, fireRate, surface):
        self.hb = pygame.Rect(screx, y, 60, 60)
        self.sShootTS = pygame.time.get_ticks()
        self.bulLs = []
        self.up = bool(random.randint(0,1))
        self.vSpeed = speed
        self.sprite = sprite
        self.firerate = fireRate
        self.screen = surface
            
    def scroll(self):
        if self.hb.x <= screx/2 - squidSPrite.get_width()/2:
            self.hb.x -= 12
        else:
            self.hb.x -= 3
        
    def move(self):
        if self.hb.y < 0:
            self.up = False
        if self.hb.y + squidSPrite.get_height()/2 > screy:
            self.up = True
        if self.up:
            self.hb.y -= self.vSpeed
        else:
            self.hb.y += self.vSpeed
    def draw(self):
        self.screen.blit(pygame.transform.rotate(self.sprite, ((sq.hb.x%10000)/1000 - 5)*10/5 ), (sq.hb.x, sq.hb.y))
    def shoot(self):
        if pygame.time.get_ticks() - self.sShootTS > self.firerate:
            self.bulLs.append(sBul(self.hb.x, self.hb.y))
            self.sShootTS = pygame.time.get_ticks()
        for i in self.bulLs:
            i.move()
            i.draw(self.screen)
            #kills player
            if playerSprite.get_rect(center=(screx/2, player_y)).colliderect(i.Rect):
                deatSound.play()
                score = 0
                for i in range(0, 10):
                    screen.blit(deathmg, (0,0))
       
            if i.Rect.x < 30:
                sq.bulLs.remove(i)
                
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

deatSound = pygame.mixer.Sound("hurtSound.mp3")
killS = pygame.mixer.Sound("killSound.mp3")
pygame.mixer.music.load("music.mp3")

bg = pygame.image.load("bg_21.png").convert()
deathmg = pygame.image.load("deyied.png")
playerSprite = pygame.image.load("ivas.png")
gojoSprite = pygame.image.load("coolIvas.png")
squidSPrite = pygame.image.load("jellyfish.png")
squidSPriteG = pygame.image.load("jellyfishG.png")
squidSPriteR = pygame.image.load("jellyfishR.png")
gunSprite = pygame.image.load("gun.png")
title_image = pygame.image.load("title.png")

gojo = False
game = True
gravTime = True #bool for measuring if gravity is in effect
playable = True
deathB = True
spawnB = True

bulList = []
enemya = []

screx = screen.get_width()
screy = screen.get_height()

dt = 0
scroll = 0
player_y = -40
ymulti = 0 #accelerator for height
boostTS = 0
jumpTS = 0
shootTS = 0
obsType = -1
obsTS = 5000
score = 0
scoremsg = "Score: " + str(score)
scroll1 = 0

tiles = math.ceil(720 / bg.get_width()) + 1

pygame.mixer.music.play(-1)
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    if pygame.time.get_ticks() - boostTS >= 500:
        gravTime = True
        cdS = pygame.time.get_ticks()
        gojo = False
        drawTestSquare = False
    
    for i in range(0, tiles):
        screen.blit(bg, (i * bg.get_width() + scroll,0))
    scroll -= 1.5
    
    for i in range(0, 1):
        screen.blit(title_image, (250 + scroll1, 200))
    scroll1 -= 2
    
    if abs(scroll) > bg.get_width():
        scroll = 0
    
    screen.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (50, 50))
    
    if spawnB:
        obsType = random.randint(0, 2)
        if obsType == 0:
            enemya.append(squid(random.randint(0, screy), 4, squidSPrite, 800, screen))
        if obsType == 1:
            enemya.append(squid(random.randint(0, screy), 6, squidSPriteG, 4000, screen))
        if obsType == 2:
            enemya.append(squid(random.randint(0, screy), 3, squidSPriteR, 500, screen))
        spawnB = False
    
    for sq in enemya:
        print(sq.hb.x)
        sq.draw()
        sq.move()
        sq.scroll()
        sq.shoot()
        #kills player
        if playerSprite.get_rect(center=(screx/2, player_y)).colliderect(sq.hb):
            pygame.mixer.music.stop()
            deatSound.play()
            score = 0
            for i in range(0, 10):
                screen.blit(deathmg, (0,0))
        if sq.hb.x < 0 - 60:
            enemya.remove(sq)
            spawnB = True

    if gojo:
        screen.blit(pygame.transform.rotate(gojoSprite, pygame.time.get_ticks()%10), (screx/2 - playerSprite.get_width()/2, player_y - playerSprite.get_height()/2))
    else:
        screen.blit(pygame.transform.rotate(playerSprite, ymulti * 22/20), (screx/2 - playerSprite.get_width()/2, player_y - playerSprite.get_height()/2))        
    for bul in bulList:
        bul.move()
        bul.draw(screen)
        if bul.rect.x > 1280:
            bulList.remove(bul)
    screen.blit(gunSprite, (screx/2 - 4, player_y - 10))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pygame.time.get_ticks() - jumpTS > 200 and gravTime:
        ymulti = 25
        jumpTS = pygame.time.get_ticks()
    
    if keys[pygame.K_f] and pygame.time.get_ticks() - shootTS > 300:
        shootTS = pygame.time.get_ticks()
        bulList.append(bullet(screx/2 + 1, player_y)) #make a new bullet from class bullet
    
    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - boostTS > 2000:
        gojo = True
        ymulti = -2
        gravTime= False
        boostTS = pygame.time.get_ticks()
        drawTestSquare = True

    player_y -= ymulti
    
    if ymulti > -30 and gravTime:
        ymulti -= 1.5
    
    if player_y < -50 and playable:
        player_y = 760
        multiy = 60
    if player_y > 770:
        player_y = -40
    
    for bul in bulList:
        for sq in enemya:
            if bul.rect.colliderect(sq.hb):
                killS.play()
                bulList.remove(bul)
                enemya.remove(sq)
                spawnB = True
                score += 1
                break

    pygame.display.flip()
    dt = clock.tick(60) / 1000    
    
pygame.quit()