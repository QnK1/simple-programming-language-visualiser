import time

a = 60

print(a/3*3)


l = [1,2,3,4]

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
font = pygame.font.SysFont(None, 48)
screen.fill((0, 0, 0))

text = "aaaBBBccc"
x, y = 50, 0

for char in text:
    color = (255, 0, 0) if char.isupper() else (255, 255, 255)
    rendered_char = font.render(char, True, color)
    screen.blit(rendered_char, (x, y))
    x += rendered_char.get_width()

pygame.display.flip()

# pauza żeby zobaczyć efekt
pygame.time.wait(5000)
pygame.quit()