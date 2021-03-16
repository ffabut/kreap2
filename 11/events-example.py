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

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        print("left arrow pressed")
      if event.key == pygame.K_RIGHT:
        print("right arrow pressed")
      if event.key == pygame.K_UP:
        print("up arrow pressed")
      if event.key == pygame.K_DOWN:
        print("down arrow pressed")

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  # vykreslime modry kruh
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  # update vykresleni obrazovky
  pygame.display.flip()


pygame.quit()