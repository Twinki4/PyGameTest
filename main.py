import pygame
import random

pygame.init()

win_width = 600
win_height = 400
a = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("MyGame")

width = 40
height = 60
x = 50
y = win_height - height - 10
speed = 5

jump = False
jumpCount = 10

run = True

red = 0
green = 0
blue = 0


def col():
    global red
    global green
    global blue
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)


while run:
    pygame.time.delay(10)
    col()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x != 0:
            x -= speed
    if keys[pygame.K_RIGHT]:
        if x + width != win_width:
            x += speed
    if not jump:
        if keys[pygame.K_UP]:
            if y != 0:
                y -= speed
        if keys[pygame.K_DOWN]:
            if y + height != win_height - 10:
                y += speed
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10

    a.fill((0, 0, 0))
    pygame.draw.rect(a, (red, green, blue), (x, y, width, height))
    pygame.draw.polygon(a, (red, green, blue), ([100, 100], [120, 50], [140, 100], [100, 65], [140, 65]), 3)
    pygame.display.update()

pygame.quit()