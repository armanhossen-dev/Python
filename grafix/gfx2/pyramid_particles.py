import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Constants
NP = 300  # More particles for better effect
WIN_W = 800
WIN_H = 600

class PyramidParticles:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Lab 4: Red Pyramid with Fire Particles")
        
        # Initialize particles
        self.part_x = [0.0] * NP
        self.part_y = [0.0] * NP
        self.part_z = [0.0] * NP
        self.part_vx = [0.0] * NP
        self.part_vy = [0.0] * NP
        self.part_vz = [0.0] * NP
        self.part_life = [0.0] * NP
        self.angle = 0.0
        
        self.init_particles()
        self.setup_lighting()
        
        # Set random seed for consistent results
        random.seed(12345)
        
        # Setup OpenGL
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
    def init_particles(self):
        """Initialize fire particles"""
        for i in range(NP):
            self.part_x[i] = random.uniform(-0.8, 0.8)
            self.part_y[i] = random.uniform(0, 0.5)
            self.part_z[i] = random.uniform(-0.8, 0.8)
            self.part_vx[i] = random.uniform(-0.03, 0.03)
            self.part_vy[i] = random.uniform(0.05, 0.15)
            self.part_vz[i] = random.uniform(-0.03, 0.03)
            self.part_life[i] = random.uniform(0.0, 1.0)
    
    def update_particles(self):
        """Update particle positions and reset if out of bounds"""
        for i in range(NP):
            # Update position
            self.part_x[i] += self.part_vx[i]
            self.part_y[i] += self.part_vy[i]
            self.part_z[i] += self.part_vz[i]
            self.part_life[i] -= 0.01
            
            # Reset particle if dead or out of bounds
            if (self.part_life[i] <= 0 or 
                self.part_y[i] > 2.0 or 
                abs(self.part_x[i]) > 1.5 or 
                abs(self.part_z[i]) > 1.5):
                
                # Reset at pyramid peak
                self.part_x[i] = random.uniform(-0.5, 0.5)
                self.part_y[i] = random.uniform(0.8, 1.0)
                self.part_z[i] = random.uniform(-0.5, 0.5)
                self.part_vx[i] = random.uniform(-0.05, 0.05)
                self.part_vy[i] = random.uniform(0.08, 0.2)
                self.part_vz[i] = random.uniform(-0.05, 0.05)
                self.part_life[i] = 1.0
    
    def draw_particles(self):
        """Draw fire particles"""
        glDisable(GL_LIGHTING)
        
        for i in range(NP):
            # Fire colors: red, orange, yellow based on life
            if self.part_life[i] > 0.7:
                color = (1.0, 0.2, 0.0)  # Bright red
                size = 4.0
            elif self.part_life[i] > 0.4:
                color = (1.0, 0.5, 0.0)  # Orange
                size = 3.0
            else:
                color = (1.0, 0.8, 0.0)  # Yellow
                size = 2.0
            
            glColor3f(*color)
            glPointSize(size)
            glBegin(GL_POINTS)
            glVertex3f(self.part_x[i], self.part_y[i], self.part_z[i])
            glEnd()
        
        glEnable(GL_LIGHTING)
    
    def draw_pyramid(self):
        """Draw a 3D pyramid (triangle-based pyramid)"""
        # Material properties - Red
        ambient = [0.6, 0.1, 0.1, 1.0]
        diffuse = [0.9, 0.2, 0.2, 1.0]
        specular = [1.0, 0.6, 0.6, 1.0]
        shininess = 60.0
        
        glPushMatrix()
        glTranslatef(0.0, -0.5, 0.0)
        glRotatef(self.angle, 0.3, 1.0, 0.2)
        
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
        
        # Draw pyramid (4 triangular faces + square base)
        # Pyramid vertices
        apex = (0.0, 1.0, 0.0)
        base = [
            (-0.8, -0.5, -0.8),  # front-left
            ( 0.8, -0.5, -0.8),  # front-right
            ( 0.8, -0.5,  0.8),  # back-right
            (-0.8, -0.5,  0.8)   # back-left
        ]
        
        # Calculate normals for each face
        # Front face
        self.draw_triangle(apex, base[0], base[1], (0, 0, -1))
        # Right face
        self.draw_triangle(apex, base[1], base[2], (1, 0, 0))
        # Back face
        self.draw_triangle(apex, base[2], base[3], (0, 0, 1))
        # Left face
        self.draw_triangle(apex, base[3], base[0], (-1, 0, 0))
        
        # Draw base (square)
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        for vertex in base:
            glVertex3fv(vertex)
        glEnd()
        
        glPopMatrix()
    
    def draw_triangle(self, v1, v2, v3, normal):
        """Draw a single triangle"""
        glBegin(GL_TRIANGLES)
        glNormal3fv(normal)
        glVertex3fv(v1)
        glVertex3fv(v2)
        glVertex3fv(v3)
        glEnd()
    
    def setup_lighting(self):
        """Setup the light source"""
        # Light position
        light_pos = [2.5, 4.0, 3.0, 1.0]
        
        # Light properties - warm lighting for fire effect
        ambient = [0.2, 0.15, 0.15, 1.0]
        diffuse = [1.0, 0.8, 0.6, 1.0]
        specular = [1.0, 1.0, 1.0, 1.0]
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
        
        # Add a second light from below for dramatic effect
        light_pos2 = [0.0, -1.0, 0.0, 1.0]
        ambient2 = [0.3, 0.1, 0.1, 1.0]
        diffuse2 = [0.8, 0.3, 0.2, 1.0]
        
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_POSITION, light_pos2)
        glLightfv(GL_LIGHT1, GL_AMBIENT, ambient2)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse2)
    
    def display(self):
        """Main display function"""
        glClearColor(0.02, 0.02, 0.05, 1.0)  # Very dark blue-black background
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Setup projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(WIN_W) / float(WIN_H), 0.1, 100.0)
        
        # Setup modelview
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3.5, 1.5, 4.0,   # Eye position
                  0.0, 0.0, 0.0,   # Center position
                  0.0, 1.0, 0.0)   # Up direction
        
        # Draw ground reflection effect
        glDisable(GL_LIGHTING)
        glColor4f(0.1, 0.0, 0.0, 0.3)
        glBegin(GL_QUADS)
        glVertex3f(-2, -0.6, -2)
        glVertex3f(2, -0.6, -2)
        glVertex3f(2, -0.6, 2)
        glVertex3f(-2, -0.6, 2)
        glEnd()
        glEnable(GL_LIGHTING)
        
        # Draw pyramid and particles
        self.draw_pyramid()
        self.draw_particles()
        
        pygame.display.flip()
    
    def run(self):
        """Main loop"""
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        self.init_particles()
                    elif event.key == pygame.K_SPACE:
                        # Toggle rotation
                        pass
            
            # Update animation
            self.angle += 0.35
            if self.angle >= 360.0:
                self.angle -= 360.0
            self.update_particles()
            
            # Render
            self.display()
            
            # Control frame rate
            clock.tick(60)
        
        pygame.quit()

