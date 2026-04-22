import pygame
import sys
import math

# Constants
WIN_W = 900
WIN_H = 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 106, 78)      # Official Bangladesh flag green
RED = (244, 42, 65)       # Official Bangladesh flag red

class BangladeshFlag:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption("Flag of Bangladesh - Midpoint Circle Algorithm")
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
    
    def midpoint_circle(self, cx, cy, r):
        """Draw circle using midpoint algorithm"""
        x = 0
        y = r
        d = 1 - r
        
        while x <= y:
            points = [
                (cx + x, cy + y), (cx - x, cy + y),
                (cx + x, cy - y), (cx - x, cy - y),
                (cx + y, cy + x), (cx - y, cy + x),
                (cx + y, cy - x), (cx - y, cy - x)
            ]
            for px, py in points:
                self.pt_add(px, py)
            
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1
    
    def fill_circle(self, cx, cy, r, color):
        """Fill circle by drawing concentric rings"""
        for ri in range(r, -1, -1):
            self.midpoint_circle(cx, cy, ri)
        self.flush_points(color)
    
    def fill_rectangle(self, x, y, w, h, color):
        """Fill rectangle using scanlines"""
        for i in range(w):
            self.bresenham_line(x + i, y, x + i, y + h)
        self.flush_points(color)
    
    def draw_flag(self):
        """Draw the national flag of Bangladesh"""
        # Clear screen to WHITE
        self.screen.fill(WHITE)
        
        # Flag proportions: Length:Width = 10:6
        flag_width = 600
        flag_height = 360
        start_x = (WIN_W - flag_width) // 2
        start_y = (WIN_H - flag_height) // 2
        
        # Draw green rectangle (the flag)
        self.fill_rectangle(start_x, start_y, flag_width, flag_height, GREEN)
        
        # Calculate circle dimensions
        # Circle radius = Length/5 = flag_width/5
        # Circle center at Length/2.5 from hoist (left side)
        circle_radius = flag_width // 5
        circle_center_x = start_x + (flag_width * 2 // 5)
        circle_center_y = start_y + (flag_height // 2)
        
        # Draw red circle
        self.fill_circle(circle_center_x, circle_center_y, circle_radius, RED)
        
        # Draw black border around the flag (for definition)
        self.bresenham_line(start_x, start_y, start_x + flag_width, start_y)
        self.bresenham_line(start_x + flag_width, start_y, start_x + flag_width, start_y + flag_height)
        self.bresenham_line(start_x + flag_width, start_y + flag_height, start_x, start_y + flag_height)
        self.bresenham_line(start_x, start_y + flag_height, start_x, start_y)
        self.flush_points(BLACK)
        
        # Add title
        font_title = pygame.font.Font(None, 36)
        title = "National Flag of Bangladesh"
        title_surface = font_title.render(title, True, BLACK)
        title_rect = title_surface.get_rect(center=(WIN_W // 2, 50))
        self.screen.blit(title_surface, title_rect)
        
        # Add information
        font_info = pygame.font.Font(None, 20)
        info1 = "Green Background: Symbolizes the lushness of the land"
        info2 = "Red Circle: Symbolizes the blood of those who sacrificed for independence"
        info3 = "Drawn using Midpoint Circle Algorithm & Bresenham Line Algorithm"
        
        info_surface1 = font_info.render(info1, True, BLACK)
        info_surface2 = font_info.render(info2, True, BLACK)
        info_surface3 = font_info.render(info3, True, BLACK)
        
        info_rect1 = info_surface1.get_rect(center=(WIN_W // 2, WIN_H - 80))
        info_rect2 = info_surface2.get_rect(center=(WIN_W // 2, WIN_H - 55))
        info_rect3 = info_surface3.get_rect(center=(WIN_W // 2, WIN_H - 30))
        
        self.screen.blit(info_surface1, info_rect1)
        self.screen.blit(info_surface2, info_rect2)
        self.screen.blit(info_surface3, info_rect3)
        
        # Flag specifications
        font_spec = pygame.font.Font(None, 16)
        spec = "Specifications: Length:Width = 10:6 | Circle radius = Length/5 | Circle center at Length/2.5 from hoist"
        spec_surface = font_spec.render(spec, True, BLACK)
        spec_rect = spec_surface.get_rect(center=(WIN_W // 2, WIN_H - 10))
        self.screen.blit(spec_surface, spec_rect)
        
        pygame.display.flip()
    
    def draw_simple_flag(self):
        """Simpler version without text - just the flag"""
        self.screen.fill(WHITE)
        
        flag_width = 600
        flag_height = 360
        start_x = (WIN_W - flag_width) // 2
        start_y = (WIN_H - flag_height) // 2
        
        # Draw green background
        for y in range(flag_height):
            for x in range(flag_width):
                self.screen.set_at((start_x + x, start_y + y), GREEN)
        
        # Draw red circle
        circle_radius = flag_width // 5
        circle_center_x = start_x + (flag_width * 2 // 5)
        circle_center_y = start_y + (flag_height // 2)
        
        for radius in range(circle_radius, -1, -1):
            x, y = 0, radius
            d = 1 - radius
            while x <= y:
                points = [
                    (circle_center_x + x, circle_center_y + y),
                    (circle_center_x - x, circle_center_y + y),
                    (circle_center_x + x, circle_center_y - y),
                    (circle_center_x - x, circle_center_y - y),
                    (circle_center_x + y, circle_center_y + x),
                    (circle_center_x - y, circle_center_y + x),
                    (circle_center_x + y, circle_center_y - x),
                    (circle_center_x - y, circle_center_y - x)
                ]
                for px, py in points:
                    if 0 <= px < WIN_W and 0 <= py < WIN_H:
                        self.screen.set_at((px, py), RED)
                
                if d < 0:
                    d += 2 * x + 3
                else:
                    d += 2 * (x - y) + 5
                    y -= 1
                x += 1
        
        pygame.display.flip()
    
    def run(self, simple=False):
        if simple:
            self.draw_simple_flag()
        else:
            self.draw_flag()
        
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
    print("=" * 50)
    print("Bangladesh Flag Drawing Program")
    print("=" * 50)
    print("\nChoose flag style:")
    print("1. Full flag with information text")
    print("2. Simple flag (no text)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    flag = BangladeshFlag()
    
    if choice == "2":
        flag.run(simple=True)
    else:
        flag.run(simple=False)