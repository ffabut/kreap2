import pygame

pygame.init()

screen = pygame.display.set_mode([600, 400])

running = True

# nekonecny loop, v nemz se odehrava aktualizace hry

x = 250
y = 250
v = (1, 0)
while running:

  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        v = (-1, 0)
        print("left arrow pressed")
      if event.key == pygame.K_RIGHT:
        v = (1, 0)
        print("right arrow pressed")
      if event.key == pygame.K_UP:
        v = (0, -1)
        print("up arrow pressed")
      if event.key == pygame.K_DOWN:
        v = (0, 1)
        print("down arrow pressed")

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  # vykreslime modry kruh
  x = x + v[0]
  y = y + v[1]
  pygame.draw.circle(screen, (0, 0, 255), (x, y), 75)

  # update vykresleni obrazovky
  pygame.display.flip()

  if x > 600 or x < 0 or y > 400 or y < 0:
    running = False


pygame.quit()