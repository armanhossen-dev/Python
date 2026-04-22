import pygame
import sys

# Constants
W, H = 800, 600
BG = (26, 26, 31)
LINE_COLOR = (255, 77, 217)

def bresenham_line(x0, y0, x1, y1):
    """Bresenham's Line Algorithm - Returns list of points"""
    points = []
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    
    return points

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bresenham Line Algorithm")
clock = pygame.time.Clock()

# Draw lines
screen.fill(BG)

# Test lines
test_lines = [
    (50, 80, 750, 520),      # Diagonal
    (80, 500, 720, 120),     # Cross diagonal
    (400, 50, 400, 550),     # Vertical
    (100, 300, 700, 310),    # Almost horizontal
]

for x1, y1, x2, y2 in test_lines:
    points = bresenham_line(x1, y1, x2, y2)
    for point in points:
        screen.set_at(point, LINE_COLOR)

# Draw text
font = pygame.font.Font(None, 15)
text = "Bresenham's Line Algorithm (Integer-only)"
text_surface = font.render(text, True, (217, 217, 217))
screen.blit(text_surface, (20, H - 28))

pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    clock.tick(60)