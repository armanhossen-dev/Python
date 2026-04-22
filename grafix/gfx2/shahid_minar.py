import pygame
import sys
import math

# Constants
WIN_W = 900
WIN_H = 700
MAX_PTS = 131072

# Colors (RGB)
COLOR_BG = (107, 128, 148)  # 0.42, 0.50, 0.58
COLOR_DARK_GRAY = (71, 71, 77)  # 0.28, 0.28, 0.30
COLOR_DARK_BORDER = (31, 31, 36)  # 0.12, 0.12, 0.14
COLOR_SUN = (242, 13, 20)  # 0.95, 0.05, 0.08
COLOR_WHITE = (255, 255, 255)  # 1.0, 1.0, 1.0
COLOR_LIGHT_GRAY = (191, 191, 199)  # 0.75, 0.75, 0.78
COLOR_BLACK = (5, 5, 5)  # 0.02, 0.02, 0.02
COLOR_TEXT = (230, 230, 230)  # 0.9, 0.9, 0.9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ShahidMinar:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption("Shahid Minar - Bresenham lines, midpoint circle (sun)")
        self.clock = pygame.time.Clock()
        self.points = []
        
    def pt_reset(self):
        self.points = []
    
    def pt_add(self, x, y):
        if len(self.points) < MAX_PTS:
            self.points.append(Point(x, y))
    
    def flush_points(self, color):
        for point in self.points:
            self.screen.set_at((point.x, WIN_H - point.y), color)
    
    def bresenham_line(self, x0, y0, x1, y1):
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
    
    def rect_outline(self, x0, y0, x1, y1):
        self.bresenham_line(x0, y0, x1, y0)
        self.bresenham_line(x1, y0, x1, y1)
        self.bresenham_line(x1, y1, x0, y1)
        self.bresenham_line(x0, y1, x0, y0)
    
    def hline_bresenham(self, x0, x1, y):
        self.bresenham_line(x0, y, x1, y)
    
    def fill_rect_scanlines(self, x0, y0, x1, y1):
        if y0 > y1:
            y0, y1 = y1, y0
        if x0 > x1:
            x0, x1 = x1, x0
        
        for y in range(y0, y1 + 1):
            self.hline_bresenham(x0, x1, y)
    
    def fill_frame_scanlines(self, xl, yb, xr, yt, ix0, iy0, ix1, iy1):
        for y in range(yb, yt + 1):
            if y < iy0 or y > iy1:
                self.hline_bresenham(xl, xr, y)
            else:
                if xl <= ix0 - 1:
                    self.hline_bresenham(xl, ix0 - 1, y)
                if ix1 + 1 <= xr:
                    self.hline_bresenham(ix1 + 1, xr, y)
    
    def midpoint_circle_ring(self, cx, cy, r):
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
    
    def fill_circle_midpoint(self, cx, cy, r):
        self.pt_reset()
        for ri in range(r, -1, -1):
            self.midpoint_circle_ring(cx, cy, ri)
    
    def draw_pillar_frame(self, cx, w, y0, y1, inset, color):
        xl = cx - w // 2
        xr = cx + w // 2
        yb = y0
        yt = y1
        ix0 = xl + inset
        ix1 = xr - inset
        iy0 = yb + inset
        iy1 = yt - inset
        
        # Fill the frame
        self.pt_reset()
        self.fill_frame_scanlines(xl, yb, xr, yt, ix0, iy0, ix1, iy1)
        self.flush_points(color)
        
        # Draw outlines
        self.pt_reset()
        self.rect_outline(xl, yb, xr, yt)
        self.rect_outline(ix0, iy0, ix1, iy1)
        self.flush_points(COLOR_LIGHT_GRAY)
        
        # Draw vertical lines
        self.pt_reset()
        gap = ix1 - ix0
        x1 = ix0 + gap // 4
        x2 = ix0 + gap // 2
        x3 = ix0 + 3 * gap // 4
        self.bresenham_line(x1, iy0 + 6, x1, iy1 - 6)
        self.bresenham_line(x2, iy0 + 6, x2, iy1 - 6)
        self.bresenham_line(x3, iy0 + 6, x3, iy1 - 6)
        self.flush_points(COLOR_BLACK)
    
    def draw_scene(self):
        cx = WIN_W // 2
        base_top = 180
        
        # Define pillars
        pillars = [
            (cx - 260, 52, base_top, 395, 9, COLOR_WHITE),
            (cx + 260, 52, base_top, 395, 9, COLOR_WHITE),
            (cx - 135, 58, base_top, 455, 10, COLOR_WHITE),
            (cx + 135, 58, base_top, 455, 10, COLOR_WHITE),
            (cx, 72, base_top, 535, 11, COLOR_WHITE)
        ]
        
        # Draw base - filled rectangles
        self.pt_reset()
        self.fill_rect_scanlines(cx - 340, 40, cx + 340, 85)
        self.fill_rect_scanlines(cx - 300, 85, cx + 300, 120)
        self.fill_rect_scanlines(cx - 260, 120, cx + 260, base_top)
        self.flush_points(COLOR_DARK_GRAY)
        
        # Draw base outlines
        self.pt_reset()
        self.rect_outline(cx - 340, 40, cx + 340, 85)
        self.rect_outline(cx - 300, 85, cx + 300, 120)
        self.rect_outline(cx - 260, 120, cx + 260, base_top)
        self.flush_points(COLOR_DARK_BORDER)
        
        # Draw sun
        sun_cy = (pillars[4][2] + pillars[4][3]) // 2 + 8
        sun_r = (pillars[4][3] - pillars[4][2]) // 4
        self.pt_reset()
        self.fill_circle_midpoint(cx, sun_cy, sun_r)
        self.flush_points(COLOR_SUN)
        
        # Draw all pillars
        for cx, w, y0, y1, inset, color in pillars:
            self.draw_pillar_frame(cx, w, y0, y1, inset, color)
    
    def draw_text(self):
        font = pygame.font.Font(None, 18)
        text = "Shahid Minar — Bresenham lines, midpoint circle (sun)"
        text_surface = font.render(text, True, COLOR_TEXT)
        self.screen.blit(text_surface, (18, WIN_H - 22))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            self.screen.fill(COLOR_BG)
            self.draw_scene()
            self.draw_text()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = ShahidMinar()
    app.run()