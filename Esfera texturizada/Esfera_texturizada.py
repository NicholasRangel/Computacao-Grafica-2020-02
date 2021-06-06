from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import png

from math import pi, cos, sin

#texturas
texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(2) # Gera 2 IDs para as texturas

    ################################################################################
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

#Cacacteristicas da esfera
def f(i,j):
    theta = ( (pi * i) / (n1 -1) ) - (pi / 2)
    phi = 2*pi*j/(n2-1)
    x = r * cos(theta) * cos(phi)
    y = r * sin(theta)
    z = r * cos(theta) * sin(phi)
    t = ((theta + (pi/2))/pi)
    p = (phi/(2*pi))
    return x,y,z,t,p

#variaveis da esfera
a = 0
n1 = 50
n2 = 50
r = 2

#criação do objeto
def mesh():
    glPushMatrix()
    glRotatef(a,1.0,0.0,0.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    for i in range(n1):
        
        glBegin(GL_QUAD_STRIP)
        for j in range(n2):
            
            x, y, z, t, p = f(i,j)
            glTexCoord2f(p, t)
            glVertex3f(x,y,z)
            

            x, y, z, t, p = f(i+1, j)
            glTexCoord2f(p, t)
            glVertex3f(x,y,z)
            
        glEnd()


    glPopMatrix()

#desenho do objeto
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
glutCreateWindow("Esfera Texturizada")
glutDisplayFunc(desenha)
LoadTextures()

glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)

glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()
