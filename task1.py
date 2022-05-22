from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
import math

r = 250

def Mid_Point_Circle_Algo(r,x=0,y=0):
    i = x
    j = y

    x = 0
    y = r

    d = 1 - r

    while x < y:
        glPointSize(1.5)
        glBegin(GL_POINTS)
        glVertex2f(i+x+400, 400+j+y)
        glVertex2f(i+y+400, 400+j+x)
        glVertex2f(i-x+400, 400+j+y)
        glVertex2f(i+y+400, 400+j-x)
        glVertex2f(i-y+400, 400+j-x)
        glVertex2f(i-x+400, 400+j-y)
        glVertex2f(i+x+400, 400+j-y)
        glVertex2f(i-y+400, 400+j+x)
        glEnd()

        if d < 0:

            d = d + 2*x + 3
            x = x + 1

        else:

            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 800, 0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def show():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)


    Mid_Point_Circle_Algo(r,x=0,y=0)

    #SMALL RADIUS
    r1 = r/2

    #RIGHT CIRCLE
    Mid_Point_Circle_Algo(r1,r1,0)
    #ABOVE CIRCLE
    Mid_Point_Circle_Algo(r1, 0, r1)
    #BELOW CIRCLE
    Mid_Point_Circle_Algo(r1, 0, -1 * r1)
    #LEFT CIRCLE
    Mid_Point_Circle_Algo(r1, -1 * r1, 0)

    #FOR DIAGONAL
    diagonal = math.sqrt((r1**2)/2)
    r2 = diagonal

    #NORTH EAST CIRCLE
    Mid_Point_Circle_Algo(r1, r2, r2)
    #NORTH WEST CIRCLE
    Mid_Point_Circle_Algo(r1, -1*r2, r2)
    #SOUTH WEST CIRCLE
    Mid_Point_Circle_Algo(r1, -1*r2, -1*r2)
    #SOUTH EAST CIRCLE
    Mid_Point_Circle_Algo(r1, r2, -1 * r2)


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Mid Point Circle Drawing Algorithm") #window name
glutDisplayFunc(show)

glutMainLoop()

