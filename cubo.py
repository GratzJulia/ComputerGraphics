import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *
import math

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ((1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5))

def Cubo():
    # glBegin(GL_QUADS)
    # i = 0
    # for face in faces:
    #     # glColor3fv(cores[i])
    #     for vertex in face:
    #        glColor3fv(cores[vertex])
    #        glVertex3fv(vertices[vertex])
    #     i = i+1
    # glEnd()

    # glColor3f(0,0.5,0)
    # glBegin(GL_LINES)
    # for linha in linhas:
    #     for vertice in linha:
    #         glVertex3fv(vertices[vertice])
    # glEnd()
    return

def desenhaDoisCubos():
    # Cubo da Esquerda
    # glPushMatrix()
    # glTranslatef(-2,0,0)
    # glRotatef(-a,0,0,1)
    # Cubo()
    # glPopMatrix()
    # Cubo da Direita
    # glPushMatrix()
    # glTranslatef(2,0,0)
    # glRotatef(a,1,0,0)
    # Cubo()
    # glPopMatrix()
    return

def desenhaHexagono():
    glBegin(GL_POLYGON)
    a = math.pi/3
    pts = []
    for lado in range(0,6):
        x = math.cos(a * lado)
        y = math.sin(a * lado)
        glVertex3f(x, y, 0)
        pts.append((x, y))
    glEnd()
    return pts

def desenhaPiramide():
    pts = desenhaHexagono()

    glBegin(GL_TRIANGLES)
    a = math.pi/3

    for index in range(0,len(pts)):
        p = pts[index]
        if index == 6-1:
            p2 = pts[0]
        else:
            p2 = pts[index+1]
        
        glColor3fv(cores[index])
        glVertex3f(p[0], p[1], 0)
        glVertex3f(p2[0], p2[1], 0)
        glVertex3f(0, 0, 5)
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    desenhaPiramide()
    glRotatef(math.pi/20, 2, 0, 0)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Cubo", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)