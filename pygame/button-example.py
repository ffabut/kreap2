import pygame
import sys

pygame.init()

clock=pygame.time.Clock()

window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Clickable Button')


button_surface = pygame.Surface((150, 50))
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

# Render text on the button
font = pygame.font.Font(None, 24)
text = font.render("Click Me", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))


# Create a pygame.Rect object that represents the button's boundaries



while True:
    clock.tick(60) # Set the frame rate
    screen.fill((155, 155, 155))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if mouse is pressed over button_rect
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # HOVER EFFECT
    if button_rect.collidepoint(pygame.mouse.get_pos()): #if mouse is above button
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    # Show the button text on the button surface
    button_surface.blit(text, text_rect)

    # Draw the button surface on the screen surface
    screen.blit(button_surface, (button_rect.x, button_rect.y))


    pygame.display.update() # Update the game state, alternative to flip(), we can use both
