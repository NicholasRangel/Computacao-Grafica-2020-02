from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi, sqrt


#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def calcula_normal(v0,v1,v2, Invertida=False): #normal se envertida, adicionar True
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

def prisma():
    raio = 2
    N = 5
    H = 4
    pontosBase = []
    angulo = (2*pi)/N

    glPushMatrix()
    #glTranslatef(0,-2,0)
    #glRotatef(a,0.0,1.0,0.0)
    glRotatef(110,1.0,0.0,0.0)
    #glRotatef(120,1.0,0.0,0.0)
    #glColor3fv(cores[0])

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
    glNormal3fv(calcula_normal(u,v,p))
    for v in pontosBase:
        glVertex3f(v[0],v[1],0)
    
    glEnd()

    # TOPO
    glBegin(GL_POLYGON)
    u = (pontosBase[0][0], pontosBase[0][1], H)
    v = (pontosBase[1][0], pontosBase[1][1], H)
    p = (pontosBase[2][0], pontosBase[2][1], H)
    glNormal3fv(calcula_normal(u,v,p,True))
    for i in range(0,N):
        glVertex3f(pontosBase[i][0],pontosBase[i][1],H)
    
    glEnd()

    # LATERAL
    glBegin(GL_QUADS)
    for i in range(0,N):
        #u = ((pontosBase[i][0]),(pontosBase[i][1]),(0.0))
        #v = ((pontosBase[i][0]),(pontosBase[i][1]),(H))
        #p = ((pontosBase[(i+1)%N][0]),(pontosBase[(i+1)%N][1]),(H))
        #q = ((pontosBase[(i+1)%N][0]),(pontosBase[(i+1)%N][1]),(0.0))

        u = ((pontosBase[i][0]),(pontosBase[i][1]),(0.0))
        v = ((pontosBase[i][0]),(pontosBase[i][1]),(H))
        p = ((pontosBase[(i+1)%N][0]),(pontosBase[(i+1)%N][1]),(H))
        q = ((pontosBase[(i+1)%N][0]),(pontosBase[(i+1)%N][1]),(0.0))
        glNormal3fv(calcula_normal(u,v,p))
        glVertex3fv(u)
        glVertex3fv(v)
        glVertex3fv(p)
        glVertex3fv(q)
        

    glEnd()

    glPopMatrix()


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    prisma()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera Virtual
    #          onde    Pra onde   up-size
    gluLookAt( 0,0,10, 0,0,0,     1,1,1 ) #x-largura,y-altura,z-profundidade

def init():

    mat_ambient = (0.25,  0.20725,  0.20725,  0.922)
    mat_diffuse = (1.0,  0.829,  0.829,  0.922)
    mat_specular = (0.296648,  0.296648,  0.296648,  0.922)
    mat_shininess = (11.264)
    light_position = (5,0,0,0)
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
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
init()
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()
