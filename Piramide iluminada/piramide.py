from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi, sqrt


def calcula_normal(v0,v1,v2,Invertida=False):
    x = 0
    y = 1
    z = 2
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    if Invertida:
        return ( -N[x]/NLength, -N[y]/NLength, -N[z]/NLength)
    else:
        return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)



def piramide():
    raio = 2
    N = 4 #numero de lados
    H = 2 # altura
    pontosBase = []
    angulo = (2*pi)/N

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(-90,1.0,0.0,0.0)

    # BASE - é virada pra dentro,devido a isso, normal invertida

    for i in range(0,N):
        x = raio * cos(i*angulo)
        y = raio * sin(i*angulo)
        pontosBase += [ (x,y) ]

    u = (pontosBase[0][0], pontosBase[0][1], 0)
    v = (pontosBase[1][0], pontosBase[1][1], 0)
    p = (pontosBase[2][0], pontosBase[2][1], 0)
    
    glBegin(GL_POLYGON)
    # normal
    glNormal3fv(calcula_normal(u,v,p,True))

    for v in pontosBase:    
        glVertex3f(v[0],v[1],0)
        

    glEnd()


    # LATERAL
    glBegin(GL_TRIANGLES)
    for i in range(0,N):

        u = (pontosBase[i][0],pontosBase[i][1],0.0)
        v = (pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        p = (0,0,H)
        glNormal3fv(calcula_normal(u,v,p))
        glVertex3fv(u)
        glVertex3fv(v)
        glVertex3fv(p)

    glEnd()

    glPopMatrix()


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    piramide()
    glRotatef(1,0.0,1.0,0.0)
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera Virtual
    #          onde    Pra onde     posição superior
    gluLookAt( 10,0,0,   0,0,0,     0,1,0 )

def init():

    mat_ambient = (0.19225,  0.19225,  0.19225,  1.0)
    mat_diffuse = (0.50754,  0.50754,  0.50754,  1.0)
    mat_specular = (0.508273,  0.508273,  0.508273,  1.0)
    mat_shininess = (50.2)
    light_position = (-10.0, 0.0, -5.0, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutReshapeFunc(reshape)
glutDisplayFunc(desenha)
init()
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()
