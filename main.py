import pygame
import math

pygame.init()

# time variables
clock = pygame.time.Clock()
FPS = 120
dt = 0

# display variables
screen_Width = 1500
screen_Height = 720
screen = pygame.display.set_mode((screen_Width, screen_Height))
pygame.display.set_caption("Macroplastics")
image = pygame.image.load("bg_21.png").convert()
image_Width = image.get_width()
player = pygame.image.load("ivas.png").convert()

# scrolling variables
scroll = 0
tiles = math.ceil(screen_Width / image_Width) + 1
print(tiles)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    for i in range(0, tiles):
        screen.blit(image, (i * image_Width + scroll,0))
    scroll -= 1.5
    
    if abs(scroll) > image_Width:
        scroll = 0

    pygame.display.update()

    dt = clock.tick(FPS) / 1000

pygame.quit()