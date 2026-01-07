import pygame
import random as r

pygame.init()

width = 600
height = 500    
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the ball")

circle = pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, (30, 30))

rect_image = pygame.image.load("dash-cut1.png")
rect_image = pygame.transform.scale(rect_image, (120, 80))

background_img = pygame.image.load("background1.jpg")
background_img = pygame.transform.scale(background_img, (width, height))

circle_x = r.randint(0, width)
circle_y = 0
circle_r = 30    

rect_h = 70
rect_w = 70

rect_x = r.randint(0, width - rect_w)
rect_y = height - rect_h

# --------------------
# GAME VARIABLES
# --------------------
score = 0
missed = 0
level = 1

ball_speed = 5
speed_increase = 1

open = True
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

while open:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect_x += 7
    if keys[pygame.K_LEFT]:
        rect_x -= 7

    rect_x = max(0, min(rect_x, width - rect_w))

    # Ball movement (speed changes with level)
    circle_y += ball_speed

    # Catch condition
    if (rect_y <= circle_y + circle_r <= rect_y + rect_h) and \
       (rect_x <= circle_x <= rect_x + rect_w):
        score += 1
        circle_x = r.randint(0, width - circle_r)
        circle_y = 0

        if score % 5 == 0:
            level += 1
            ball_speed += speed_increase

    elif circle_y + circle_r >= height:
        missed += 1
        circle_x = r.randint(0, width - circle_r)
        circle_y = 0

    screen.blit(background_img, (0, 0))
    screen.blit(rect_image, (rect_x, rect_y))
    screen.blit(circle, (circle_x, circle_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    missed_text = font.render(f"Missed: {missed}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    screen.blit(missed_text, (10, 70))

    pygame.display.update()

pygame.quit()
