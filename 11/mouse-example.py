import pygame

pygame.init()

screen = pygame.display.set_mode([600, 400])

running = True

# nekonecny loop, v nemz se odehrava aktualizace hry
while running:

  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  x, y = pygame.mouse.get_pos()
  print(x,y)

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  # vykreslime modry kruh
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  # update vykresleni obrazovky
  pygame.display.flip()


pygame.quit()