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

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  img = pygame.image.load("favulife.jpg")
  screen.blit(img, (50, 50))

  pygame.display.flip()


pygame.quit()