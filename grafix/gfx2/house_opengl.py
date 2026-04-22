import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Constants
W = 700
H = 600

def draw_house():
    """Exact match to the C code house drawing"""
    
    # Ground (green grass)
    glColor3f(0.2, 0.55, 0.25)
    glBegin(GL_QUADS)
    glVertex2i(0, 0)
    glVertex2i(W, 0)
    glVertex2i(W, 120)
    glVertex2i(0, 120)
    glEnd()
    
    # House body (wood color)
    glColor3f(0.72, 0.58, 0.42)
    glBegin(GL_QUADS)
    glVertex2i(180, 120)
    glVertex2i(520, 120)
    glVertex2i(520, 320)
    glVertex2i(180, 320)
    glEnd()
    
    # Roof (red)
    glColor3f(0.75, 0.2, 0.15)
    glBegin(GL_TRIANGLES)
    glVertex2i(150, 320)
    glVertex2i(350, 430)
    glVertex2i(550, 320)
    glEnd()
    
    # Chimney (gray)
    glColor3f(0.45, 0.45, 0.48)
    glBegin(GL_QUADS)
    glVertex2i(430, 340)
    glVertex2i(470, 340)
    glVertex2i(470, 420)
    glVertex2i(430, 420)
    glEnd()
    
    # Door (dark brown)
    glColor3f(0.35, 0.22, 0.12)
    glBegin(GL_QUADS)
    glVertex2i(310, 120)
    glVertex2i(380, 120)
    glVertex2i(380, 260)
    glVertex2i(310, 260)
    glEnd()
    
    # Door knob (yellow/gold)
    glColor3f(0.9, 0.85, 0.5)
    glPointSize(6.0)
    glBegin(GL_POINTS)
    glVertex2i(365, 195)
    glEnd()
    
    # Left window (blue)
    glColor3f(0.45, 0.65, 0.85)
    glBegin(GL_QUADS)
    glVertex2i(210, 200)
    glVertex2i(280, 200)
    glVertex2i(280, 270)
    glVertex2i(210, 270)
    glEnd()
    
    # Right window (blue)
    glBegin(GL_QUADS)
    glVertex2i(410, 200)
    glVertex2i(480, 200)
    glVertex2i(480, 270)
    glVertex2i(410, 270)
    glEnd()
    
    # Window panes (dark gray lines)
    glColor3f(0.25, 0.25, 0.28)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    # Left window panes
    glVertex2i(245, 200)
    glVertex2i(245, 270)
    glVertex2i(210, 235)
    glVertex2i(280, 235)
    # Right window panes
    glVertex2i(445, 200)
    glVertex2i(445, 270)
    glVertex2i(410, 235)
    glVertex2i(480, 235)
    glEnd()

def display():
    glClearColor(0.55, 0.75, 0.95, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, W, 0, H)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_house()
    pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_mode((W, H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Lab 3: House (OpenGL)")
    
    display()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.time.wait(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
#     # Install required packages
# pip install pygame PyOpenGL PyOpenGL_accelerate

# # Run the full version with menu
# python house_opengl.py

# # Or run the minimal version (exact match)
# python house_minimal.py