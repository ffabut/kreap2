import pygame

pygame.init()

screen = pygame.display.set_mode([600, 400])

running = True

# souradnice cerveneho kruhu
rx = 50
ry = 50

# souradnice obdelniku
bx = 20
by = 20

# nekonecny loop, v nemz se odehrava aktualizace hry
while running:
  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # sipky ovlivnuji souradnice RX a RY cerveneho kruhu
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        rx = rx - 10
      if event.key == pygame.K_RIGHT:
        rx = rx + 10
      if event.key == pygame.K_UP:
        ry = ry - 10
      if event.key == pygame.K_DOWN:
        ry = ry + 10

  # pozice mysi urcuje souradnice BX a BY modreho kruhu
  bx, by = pygame.mouse.get_pos()

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  # vykreslime modry kruh
  pygame.draw.circle(screen, (0, 0, 255), (bx, by), 30)
  pygame.draw.circle(screen, (255, 0, 0), (rx, ry), 30)

  # update vykresleni obrazovky
  pygame.display.flip()


pygame.quit()