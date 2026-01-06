import pygame
import random

pygame.init()

width = 400
height = 300    
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

circle = pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, (30, 30))

rect_image = pygame.image.load("rect.png")
rect_image = pygame.transform.scale(rect_image, (70, 70))

background_img = pygame.image.load("background.png")
background_img= pygame.transform.scale(background_img, (width, height))

circle_x = random.randint(0, width)
circle_y = 0
circle_r=20     
rect_h = 70
rect_w = 70

velocity_x = random.randint(0, width)
velocity_y = height -rect_h

score = 0
missed = 0
open = True

rect_x = width // 2 - rect_w // 2
rect_y = height - rect_h

while open:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect_x += 5
    if keys[pygame.K_LEFT]:
        rect_x -= 5

    rect_x = max(0, min(rect_x, width - rect_w))

    circle_y += 5

    if (rect_y <= circle_y + circle_r <= rect_y + rect_h) and \
       (rect_x <= circle_x <= rect_x + rect_w):
        score += 1
        circle_x = random.randint(0, width - circle_r)
        circle_y = 0

    elif circle_y + circle_r >= height:
        missed += 1
        circle_x = random.randint(0, width - circle_r)
        circle_y = 0

    screen.blit(background_img, (0, 0))
    screen.blit(rect_image, (rect_x, rect_y))
    screen.blit(circle, (circle_x, circle_y))
    pygame.display.update()

    print("Your Score: ", score)
    print("Your Missed: ", missed)

pygame.quit()   