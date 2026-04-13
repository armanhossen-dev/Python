from PIL import Image, ImageDraw, ImageFont

def create_pakha():
    # Create a canvas matching your photo background
    width, height = 800, 600
    img = Image.new('RGB', (width, height), '#F1F1F1')
    draw = ImageDraw.Draw(img)

    def draw_single_fan(x_center, handle_on_right=True):
        # Colors from the image
        green, yellow, orange, blue, pink = '#66BB6A', '#FFEB3B', '#EF6C00', '#29B6F6', '#D81B60'
        
        # 1. Handle Position logic
        fan_center_y = 250
        offset = -90 if handle_on_right else 90
        fan_center_x = x_center + offset
        
        # 2. Draw Handle
        draw.rounded_rectangle([x_center-4, 150, x_center+4, 450], radius=5, fill=green)
        
        # 3. Draw Fan Head (Outer Scallop)
        r = 110
        draw.ellipse([fan_center_x-r, fan_center_y-r, fan_center_x+r, fan_center_y+r], fill=orange)
        
        # 4. Yellow Circle
        r = 90
        draw.ellipse([fan_center_x-r, fan_center_y-r, fan_center_x+r, fan_center_y+r], fill=yellow)
        
        # 5. Blue Ring (Outline only)
        r = 70
        draw.ellipse([fan_center_x-r, fan_center_y-r, fan_center_x+r, fan_center_y+r], outline=blue, width=15)
        
        # 6. Pink Center Diamond/Flower
        r = 20
        draw.polygon([(fan_center_x, fan_center_y-r), (fan_center_x+r, fan_center_y), 
                      (fan_center_x, fan_center_y+r), (fan_center_x-r, fan_center_y)], fill=pink)

    # Draw both fans
    draw_single_fan(width//2 - 20, handle_on_right=True)  # Left fan
    draw_single_fan(width//2 + 20, handle_on_right=False) # Right fan

    # Add Text
    try:
        # Try to use a system font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        font = ImageFont.load_default()
        
    draw.text((width//2, 520), "Boishaki Pakha", fill="grey", font=font, anchor="mm")

    img.save("boishaki_pakha_output.png")
    print("Image saved as boishaki_pakha_output.png")

create_pakha()