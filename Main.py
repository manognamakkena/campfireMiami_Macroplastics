import pygame
import math

pygame.init()

# time variables
clock = pygame.time.Clock()
FPS = 120
dt = 0

# display variables
screen_Width = 1080
screen_Height = 720
screen = pygame.display.set_mode((screen_Width, screen_Height))
pygame.display.set_caption("Macroplastics")
image = pygame.image.load("bg.png").convert()
image_Width = image.get_width()
# scrolling variables
scroll = 0 
tiles = math.ceil(screen_Width / image_Width) + 1

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0, tiles):
        screen.blit(image, (i * image_Width + scroll,0))
        scroll -= 2
    
    if abs(scroll) > image_Width:
        scroll = 0

    pygame.display.update()

    dt = clock.tick(FPS) / 1000

pygame.quit()