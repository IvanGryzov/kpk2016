from turtle import Turtle

#
# Переменные - состояние Чертежника
# Масштаб по осям
default_scale_x = 40
default_scale_y = 15
_drawman_scale_x = 10
_drawman_scale_y = 10

# координаты центра в точках Черепахи
center_x=0
center_y=0
# Рисовать Оси координат?
grid_drawing=True
# Список выполненных операций
operation=[]

def draw_grid(x0=0,y0=0):
    global center_x,center_y
    center_x=x0
    center_y=y0
    t.speed(0)
    h=t.screen.window_height()
    w=t.screen.window_width()
    h2=int(h/2)
    w2=int(w/2)

    t.color('gray')
    for x in range(center_x,w2,_drawman_scale_x):
        _draw_line(x,-h2,x,h2)
    for x in range(center_x,-w2,-_drawman_scale_x):
        _draw_line(x,-h2,x,h2)
    for y in range(center_y,h2,_drawman_scale_y):
        _draw_line(-w2,y,w2,y)
    for y in range(center_y,-h2,-_drawman_scale_y):
        _draw_line(-w2,y,w2,y)
    t.pensize(2)
    t.color('black')
    _draw_line(-w2,center_y,w2,center_y)
    _draw_line(center_x,-h2,center_x,h2)
    t.pensize(1)
    t.penup()
    if _drawman_scale_x<15:
        _dx=2
    else:
        _dx=1
    xx=0
    for x in range(center_x,w2,_drawman_scale_x*_dx):
        t.goto(x+2,center_y)
        #t.write(xx,align="center")
        t.write(xx)
        xx+=_dx
    xx=0
    for x in range(center_x,-w2,-_drawman_scale_x*_dx):
        t.goto(x+2,center_y)
        #t.write(xx,align="center")
        t.write(xx)
        xx-=_dx

    if _drawman_scale_y<15:
        _dy=2
    else:
        _dy=1
    yy=0
    for y in range(center_y,h2,_drawman_scale_y*_dy):
        t.goto(center_x+2,y)
        #t.write(xx,align="center")
        t.write(yy)
        yy+=_dy
    yy=0
    for y in range(center_y,-h2,-_drawman_scale_y*_dy):
        t.goto(center_x+2,y)
        #t.write(xx,align="center")
        t.write(yy)
        yy-=_dy
    t.speed(10)

def _draw_line(x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.penup()

def init_drawman(x0=0,y0=0):
    global t, x_current, y_current
    t = Turtle()
    t.hideturtle()
    t.speed(0)


    drawman_scale(default_scale_x,default_scale_y)
    draw_grid(x0,y0)
    t.penup()
    x_current = x0
    y_current = y0
    t.goto(x_current, y_current)


def drawman_scale(scale_x,scale_y):
    global _drawman_scale_x,_drawman_scale_y
    _drawman_scale_x = scale_x
    _drawman_scale_y = scale_y

def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)


def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(center_x+_drawman_scale_x*x_current, center_y+_drawman_scale_y*y_current)


init_drawman()
if __name__ == '__main__':
    import time

    test_drawman()
    time.sleep(5)