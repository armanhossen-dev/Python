from PIL import Image, ImageDraw, ImageFont
import math


C_RED = '#E14F26'
C_ORANGE = '#F58220'
C_YELLOW = '#FFEB3B'
C_GREEN = '#66BB6A'
C_BLUE = '#29B6F6'
C_MAGENTA = '#D81B60'
C_WHITE = '#FFFFFF'
C_BG = '#F2F2F2'
C_TEXT = '#757575'

def get_star_points(center, r_outer, r_inner, num_points):
    """Calculates points for zig-zag/serrated edges."""
    points = []
    for i in range(num_points * 2):
        angle = math.radians(i * (360 / (num_points * 2)) - 90)
        r = r_outer if i % 2 == 0 else r_inner
        points.append((center[0] + r * math.cos(angle), center[1] + r * math.sin(angle)))
    return points

def draw_pakha(draw, x_center, y_center, handle_on_right=True):
    
    head_x = x_center - 110 if handle_on_right else x_center + 110
    head_center = (head_x, y_center - 50)
  
    
    draw.ellipse([head_center[0]-145, head_center[1]-145, head_center[0]+145, head_center[1]+145], fill=C_WHITE)
    draw.rounded_rectangle([x_center-15, y_center-160, x_center+15, y_center+240], radius=15, fill=C_WHITE)

       
    draw.rectangle([x_center-4, y_center-150, x_center+4, y_center+200], fill=C_GREEN)
    
    draw.rounded_rectangle([x_center-10, y_center+110, x_center+10, y_center+220], radius=8, fill=C_ORANGE)
    
    draw.pieslice([x_center-10, y_center+210, x_center+10, y_center+235], 0, 180, fill=C_GREEN)

        
    scallop_points = get_star_points(head_center, 135, 125, 30)
    draw.polygon(scallop_points, fill=C_RED)
    
    
    inner_scallop = get_star_points(head_center, 128, 120, 30)
    draw.polygon(inner_scallop, fill=C_ORANGE)

    
    yellow_star = get_star_points(head_center, 105, 90, 20)
    draw.polygon(yellow_star, fill=C_YELLOW)

    
    draw.ellipse([head_center[0]-82, head_center[1]-82, head_center[0]+82, head_center[1]+82], fill=C_GREEN)

    
    blue_ring = get_star_points(head_center, 78, 65, 16)
    draw.polygon(blue_ring, fill=C_BLUE)

    
    draw.ellipse([head_center[0]-55, head_center[1]-55, head_center[0]+55, head_center[1]+55], fill=C_YELLOW)

    
    
    for angle in [0, 90, 180, 270]:
        rad = math.radians(angle)
        px = head_center[0] + 25 * math.cos(rad)
        py = head_center[1] + 25 * math.sin(rad)
        draw.ellipse([px-15, py-15, px+15, py+15], fill=C_BLUE)

    
    for angle in [0, 90, 180, 270]:
        rad = math.radians(angle)
        
        p_dist = 20
        px, py = head_center[0] + p_dist * math.cos(rad), head_center[1] + p_dist * math.sin(rad)
        
        draw.ellipse([px-18, py-10, px+18, py+10], fill=C_MAGENTA)
        
        draw.ellipse([px-10, py-18, px+10, py+18], fill=C_MAGENTA)

    
    draw.ellipse([head_center[0]-6, head_center[1]-6, head_center[0]+6, head_center[1]+6], fill=C_GREEN)


def create_final_image():
    
    img = Image.new('RGB', (1200, 1000), C_BG)
    draw = ImageDraw.Draw(img)
  
    
    draw_pakha(draw, 550, 450, handle_on_right=True)
    
    draw_pakha(draw, 650, 450, handle_on_right=False)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    draw.text((600, 900), "Boishaki Pakha", fill=C_TEXT, font=font, anchor="mm")

    img.save("boishaki_pakha_close.png")
    print("Success! Image with reduced gap saved as boishaki_pakha.png")

create_final_image()