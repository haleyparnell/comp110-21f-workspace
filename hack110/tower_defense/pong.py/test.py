import pygame
from testpaddles import Paddle
from ball import Ball
from vector import Vector
import pygame_gui
pygame.init()
 
BLUE = (0, 191, 255)
WHITE = (255, 255, 255)

paddleB_color = WHITE 


gloria_position: Vector = Vector(50, 200)
gloria: Ball = Ball(gloria_position, paddleB_color, 8.0)

size = width, height = (700, 500)
FRAMES = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 500
paddleB.rect.y = 200
 
all_sprites_list = pygame.sprite.Group()
 
all_sprites_list.add(paddleB)
 
carryOn = True
 
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((width, height))
 
while carryOn:
    clock.tick(FRAMES)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            carryOn = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False  

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddleB.moveUp(60)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(60)  

    all_sprites_list.update()

    screen.fill(BLUE)
    
    pygame.draw.circle(screen, paddleB_color, (gloria.position.x, gloria.position.y), 10)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen) 
    pygame.display.flip()
    clock.tick(60)


pygame.quit()