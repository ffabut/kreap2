import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 400])

running = True



# nekonecny loop, v nemz se odehrava aktualizace hry
while running:
  clock.tick(1000)
  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # nastaveni bileho pozadi okna
  # screen.fill((255, 255, 255))

  x = random.randint(0, 600)
  y = random.randint(0, 400)
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  myfont = pygame.font.SysFont('Comic Sans MS', 40)
  textsurface = myfont.render('FaVU life', False, (r, g, b))



  screen.blit(textsurface,(x,y))

  pygame.display.flip()


pygame.quit()