import pygame

pygame.init()

import random


screen = pygame.display.set_mode([600, 400])

running = True


i = 0
while running:
  i = i + 1
  if i > 255:
    i = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #screen.fill((255, 255, 255))
  a = random.randint(0, 600)
  b = random.randint(0, 400)
  pygame.draw.circle(screen, (i, i, 255), (a, b), 10)

  pygame.display.flip()


pygame.quit()