# Version with a star-shaped pyramid
class StarPyramidParticles(PyramidParticles):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Lab 4: Star Pyramid with Magic Particles")
        
    def draw_pyramid(self):
        """Draw a multi-colored pyramid"""
        glPushMatrix()
        glTranslatef(0.0, -0.5, 0.0)
        glRotatef(self.angle, 0.3, 1.0, 0.2)
        
        apex = (0.0, 1.0, 0.0)
        base = [
            (-0.8, -0.5, -0.8),
            (0.8, -0.5, -0.8),
            (0.8, -0.5, 0.8),
            (-0.8, -0.5, 0.8)
        ]
        
        # Different colors for each face
        colors = [
            (1.0, 0.2, 0.2),  # Front - Red
            (1.0, 0.5, 0.2),  # Right - Orange
            (1.0, 0.8, 0.2),  # Back - Gold
            (0.8, 0.3, 0.8)   # Left - Purple
        ]
        
        faces = [
            (apex, base[0], base[1], (0, 0, -1)),  # Front
            (apex, base[1], base[2], (1, 0, 0)),   # Right
            (apex, base[2], base[3], (0, 0, 1)),   # Back
            (apex, base[3], base[0], (-1, 0, 0))   # Left
        ]
        
        for i, (v1, v2, v3, normal) in enumerate(faces):
            glMaterialfv(GL_FRONT, GL_AMBIENT, [colors[i][0]*0.5, colors[i][1]*0.5, colors[i][2]*0.5, 1.0])
            glMaterialfv(GL_FRONT, GL_DIFFUSE, [*colors[i], 1.0])
            glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
            
            glBegin(GL_TRIANGLES)
            glNormal3fv(normal)
            glVertex3fv(v1)
            glVertex3fv(v2)
            glVertex3fv(v3)
            glEnd()
        
        # Base
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        for vertex in base:
            glVertex3fv(vertex)
        glEnd()
        
        glPopMatrix()

# Simple version with basic pyramid
def simple_pyramid():
    """Simpler version with basic pyramid"""
    pygame.init()
    pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Simple 3D Pyramid")
    
    angle = 0.0
    
    # Setup OpenGL
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    
    # Light setup
    light_pos = [2.5, 4.0, 3.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.8, 0.6, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        angle += 0.5
        if angle >= 360.0:
            angle -= 360.0
        
        # Render
        glClearColor(0.02, 0.02, 0.05, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(WIN_W) / float(WIN_H), 0.1, 100.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        
        # Draw pyramid
        glPushMatrix()
        glRotatef(angle, 0, 1, 0)
        
        # Material
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.6, 0.1, 0.1, 1.0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.9, 0.2, 0.2, 1.0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 0.6, 0.6, 1.0])
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50.0)
        
        # Draw pyramid manually
        apex = (0.0, 1.0, 0.0)
        base = [(-0.8, -0.5, -0.8), (0.8, -0.5, -0.8), (0.8, -0.5, 0.8), (-0.8, -0.5, 0.8)]
        
        # 4 triangular faces
        glBegin(GL_TRIANGLES)
        # Front
        glNormal3f(0, 0, -1)
        glVertex3fv(apex)
        glVertex3fv(base[0])
        glVertex3fv(base[1])
        # Right
        glNormal3f(1, 0, 0)
        glVertex3fv(apex)
        glVertex3fv(base[1])
        glVertex3fv(base[2])
        # Back
        glNormal3f(0, 0, 1)
        glVertex3fv(apex)
        glVertex3fv(base[2])
        glVertex3fv(base[3])
        # Left
        glNormal3f(-1, 0, 0)
        glVertex3fv(apex)
        glVertex3fv(base[3])
        glVertex3fv(base[0])
        glEnd()
        
        # Base
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        for vertex in base:
            glVertex3fv(vertex)
        glEnd()
        
        glPopMatrix()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    print("=" * 50)
    print("3D Pyramid with Fire Particles")
    print("=" * 50)
    print("\nChoose version:")
    print("1. Red Pyramid with Fire Particles")
    print("2. Multi-colored Star Pyramid")
    print("3. Simple Pyramid (no particles)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        app = PyramidParticles()
        app.run()
    elif choice == "2":
        app = StarPyramidParticles()
        app.run()
    elif choice == "3":
        simple_pyramid()
    else:
        print("Invalid choice. Running red pyramid with particles...")
        app = PyramidParticles()
        app.run()