from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# دي طريقة ممكن تساعد بتوع الكوليجن يعني

# القيمة دي معتمدة على نص قطر التورس الخارجي ممكن نقلل منه
# حبة يعني بحيث يقعد لما يطلع منه كله او نصه ممكن نخليها 0.7

front_collision = 1.4


# FUNCTION TO TEST MY CODE


def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()  # F


# Initial Value to my code
def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(0, 9, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0.4, 0.2, 0.7, 1)


angle = 0
CHANGE_COLOR = 0

forward = True

up = 0


def draw():
    global angle
    global CHANGE_COLOR, up, r
    global forward
    # HERE TO CLEAR THE BACK. COLOR AND TEST THE Z-BUFFER (O. CULLING )
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # HERE TO TEST THE PREVIOUS ONE
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # TEST SCENE
    draw_XYZ()
    # DRAW TORUS WITH CHANGED COLOR
    glColor3f(1, CHANGE_COLOR, CHANGE_COLOR)
    glTranslate(up, 0, r)  # TRANSLATE IN RESPONSE TO KEYBOARD
    glRotate(angle, 0, 1, 0)  # TO ROTATE
    glRotate(90, 1, 0, 0)  # TO DRAW OUR TOURUS IN WANTED VIEW " قبل كدة كان بيترسم عمودي مش نايم على الارضية "
    glutSolidTorus(0.2, 1.2, 5, 5)
    glLoadIdentity()
    # DRAW OUR SPHERE
    glTranslate(up, 0, r)  # TRANSLATE IN RESPONSE TO KEYBOARD
    glColor3f(1, 1, 1)
    glutSolidSphere(0.5, 10, 10)
    glLoadIdentity()

    glutSwapBuffers()
    # HERE FUNCTION TO CHANGE THE MODEL COLOR " IF ITS ( g , b ) IN RANGE 0 , 1 ..
    # INCREASE THEM BY 0.05 .. IF IT EQUALS TO 1 ( WHITE COLOUR ) CHANGE THEM IMMEDIATLY TO 0 TO BE RED
    if 1 >= CHANGE_COLOR >= 0:
        CHANGE_COLOR += 0.05
        if CHANGE_COLOR >= 1:
            CHANGE_COLOR = 0

    angle += 1  # HERE THE ANGLE TO ROTATE THE TORUS


# THIS FUNCTION TO DRAW THE MODEL MOVING IN Z-AXIS

def drawz():
    glRotate(90, 0, 1, 0)
    draw()
    glLoadIdentity()


r: " بيتحكم في الحركة الجانبية  يمين وشمال" = 0

col_R = True  # collision right قيمة ابتدائية للتجربة
col_L = True  # collision left قيمة ابتدائية للتجربة


def Key(key,x,y):
    # اللي هيعمل الدوران والكوليشن يحط شرط يغير قيمة col_R
    # يعني لو في كوليشن يمين قبل يتحرك ويتنقل عالطريق يحصله الروتيت
    # لو مفيش كوليشن يمين يقع يموت ويجيب الفانكشن اللي هي Gameover
    # وكذلك على col_L
    # هنا هنشوف الكوليشن هيقع امتى لو اي شرط من الاتنين دول متحققوش
    # اما الفوروارد اكبر من ناهية الطريق اللي هو عليه ف ساعتها يقع
    # او الفوروارد اقل من بداية الطريق اللي هو لسة هيروح عليه
    # وممكن برضو المقارنة تتم تعمل back_collision وتعمل مقارنة بين نهاية الاوبجيكت و بداية الطريق التاني اللي هيمشي عليه

    global r, front_collision
    global up, forward
    if key == GLUT_KEY_UP:
        up += 1
        front_collision += 1

    elif key == GLUT_KEY_DOWN:
        up -= 1
        front_collision -= 1
    elif key == GLUT_KEY_LEFT and col_L:
        r -= 1
    elif key == GLUT_KEY_RIGHT and col_R:
        r += 1


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"our Model")
myInit()
glutSpecialFunc(Key)
glutDisplayFunc(drawz)
glutIdleFunc(drawz)
glutMainLoop()
