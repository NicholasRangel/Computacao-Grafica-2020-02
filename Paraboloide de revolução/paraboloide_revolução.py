from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math



def f(i,j):
    theta = (math.pi*i/(n1-1))-(math.pi/2)
    phi = 2*math.pi*j/(n2-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x,y**2,z

a = 0
n1 = 50
n2 = 50
r = 2


def mesh():
    glPushMatrix()
    glRotatef(-170,1.0,0.0,0.0)
    glRotatef(a,0.0,1.0,0.1)
    
    
    

    

    for i in range(round(n1/2)): #theta
        glBegin(GL_QUAD_STRIP)
        glColor3fv(((1.0*(i+1)/(n1-1)),0,1 - (1.0*(i+1)/(n1-1))))
        for j in range(n2): #phi
            x,y,z = f(i,j)
            glVertex3f(x,y,z)
            x,y,z = f(i+1,j)
            glVertex3f(x,y,z)
            
        glEnd()
    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1024,1024)
glutCreateWindow("paraboloide de revolucao")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(10,timer,1)
glutMainLoop()
