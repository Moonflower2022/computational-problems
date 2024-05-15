import pygame
import sys
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def radius_1b(x, y):
    if math.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) >= 0.5:
        return 0.5
    if x < 0.5:
        x = 1 - x
    if y < 0.5:
        y = 1 - y
    return x + y - math.sqrt(2 * x * y)

def center_1b(r, x, y):
    print(x, y)
    center_x = r if x >= 0.5 else 1 - r
    center_y = r if y >= 0.5 else 1 - r
    return (center_x, center_y)

def two_blockers(blocker1, blocker2):
    pass

def draw_scene(center, radius, blocker1, blocker2):
    # Clear the screen
    screen.fill(WHITE)
    # Draw the square
    pygame.draw.rect(screen, BLACK, (0, 0, SCALE_FACTOR, SCALE_FACTOR), 2)
    # Draw the circle
    pygame.draw.circle(screen, BLACK, (center[0] * SCALE_FACTOR, center[1] * SCALE_FACTOR), int(radius * SCALE_FACTOR), 2)
    # Draw the points
    pygame.draw.circle(screen, RED, blocker1, 5, 5)
    pygame.draw.circle(screen, BLUE, blocker2, 5, 5)

    # Display the area of the circle
    font = pygame.font.Font(None, 36)
    text = font.render(f"Circle Area: {math.pi * radius ** 2:.3f}", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT - 50))
    screen.blit(text, text_rect)

def get_coordinates(mouse_pos, scale_factor):
    return mouse_pos[0] / scale_factor, mouse_pos[1] / scale_factor

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
SCALE_FACTOR = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Largest Circle in Square")

selected = 1

blocker1 = (0.4, 0.6)
blocker2 = (0.7, 0.1)
center, radius = two_blockers(blocker1, blocker2)

clock = pygame.time.Clock()
running = True

draw_scene(center, radius, blocker1, blocker2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if selected == 1:
                blocker1 = get_coordinates(pygame.mouse.get_pos())
            elif selected == 2:
                blocker2 = get_coordinates(pygame.mouse.get_pos())
            else:
                raise Exception()

            center, radius = two_blockers(blocker1, blocker2)
            draw_scene(center, radius, blocker1, blocker2)
            
            pygame.display.flip()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected = 1
            if event.key == pygame.K_2:
                selected = 2

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

