from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

# Precise colors from image_4.png
P_RED = '#DC4D26'
P_ORANGE = '#EF6C00'
P_YELLOW = '#FFEB3B'
P_BLUE = '#29B6F6'
P_GREEN = '#66BB6A'
P_MAGENTA = '#D81B60'
P_BACK = '#F1F1F1'
P_GREY = '#757575'

def create_scalloped_circle(draw, center, radius, num_scallops, amplitude, color):
    """Calculates points for a scalloped circle (the red/orange edge)"""
    points = []
    # 360 points to make a smooth curve
    for i in range(361):
        angle = np.radians(i)
        # Create a wave on top of the radius
        scallop_offset = amplitude * np.sin(np.radians(i * num_scallops))
        r = radius + scallop_offset
        x = center[0] + r * np.cos(angle)
        y = center[1] + r * np.sin(angle)
        points.append((x, y))
    draw.polygon(points, fill=color)

def create_star_polygon(draw, center, inner_radius, outer_radius, num_points, color):
    """Calculates points for a star polygon (the central yellow star)"""
    points = []
    # Half the number of points for internal vs external vertices
    for i in range(num_points * 2):
        angle = np.radians(i * (180 / num_points) - 90) # -90 to start at the top
        r = outer_radius if i % 2 == 0 else inner_radius
        x = center[0] + r * np.cos(angle)
        y = center[1] + r * np.sin(angle)
        points.append((x, y))
    draw.polygon(points, fill=color)

def create_precise_handfan():
    W, H = 1000, 800
    img = Image.new('RGB', (W, H), P_BACK)
    draw = ImageDraw.Draw(img)

    def draw_full_fan(x_center, handle_on_right=True):
        f_center_y = 350
        offset = -120 if handle_on_right else 120
        f_center_x = x_center + offset
        
        # 1. Complex Handle drawing
        h_x = x_center
        # Green central stick
        draw.line([(h_x, 200), (h_x, 600)], fill=P_GREEN, width=10)
        # Textured Orange grip
        draw.rounded_rectangle([h_x-10, 500, h_x+10, 580], radius=10, fill=P_ORANGE)
        # Curved green end cap (arc)
        draw.arc([h_x-10, 560, h_x+10, 600], start=0, end=180, fill=P_GREEN, width=10)

        # Create a layer with just the fan head for layering effect
        fan_head = Image.new('RGBA', (W, H), (0,0,0,0))
        d_fan = ImageDraw.Draw(fan_head)
        f_center = (f_center_x, f_center_y)

        # 2. Outer Scalloped Border (Red and Orange layers)
        create_scalloped_circle(d_fan, f_center, 135, 24, 8, P_RED) # Outer Red
        create_scalloped_circle(d_fan, f_center, 132, 24, 7, P_ORANGE) # Inner Orange

        # 3. Yellow and Blue Ring complex geometry
        # Yellow 'sun' base
        create_star_polygon(d_fan, f_center, 105, 115, 24, P_YELLOW)
        # Blue/Green pointed ring
        create_star_polygon(d_fan, f_center, 80, 95, 12, P_BLUE)
        
        # 4. Central Mandala Pattern
        # Central Magenta flower (using complex shapes rather than simple ellipses)
        for i in range(4):
            angle = i * 90
            d_fan.pieslice([f_center_x-25, f_center_y-25, f_center_x+25, f_center_y+25], 
                           start=angle+5, end=angle+85, fill=P_MAGENTA)

        # Little green and blue center dots
        d_fan.ellipse([f_center_x-5, f_center_y-5, f_center_x+5, f_center_y+5], fill=P_GREEN)

        # Paste the fan head onto the main canvas
        img.paste(fan_head, (0, 0), fan_head)

    # Draw both precise fans
    draw_full_fan(W//2 - 25, handle_on_right=True)  # Left precise fan
    draw_full_fan(W//2 + 25, handle_on_right=False) # Right precise fan (mirror handle logic)

    # Precise Writing using Helvetica (a common system serif font)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 50)
    except:
        font = ImageFont.load_default()
    
    draw.text((W//2, 700), "Boishaki Pakha", fill=P_GREY, font=font, anchor="mm")

    final_img = img.save("precise_boishaki_pakha.png")
    print("Detailed image saved as precise_boishaki_pakha.png")

create_precise_handfan()