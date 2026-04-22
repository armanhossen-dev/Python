import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Constants
NP = 200
WIN_W = 800
WIN_H = 600

class Particles3D:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Lab 4: Particles + 3D Lit Cube")
        
        # Initialize particles
        self.part_x = [0.0] * NP
        self.part_y = [0.0] * NP
        self.part_z = [0.0] * NP
        self.part_vy = [0.0] * NP
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
        
    def init_particles(self):
        """Initialize particle positions and velocities"""
        for i in range(NP):
            self.part_x[i] = (random.randint(0, 200) - 100) / 25.0
            self.part_y[i] = (random.randint(0, 200) / 40.0) - 2.0
            self.part_z[i] = (random.randint(0, 200) - 100) / 30.0
            self.part_vy[i] = 0.02 + (random.randint(0, 100) / 5000.0)
    
    def update_particles(self):
        """Update particle positions and reset if out of bounds"""
        for i in range(NP):
            self.part_y[i] += self.part_vy[i]
            if self.part_y[i] > 3.0:
                self.part_y[i] = -2.5
                self.part_x[i] = (random.randint(0, 200) - 100) / 25.0
                self.part_z[i] = (random.randint(0, 200) - 100) / 30.0
    
    def draw_particles(self):
        """Draw all particles as points"""
        glDisable(GL_LIGHTING)
        glColor3f(0.4, 0.85, 1.0)  # Light blue
        glPointSize(3.0)
        glBegin(GL_POINTS)
        for i in range(NP):
            glVertex3f(self.part_x[i], self.part_y[i], self.part_z[i])
        glEnd()
        glEnable(GL_LIGHTING)
    
    def draw_lit_cube(self):
        """Draw a rotating cube with material properties"""
        # Material properties
        ambient = [0.2, 0.15, 0.1, 1.0]
        diffuse = [0.9, 0.5, 0.2, 1.0]
        specular = [1.0, 1.0, 0.9, 1.0]
        shininess = 40.0
        
        glPushMatrix()
        glTranslatef(0.0, 0.2, 0.0)
        glRotatef(self.angle, 0.3, 1.0, 0.2)
        
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
        
        self.draw_cube(1.4)
        glPopMatrix()
    
    def draw_cube(self, size):
        """Draw a cube manually (since glutSolidCube might not be available)"""
        s = size / 2.0
        
        # Define vertices for the cube
        vertices = [
            (-s, -s, -s), ( s, -s, -s), ( s, -s,  s), (-s, -s,  s),  # Bottom face
            (-s,  s, -s), ( s,  s, -s), ( s,  s,  s), (-s,  s,  s)   # Top face
        ]
        
        # Define faces (4 vertices per face)
        faces = [
            (0, 1, 2, 3),  # Bottom
            (4, 5, 6, 7),  # Top
            (0, 1, 5, 4),  # Front
            (2, 3, 7, 6),  # Back
            (0, 3, 7, 4),  # Left
            (1, 2, 6, 5)   # Right
        ]
        
        # Define normals for each face (for lighting)
        normals = [
            (0, -1, 0),  # Bottom
            (0, 1, 0),   # Top
            (0, 0, -1),  # Front
            (0, 0, 1),   # Back
            (-1, 0, 0),  # Left
            (1, 0, 0)    # Right
        ]
        
        glBegin(GL_QUADS)
        for i, face in enumerate(faces):
            glNormal3fv(normals[i])
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()
    
    def setup_lighting(self):
        """Setup the light source"""
        # Light position
        light_pos = [2.5, 4.0, 3.0, 1.0]
        
        # Light properties
        ambient = [0.15, 0.15, 0.18, 1.0]
        diffuse = [0.9, 0.85, 0.75, 1.0]
        specular = [1.0, 1.0, 1.0, 1.0]
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    
    def display(self):
        """Main display function"""
        glClearColor(0.05, 0.06, 0.1, 1.0)  # Dark blue-black background
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Setup projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(WIN_W) / float(WIN_H), 0.1, 100.0)
        
        # Setup modelview
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3.5, 2.2, 4.0,   # Eye position
                  0.0, 0.0, 0.0,   # Center position
                  0.0, 1.0, 0.0)   # Up direction
        
        # Draw cube and particles
        self.draw_lit_cube()
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
                        # Reset particles on 'R' key
                        self.init_particles()
            
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

