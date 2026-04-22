import pygame
import sys

# Constants
W = 800
H = 600
MAX_PIX = 50000

# Colors
BG_COLOR = (26, 26, 31)        # 0.1, 0.1, 0.12
LINE_COLOR = (51, 229, 255)    # 0.2, 0.9, 1.0
TEXT_COLOR = (217, 217, 217)   # 0.85, 0.85, 0.85

class DDAAlgorithm:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Lab 2a: DDA Line Drawing")
        self.clock = pygame.time.Clock()
        self.px_buf = []
        self.max_pix = MAX_PIX
        
    def add_point(self, x, y):
        """Add a point to the buffer"""
        if len(self.px_buf) < self.max_pix:
            self.px_buf.append((x, y))
    
    def line_dda(self, x0, y0, x1, y1):
        """
        DDA (Digital Differential Analyzer) Line Algorithm
        Uses floating-point arithmetic
        """
        dx = x1 - x0
        dy = y1 - y0
        
        # Calculate number of steps
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        # Handle zero-length line
        if steps == 0:
            self.add_point(x0, y0)
            return
        
        # Calculate increments
        xinc = dx / steps
        yinc = dy / steps
        
        # Initialize starting point
        x = float(x0)
        y = float(y0)
        
        # Draw the line
        for k in range(steps + 1):
            # Add point with rounding (add 0.5 and cast to int)
            self.add_point(int(x + 0.5), int(y + 0.5))
            x += xinc
            y += yinc
    
    def draw_pixels(self, color):
        """Draw all points in the buffer"""
        for point in self.px_buf:
            if 0 <= point[0] < W and 0 <= point[1] < H:
                self.screen.set_at((point[0], point[1]), color)
    
    def draw_text(self, text, x, y, size=15):
        """Draw text on screen"""
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (x, y))
    
    def display(self):
        """Main display function - matches C code structure"""
        # Clear screen
        self.screen.fill(BG_COLOR)
        
        # Define lines (same as C code)
        lines = [
            (50, 80, W - 50, H - 80),      # Diagonal line
            (80, H - 100, W - 80, 120),    # Cross diagonal
            (W // 2, 50, W // 2, H - 50),  # Vertical line
            (100, 300, W - 100, 310)       # Almost horizontal line
        ]
        
        # Reset point buffer
        self.px_buf = []
        
        # Draw all lines using DDA algorithm
        for x0, y0, x1, y1 in lines:
            self.line_dda(x0, y0, x1, y1)
        
        # Draw all pixels
        self.draw_pixels(LINE_COLOR)
        
        # Draw text (same as C code)
        self.draw_text("Lab 2a: DDA line algorithm (floating-point steps)", 20, H - 28)
        
        # Additional information
        self.draw_text("Lines drawn:", 20, 20, 12)
        self.draw_text("1. Main diagonal (50,80) to (750,520)", 20, 35, 12)
        self.draw_text("2. Cross diagonal (80,500) to (720,120)", 20, 50, 12)
        self.draw_text("3. Vertical line (400,50) to (400,550)", 20, 65, 12)
        self.draw_text("4. Horizontal-ish line (100,300) to (700,310)", 20, 80, 12)
        
        # Display statistics
        self.draw_text(f"Total pixels drawn: {len(self.px_buf)}", 20, H - 50, 12)
        
        # Algorithm information
        self.draw_text("DDA Algorithm: Uses floating-point arithmetic", W - 200, H - 28, 10)
        
        pygame.display.flip()
    
    def run(self):
        """Main loop"""
        self.display()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        # Redraw on 'R' key
                        self.display()
            
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Extended demo with more features
class DDADemo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("DDA Algorithm - Complete Demo")
        self.clock = pygame.time.Clock()
        self.px_buf = []
        
    def add_point(self, x, y):
        self.px_buf.append((x, y))
    
    def line_dda(self, x0, y0, x1, y1):
        """DDA Line Algorithm"""
        dx = x1 - x0
        dy = y1 - y0
        
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        if steps == 0:
            self.add_point(x0, y0)
            return
        
        xinc = dx / steps
        yinc = dy / steps
        
        x = float(x0)
        y = float(y0)
        
        for k in range(steps + 1):
            self.add_point(int(x + 0.5), int(y + 0.5))
            x += xinc
            y += yinc
    
    def draw_pixels(self, color):
        for point in self.px_buf:
            if 0 <= point[0] < W and 0 <= point[1] < H:
                self.screen.set_at((point[0], point[1]), color)
    
    def draw_grid(self):
        """Draw a reference grid"""
        grid_color = (40, 40, 45)
        # Vertical lines
        for x in range(0, W, 50):
            self.px_buf = []
            self.line_dda(x, 0, x, H)
            self.draw_pixels(grid_color)
        # Horizontal lines
        for y in range(0, H, 50):
            self.px_buf = []
            self.line_dda(0, y, W, y)
            self.draw_pixels(grid_color)
    
    def draw_all_slopes(self):
        """Draw lines with different slopes"""
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        
        # Different line types
        lines = [
            # (x1, y1, x2, y2, color, description)
            (50, 50, 350, 50, (255, 0, 0), "Horizontal (0°)"),
            (50, 100, 350, 180, (0, 255, 0), "Gentle slope (~22°)"),
            (50, 150, 350, 300, (0, 0, 255), "45° diagonal"),
            (50, 200, 350, 450, (255, 255, 0), "Steep slope (~63°)"),
            (50, 250, 350, 550, (255, 0, 255), "Very steep (~68°)"),
            (450, 50, 450, 300, (0, 255, 255), "Vertical (90°)"),
            (500, 100, 750, 100, (255, 165, 0), "Horizontal (right)"),
            (500, 200, 750, 350, (128, 0, 128), "Positive slope"),
            (500, 300, 750, 200, (255, 192, 203), "Negative slope"),
            (500, 400, 750, 550, (165, 42, 42), "Long diagonal"),
        ]
        
        # Draw all lines
        for x1, y1, x2, y2, color, desc in lines:
            self.px_buf = []
            self.line_dda(x1, y1, x2, y2)
            self.draw_pixels(color)
        
        # Add descriptions
        font = pygame.font.Font(None, 14)
        for x1, y1, x2, y2, color, desc in lines:
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            text = font.render(desc, True, (200, 200, 200))
            text_rect = text.get_rect(center=(mid_x, mid_y - 10))
            pygame.draw.rect(self.screen, BG_COLOR, text_rect.inflate(4, 2))
            self.screen.blit(text, text_rect)
        
        # Title
        title_font = pygame.font.Font(None, 24)
        title = "DDA (Digital Differential Analyzer) Line Algorithm"
        title_surface = title_font.render(title, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(W // 2, 20))
        self.screen.blit(title_surface, title_rect)
        
        # Instructions
        inst_font = pygame.font.Font(None, 16)
        inst = "Press ESC to exit | R to redraw | C for comparison"
        inst_surface = inst_font.render(inst, True, (200, 200, 200))
        inst_rect = inst_surface.get_rect(center=(W // 2, H - 20))
        self.screen.blit(inst_surface, inst_rect)
        
        pygame.display.flip()
    
    def compare_dda_bresenham(self):
        """Compare DDA with Bresenham algorithm"""
        self.screen.fill(BG_COLOR)
        
        # Test lines for comparison
        test_lines = [
            (100, 100, 700, 100, "Horizontal"),
            (100, 150, 700, 250, "Gentle Slope"),
            (100, 300, 700, 500, "Steep Slope"),
            (100, 400, 700, 550, "Very Steep"),
            (100, 500, 700, 580, "Extreme Slope"),
        ]
        
        y_offset = 80
        title_font = pygame.font.Font(None, 20)
        label_font = pygame.font.Font(None, 14)
        
        title = "DDA vs Bresenham Line Algorithm Comparison"
        title_surface = title_font.render(title, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(W // 2, 20))
        self.screen.blit(title_surface, title_rect)
        
        for i, (x1, y1, x2, y2, label) in enumerate(test_lines):
            y_pos = y_offset + i * 90
            
            # Draw using DDA (left side)
            self.px_buf = []
            self.line_dda(x1, y_pos, x2, y_pos + (y2 - y1))
            self.draw_pixels((51, 229, 255))  # Cyan
            
            # Draw using Bresenham (right side, offset)
            self.px_buf = []
            self.bresenham_line(x1 + 400, y_pos, x2 + 400, y_pos + (y2 - y1))
            self.draw_pixels((255, 77, 217))  # Pink
            
            # Labels
            dda_label = label_font.render(f"DDA: {label}", True, (51, 229, 255))
            bres_label = label_font.render(f"Bresenham: {label}", True, (255, 77, 217))
            
            self.screen.blit(dda_label, (x1, y_pos - 20))
            self.screen.blit(bres_label, (x1 + 400, y_pos - 20))
        
        # Legend
        legend_font = pygame.font.Font(None, 16)
        legend1 = legend_font.render("Cyan: DDA Algorithm (floating-point)", True, (51, 229, 255))
        legend2 = legend_font.render("Pink: Bresenham Algorithm (integer-only)", True, (255, 77, 217))
        self.screen.blit(legend1, (50, H - 50))
        self.screen.blit(legend2, (50, H - 30))
        
        # Notes
        note_font = pygame.font.Font(None, 12)
        note1 = "Note: DDA uses floating-point arithmetic, Bresenham uses integer arithmetic"
        note2 = "DDA is simpler but slower, Bresenham is faster but more complex"
        self.screen.blit(note_font.render(note1, True, (150, 150, 150)), (50, H - 70))
        self.screen.blit(note_font.render(note2, True, (150, 150, 150)), (50, H - 60))
        
        pygame.display.flip()
    
    def bresenham_line(self, x0, y0, x1, y1):
        """Bresenham algorithm for comparison"""
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        
        while True:
            self.add_point(x0, y0)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy
    
    def interactive_demo(self):
        """Interactive demo - click and drag to draw lines"""
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        
        start_point = None
        lines_drawn = []
        colors = [
            (51, 229, 255),   # Cyan
            (255, 77, 217),   # Pink
            (0, 255, 0),      # Green
            (255, 255, 0),    # Yellow
            (255, 0, 0),      # Red
            (0, 255, 255),    # Cyan
        ]
        color_index = 0
        
        title_font = pygame.font.Font(None, 24)
        inst_font = pygame.font.Font(None, 16)
        
        running = True
        while running:
            # Draw instructions
            title = "DDA Algorithm - Click and Drag to Draw Lines"
            title_surface = title_font.render(title, True, (255, 255, 255))
            title_rect = title_surface.get_rect(center=(W // 2, 20))
            self.screen.blit(title_surface, title_rect)
            
            inst = "Click and drag to draw lines | ESC to exit | C to clear | S to show stats"
            inst_surface = inst_font.render(inst, True, (200, 200, 200))
            inst_rect = inst_surface.get_rect(center=(W // 2, H - 20))
            self.screen.blit(inst_surface, inst_rect)
            
            # Show stats
            stats = f"Lines drawn: {len(lines_drawn)}"
            stats_surface = inst_font.render(stats, True, (200, 200, 200))
            self.screen.blit(stats_surface, (W - 150, 40))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_c:
                        # Clear screen
                        self.screen.fill(BG_COLOR)
                        self.draw_grid()
                        lines_drawn = []
                        color_index = 0
                        pygame.display.flip()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        start_point = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and start_point:
                        end_point = event.pos
                        color = colors[color_index % len(colors)]
                        
                        # Draw the line
                        self.px_buf = []
                        self.line_dda(start_point[0], start_point[1], 
                                    end_point[0], end_point[1])
                        self.draw_pixels(color)
                        
                        lines_drawn.append((start_point, end_point, color))
                        color_index += 1
                        pygame.display.flip()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def run(self):
        """Main menu"""
        print("=" * 60)
        print("DDA (Digital Differential Analyzer) Line Algorithm")
        print("=" * 60)
        print("\nChoose a demonstration:")
        print("1. Original C code conversion (4 lines)")
        print("2. All line types demo (various slopes)")
        print("3. DDA vs Bresenham comparison")
        print("4. Interactive demo (click and draw)")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            dda = DDAAlgorithm()
            dda.run()
        elif choice == "2":
            self.draw_all_slopes()
            self.wait_for_exit()
        elif choice == "3":
            self.compare_dda_bresenham()
            self.wait_for_exit()
        elif choice == "4":
            self.interactive_demo()
        else:
            print("Invalid choice. Running original demo...")
            dda = DDAAlgorithm()
            dda.run()
    
    def wait_for_exit(self):
        """Wait for ESC key"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        self.draw_all_slopes()
                    elif event.key == pygame.K_c:
                        self.compare_dda_bresenham()
            
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Simple standalone version (exact match to C code)
def dda_simple():
    """Exact Python version of the C code"""
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Lab 2a: DDA Line Drawing")
    clock = pygame.time.Clock()
    
    px_buf = []
    
    def add_point(x, y):
        if len(px_buf) < MAX_PIX:
            px_buf.append((x, y))
    
    def line_dda(x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        if steps == 0:
            add_point(x0, y0)
            return
        
        xinc = dx / steps
        yinc = dy / steps
        
        x = float(x0)
        y = float(y0)
        
        for k in range(steps + 1):
            add_point(int(x + 0.5), int(y + 0.5))
            x += xinc
            y += yinc
    
    def draw_pixels():
        for point in px_buf:
            screen.set_at(point, LINE_COLOR)
    
    def display():
        nonlocal px_buf
        screen.fill(BG_COLOR)
        
        lines = [
            (50, 80, W - 50, H - 80),
            (80, H - 100, W - 80, 120),
            (W // 2, 50, W // 2, H - 50),
            (100, 300, W - 100, 310)
        ]
        
        px_buf = []
        for x0, y0, x1, y1 in lines:
            line_dda(x0, y0, x1, y1)
        
        draw_pixels()
        
        # Draw text
        font = pygame.font.Font(None, 15)
        text = "Lab 2a: DDA line algorithm (floating-point steps)"
        text_surface = font.render(text, True, TEXT_COLOR)
        screen.blit(text_surface, (20, H - 28))
        
        pygame.display.flip()
    
    display()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("DDA Line Algorithm Implementation")
    print("-" * 40)
    print("Choose version:")
    print("1. Simple version (exact C code match)")
    print("2. Full demo with menu")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        dda_simple()
    else:
        demo = DDADemo()
        demo.run()