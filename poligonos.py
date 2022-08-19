import sys, ctypes, math
import sdl2, sdl2.ext
from OpenGL import GL
from random import random
import random as aleatorio

def run():
    if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
        print(sdl2.SDL_GetError())
        return -1

    window = sdl2.SDL_CreateWindow(b"OpenGL Solid",
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED, 800, 600,
                                   sdl2.SDL_WINDOW_OPENGL)
    if not window:
        print(sdl2.SDL_GetError())
        return -1

    context = sdl2.SDL_GL_CreateContext(window)

    GL.glMatrixMode(GL.GL_PROJECTION | GL.GL_MODELVIEW)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glLoadIdentity()
    GL.glOrtho(-400, 400, -300, 300, -300, 300)

    draw(window)

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0

def draw(window):
    mouse_x, mouse_y = ctypes.c_int(0), ctypes.c_int(0)
    
    while handle_events():
        black_background()
        sdl2.mouse.SDL_GetMouseState(ctypes.byref(mouse_x), ctypes.byref(mouse_y))
        mouse_rotation(mouse_x, mouse_y, lambda: draw_revolution_solid(
            100,
            aleatorio.randint(1, 10),
            math.floor(mouse_x.value / 35) + 1
        ))
        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)

def handle_events():
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            return False
    return True

def black_background():
    GL.glClearColor(0, 0, 0, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

def mouse_rotation(mouse_x, mouse_y, draw_function):
        GL.glPushMatrix()
        angle_x =  mouse_y.value / 600 * 360
        angle_y =  mouse_x.value / 600 * 360
        GL.glRotatef(angle_x, 1, 0, 0)
        GL.glRotatef(angle_y, 0, 1, 0)
        draw_function()
        GL.glPopMatrix()


def draw_revolution_solid(radius = 100, base_sides_number = 8, revolution_sides_number = 1):
    base_angle_size = 2*math.pi / base_sides_number
    revolution_angle_size = 2*math.pi / revolution_sides_number

    circle_points = [(radius * math.cos(t * base_angle_size), radius * math.sin(t * base_angle_size)) for t in range(base_sides_number + 1)]

    circles = []
    for circle_index in range(revolution_sides_number + 1):
        points = []
        for point_index in range(base_sides_number + 1):
            points.append((
                circle_points[point_index][0] + radius * math.cos(circle_index * revolution_angle_size),
                circle_points[point_index][1],
                radius * math.sin(circle_index * revolution_angle_size),
            ))
        circles.append(points)
    
    for circle_index in range(revolution_sides_number):
        colorR = random()
        colorG = random()
        colorB = random()

        GL.glBegin(GL.GL_LINES)
        for point_index in range(base_sides_number):
            circle = circles[circle_index]

            GL.glColor3f(colorR, colorG, colorB)
            GL.glVertex3f(*circle[point_index])
            GL.glVertex3f(*circle[point_index + 1])
        GL.glEnd()

if __name__ == "__main__":
    sys.exit(run())