# Enhanced version with more features
class EnhancedParticles3D(Particles3D):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Lab 4: Enhanced Particles + 3D Lit Cube")
        
        # Additional particle properties for enhanced effect
        self.part_color = [(0.0, 0.0, 0.0)] * NP
        self.part_size = [3.0] * NP
        self.init_enhanced_particles()
        
    def init_enhanced_particles(self):
        """Initialize particles with colors and sizes"""
        for i in range(NP):
            # Random color for each particle
            self.part_color[i] = (
                random.uniform(0.3, 0.8),
                random.uniform(0.5, 1.0),
                random.uniform(0.7, 1.0)
            )
            # Random size
            self.part_size[i] = random.uniform(2.0, 5.0)
    
    def draw_particles(self):
        """Draw particles with individual colors and sizes"""
        glDisable(GL_LIGHTING)
        
        for i in range(NP):
            glColor3f(*self.part_color[i])
            glPointSize(self.part_size[i])
            glBegin(GL_POINTS)
            glVertex3f(self.part_x[i], self.part_y[i], self.part_z[i])
            glEnd()
        
        glEnable(GL_LIGHTING)
    
    def draw_particles_as_spheres(self):
        """Alternative: Draw particles as small spheres (more 3D effect)"""
        glDisable(GL_LIGHTING)
        
        for i in range(NP):
            glPushMatrix()
            glTranslatef(self.part_x[i], self.part_y[i], self.part_z[i])
            glColor3f(*self.part_color[i])
            
            # Draw a small sphere for each particle
            quad = gluNewQuadric()
            gluSphere(quad, 0.05, 4, 4)
            gluDeleteQuadric(quad)
            
            glPopMatrix()
        
        glEnable(GL_LIGHTING)
    
    def draw_cube_wireframe(self):
        """Draw wireframe cube for debugging"""
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 1.0, 1.0)
        glLineWidth(1.0)
        
        s = 0.7  # Half size for wireframe
        vertices = [
            (-s, -s, -s), ( s, -s, -s), ( s, -s,  s), (-s, -s,  s),
            (-s,  s, -s), ( s,  s, -s), ( s,  s,  s), (-s,  s,  s)
        ]
        
        edges = [
            (0,1), (1,2), (2,3), (3,0),  # Bottom
            (4,5), (5,6), (6,7), (7,4),  # Top
            (0,4), (1,5), (2,6), (3,7)   # Vertical
        ]
        
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        
        glEnable(GL_LIGHTING)

# Simple version with just the core functionality
def simple_particles_3d():
    """Simpler version without classes"""
    pygame.init()
    pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Lab 4: 3D Particles")
    
    # Initialize particles
    NP = 200
    part_x = [0.0] * NP
    part_y = [0.0] * NP
    part_z = [0.0] * NP
    part_vy = [0.0] * NP
    angle = 0.0
    
    random.seed(12345)
    
    # Initialize particles
    for i in range(NP):
        part_x[i] = (random.randint(0, 200) - 100) / 25.0
        part_y[i] = (random.randint(0, 200) / 40.0) - 2.0
        part_z[i] = (random.randint(0, 200) - 100) / 30.0
        part_vy[i] = 0.02 + (random.randint(0, 100) / 5000.0)
    
    # Setup OpenGL
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    
    # Light setup
    light_pos = [2.5, 4.0, 3.0, 1.0]
    ambient = [0.15, 0.15, 0.18, 1.0]
    diffuse = [0.9, 0.85, 0.75, 1.0]
    specular = [1.0, 1.0, 1.0, 1.0]
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update particles
        for i in range(NP):
            part_y[i] += part_vy[i]
            if part_y[i] > 3.0:
                part_y[i] = -2.5
                part_x[i] = (random.randint(0, 200) - 100) / 25.0
                part_z[i] = (random.randint(0, 200) - 100) / 30.0
        
        angle += 0.35
        if angle >= 360.0:
            angle -= 360.0
        
        # Render
        glClearColor(0.05, 0.06, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(WIN_W) / float(WIN_H), 0.1, 100.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3.5, 2.2, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        
        # Draw cube
        glPushMatrix()
        glTranslatef(0.0, 0.2, 0.0)
        glRotatef(angle, 0.3, 1.0, 0.2)
        
        ambient_mat = [0.2, 0.15, 0.1, 1.0]
        diffuse_mat = [0.9, 0.5, 0.2, 1.0]
        specular_mat = [1.0, 1.0, 0.9, 1.0]
        
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient_mat)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse_mat)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular_mat)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 40.0)
        
        # Draw cube as wireframe (simpler)
        glut = None
        try:
            from OpenGL.GLUT import glutSolidCube
            glutSolidCube(1.4)
        except:
            # Manual cube drawing if GLUT not available
            s = 0.7
            vertices = [
                (-s, -s, -s), ( s, -s, -s), ( s, -s,  s), (-s, -s,  s),
                (-s,  s, -s), ( s,  s, -s), ( s,  s,  s), (-s,  s,  s)
            ]
            faces = [(0,1,2,3), (4,5,6,7), (0,1,5,4), (2,3,7,6), (0,3,7,4), (1,2,6,5)]
            normals = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (-1,0,0), (1,0,0)]
            
            glBegin(GL_QUADS)
            for i, face in enumerate(faces):
                glNormal3fv(normals[i])
                for vertex in face:
                    glVertex3fv(vertices[vertex])
            glEnd()
        
        glPopMatrix()
        
        # Draw particles
        glDisable(GL_LIGHTING)
        glColor3f(0.4, 0.85, 1.0)
        glPointSize(3.0)
        glBegin(GL_POINTS)
        for i in range(NP):
            glVertex3f(part_x[i], part_y[i], part_z[i])
        glEnd()
        glEnable(GL_LIGHTING)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    print("=" * 50)
    print("3D Particles + Lit Cube")
    print("=" * 50)
    print("\nChoose version:")
    print("1. Standard version (exact C code match)")
    print("2. Enhanced version (colored particles)")
    print("3. Simple version (no classes)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        app = Particles3D()
        app.run()
    elif choice == "2":
        app = EnhancedParticles3D()
        app.run()
    elif choice == "3":
        simple_particles_3d()
    else:
        print("Invalid choice. Running standard version...")
        app = Particles3D()
        app.run()
        
        
#         # Install required packages
# pip install pygame PyOpenGL PyOpenGL_accelerate

# # Run the full version
# python particles_3d.py

# # Or run the minimal version
# python particles_simple.py