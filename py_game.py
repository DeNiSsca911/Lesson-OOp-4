from operator import truediv

import pygame
pygame.init()
import time

window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Текстовый проект")

image = pygame.image.load("sm.png")
image_rect = image.get_rect()

image2 = pygame.image.load("pit.png")
image_rect2 = image2.get_rect()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 30
            image_rect.y = mouseY - 30

    if image_rect.colliderect(image_rect2):
        print("Произошло столкновение !")
        time.sleep(1)


    screen.fill((0,0,0))
    screen.blit(image,image_rect)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.QUIT
