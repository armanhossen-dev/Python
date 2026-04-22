import pygame
import sys
import math

# Constants
WIN_W = 900
WIN_H = 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

class StarDrawer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption("Star Drawing - Bresenham Line Algorithm")
        self.clock = pygame.time.Clock()
        self.points = []
        
    def pt_add(self, x, y):
        self.points.append((x, y))
    
    def flush_points(self, color):
        for point in self.points:
            if 0 <= point[0] < WIN_W and 0 <= point[1] < WIN_H:
                self.screen.set_at((point[0], point[1]), color)
        self.points = []
    
    def bresenham_line(self, x0, y0, x1, y1):
        """Draw line using Bresenham's algorithm"""
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        
        while True:
            self.pt_add(x0, y0)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy
    
    def draw_polygon(self, vertices, color):
        """Draw polygon using Bresenham lines"""
        for i in range(len(vertices)):
            x0, y0 = vertices[i]
            x1, y1 = vertices[(i + 1) % len(vertices)]
            self.bresenham_line(x0, y0, x1, y1)
        self.flush_points(color)
    
    def draw_star_5_point(self, cx, cy, outer_r, inner_r, color, filled=False):
        """Draw a 5-pointed star"""
        vertices = []
        for i in range(10):
            # Alternate between outer and inner radius
            r = outer_r if i % 2 == 0 else inner_r
            angle = math.radians(90 - i * 36)  # Start from top
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            vertices.append((int(x), int(y)))
        
        if filled:
            self.fill_polygon_scanline(vertices, color)
        else:
            self.draw_polygon(vertices, color)
    
    def draw_star_6_point(self, cx, cy, r, color, filled=False):
        """Draw a 6-pointed star (Star of David)"""
        vertices = []
        for i in range(6):
            angle = math.radians(90 - i * 60)
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            vertices.append((int(x), int(y)))
        
        # Create two triangles
        triangle1 = [vertices[0], vertices[2], vertices[4]]
        triangle2 = [vertices[1], vertices[3], vertices[5]]
        
        if filled:
            self.fill_polygon_scanline(triangle1, color)
            self.fill_polygon_scanline(triangle2, color)
        else:
            self.draw_polygon(triangle1, color)
            self.draw_polygon(triangle2, color)
    
    def draw_star_8_point(self, cx, cy, outer_r, inner_r, color, filled=False):
        """Draw an 8-pointed star"""
        vertices = []
        for i in range(16):
            r = outer_r if i % 2 == 0 else inner_r
            angle = math.radians(90 - i * 22.5)
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            vertices.append((int(x), int(y)))
        
        if filled:
            self.fill_polygon_scanline(vertices, color)
        else:
            self.draw_polygon(vertices, color)
    
    def fill_polygon_scanline(self, vertices, color):
        """Fill a polygon using scanline algorithm"""
        # Find y bounds
        y_min = min(v[1] for v in vertices)
        y_max = max(v[1] for v in vertices)
        
        # For each scanline
        for y in range(y_min, y_max + 1):
            intersections = []
            for i in range(len(vertices)):
                x1, y1 = vertices[i]
                x2, y2 = vertices[(i + 1) % len(vertices)]
                
                # Check if edge crosses this scanline
                if (y1 <= y < y2) or (y2 <= y < y1):
                    if (y2 - y1) != 0:
                        x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                        intersections.append(int(x))
            
            intersections.sort()
            # Draw horizontal lines between pairs of intersections
            for i in range(0, len(intersections), 2):
                if i + 1 < len(intersections):
                    self.bresenham_line(intersections[i], y, intersections[i + 1], y)
        
        self.flush_points(color)
    
    def draw_star_pattern(self):
        """Draw multiple star patterns"""
        self.screen.fill(WHITE)
        
        # Title
        font = pygame.font.Font(None, 36)
        title = "Star Patterns using Bresenham Line Algorithm"
        title_surface = font.render(title, True, BLACK)
        title_rect = title_surface.get_rect(center=(WIN_W // 2, 40))
        self.screen.blit(title_surface, title_rect)
        
        # 5-point star (outline) - Top Left
        self.draw_star_5_point(WIN_W // 4, WIN_H // 3, 70, 30, RED, filled=False)
        
        # 5-point star (filled) - Top Right
        self.draw_star_5_point(3 * WIN_W // 4, WIN_H // 3, 70, 30, GOLD, filled=True)
        
        # 6-point star (filled) - Center
        self.draw_star_6_point(WIN_W // 2, 2 * WIN_H // 3, 70, BLUE, filled=True)
        
        # 8-point star (outline) - Bottom Left
        self.draw_star_8_point(WIN_W // 4, 2 * WIN_H // 3, 70, 30, PURPLE, filled=False)
        
        # 8-point star (filled) - Bottom Right
        self.draw_star_8_point(3 * WIN_W // 4, 2 * WIN_H // 3, 70, 30, ORANGE, filled=True)
        
        # Labels
        font_small = pygame.font.Font(None, 20)
        labels = [
            ("5-point (Outline)", WIN_W // 4, WIN_H // 3 - 50),
            ("5-point (Filled)", 3 * WIN_W // 4, WIN_H // 3 - 50),
            ("6-point (Filled)", WIN_W // 2, 2 * WIN_H // 3 - 50),
            ("8-point (Outline)", WIN_W // 4, 2 * WIN_H // 3 - 50),
            ("8-point (Filled)", 3 * WIN_W // 4, 2 * WIN_H // 3 - 50)
        ]
        
        for label, x, y in labels:
            text = font_small.render(label, True, BLACK)
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)
        
        # Instructions
        font_inst = pygame.font.Font(None, 18)
        inst = "Press ESC to exit"
        inst_surface = font_inst.render(inst, True, BLACK)
        inst_rect = inst_surface.get_rect(center=(WIN_W // 2, WIN_H - 20))
        self.screen.blit(inst_surface, inst_rect)
        
        pygame.display.flip()
    
    def run(self):
        self.draw_star_pattern()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    star_drawer = StarDrawer()
    star_drawer.run()