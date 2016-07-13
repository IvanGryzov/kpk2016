from tkinter import *

# Переменные - состояние Чертежника
# Масштаб
__draftman_scale = 5
# Рисовать Оси координат?
__grid_drawing = True
# координаты центра в точках Черепахи
__center_x = 0
__center_y = 0
# Список выполненных операций
_operation = []
# Признак поднятости пера
__penup = True
# текущий цвет рисования
__color="black"


def __repaint():
    """
    Печать статуса
    :return:
    """
    global x_current, y_current, __penup

    main_canvas.delete("all")
    if __grid_drawing:
        __draw_grid(__center_x, __center_y)
    color="black"
    x_current, y_current = 0, 0
    for op, x, y, c in _operation:
        if op==1:
            __penup = False
        elif op==2:
            __penup = True
        elif op==3:
            if not __penup:
                main_canvas.create_line(__center_x + __draftman_scale * x_current,
                                        __center_y - __draftman_scale * y_current,
                                        __center_x + __draftman_scale * x, __center_y - __draftman_scale * y, fill=color)
            x_current = x
            y_current = y
        elif op==4:
            if not __penup:
                main_canvas.create_line(__center_x + __draftman_scale * x_current,
                                        __center_y - __draftman_scale * y_current,
                                        __center_x + __draftman_scale * (x_current + x),
                                        __center_y - __draftman_scale * (y_current + y), fill=color)
            x_current = x_current + x
            y_current = y_current + y
        elif op==5:
            color=c

    # print(__center_x, __center_y, __draftman_scale, __grid_drawing)


def __draw_grid(x0=__center_x, y0=__center_y):
    """
    Рисует оси координат
    :param x0:
    :param y0:
    :return:
    """
    global __center_x, __center_y
    # print(x0, y0)
    __center_x = x0
    __center_y = y0
    h = int(main_canvas['height'])
    w = int(main_canvas['width'])
    h2 = int(h / 2)
    w2 = int(w / 2)
    main_canvas.delete("all")

    for x in range(__center_x, w, __draftman_scale):
        main_canvas.create_line(x, 0, x, h, fill="gray")

    for x in range(__center_x, 0, -__draftman_scale):
        main_canvas.create_line(x, 0, x, h, fill="gray")

    for y in range(__center_y, h, __draftman_scale):
        main_canvas.create_line(0, y, w, y, fill="gray")

    for y in range(__center_y, 0, -__draftman_scale):
        main_canvas.create_line(0, y, w, y, fill="gray")

    main_canvas.create_line(0, __center_y, w, __center_y, width=2, fill="black")
    main_canvas.create_line(__center_x, 0, __center_x, h, width=2, fill="black")
    if __draftman_scale < 20:
        _dx = 3
    else:
        _dx = 1

    xx = 0
    for x in range(__center_x, w, __draftman_scale * _dx):
        main_canvas.create_text(x + 7, __center_y + 7, text=str(xx), font="Verdana 8")
        xx += _dx
    xx = 0
    for x in range(__center_x, 0, -__draftman_scale * _dx):
        main_canvas.create_text(x + 7, __center_y + 7, text=str(xx), font="Verdana 8")
        xx -= _dx

    yy = 0
    for y in range(__center_y, h, __draftman_scale * _dx):
        main_canvas.create_text(__center_x + 7, y + 7, text=str(-yy), font="Verdana 8")
        yy += _dx

    yy = 0
    for y in range(__center_y, 0, -__draftman_scale * _dx):
        main_canvas.create_text(__center_x + 7, y + 7, text=str(-yy), font="Verdana 8")
        yy -= _dx


def pen_down():
    global __penup
    __penup = False
    _operation.append((1, 0, 0, 0))
    text1.insert(END,"Опустить перо\n")


def pen_up():
    global __penup
    __penup = True
    _operation.append((2, 0, 0, 0))
    text1.insert(END, "Поднять перо\n")


def on_vector(dx, dy):
    global x_current, y_current, main_canvas
    _operation.append((4, dx, dy, __color))
    text1.insert(END, "На вектор("+str(dx)+","+str(dy)+")\n")
    if not __penup:
        main_canvas.create_line(__center_x + __draftman_scale * x_current, __center_y - __draftman_scale * y_current,
                                __center_x + __draftman_scale * (x_current+dx), __center_y - __draftman_scale * (y_current-dy), fill=__color)
    x_current = x_current+dx
    y_current = y_current-dy
    #print(__center_x + __draftman_scale * x_current, __center_y - __draftman_scale * y_current,
    #                            __center_x + __draftman_scale * (x_current+dx), __center_y - __draftman_scale * (y_current-dy))



def to_point(x, y):
    global x_current, y_current, main_canvas
    _operation.append((3, x, y, __color))
    text1.insert(END, "В точку(" + str(x) + "," + str(y) + ")\n")
    if not __penup:
        main_canvas.create_line(__center_x + __draftman_scale * x_current, __center_y - __draftman_scale * y_current,
                                __center_x + __draftman_scale * x, __center_y - __draftman_scale * y, fill=__color)
    x_current = x
    y_current = y
    #print(__center_x + __draftman_scale * x_current, __center_y - __draftman_scale * y_current,
    #      __center_x + __draftman_scale * x, __center_y - __draftman_scale * y)


def setcolor(c):
    global __color
    __color=c
    _operation.append((5, 0, 0, c))
    text1.insert(END, "Цвет('"+ c +"')\n")


def change_00(event):
    """
    Изменение точки начала координат
    :param event:
    :return: None
    """
    global __center_x, __center_y
    __center_x = event.x
    __center_y = event.y
    __repaint()


def scale_change(self):
    """
    Изменяет масштаб чертежа
    :param self:
    :return:
    """
    global __draftman_scale
    __draftman_scale = scale1.get()
    __repaint()


def check_change():
    """
    Включает или выключает систему координат
    :param self:
    :return:
    """
    global __grid_drawing
    __grid_drawing = c1.get() == 1
    __repaint()


def init_main_window():
    """
    Начальная инициализация экрана
    :return:
    """
    global root, main_canvas, scale1, check1, text1, c1, __center_x, __center_y, __penup, x_current, y_current, scrollbar1, __color
    root = Tk()
    root.title("Чертежник")
    c1 = IntVar()
    sc = IntVar()
    sc.set(__draftman_scale)
    if __grid_drawing:
        c1.set(1)
    else:
        c1.set(0)
    __penup = True
    __color="black"
    main_canvas = Canvas(root, width=600, height=600, bg="lightgray", cursor="pencil")

    scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=5, to=100, tickinterval=10, resolution=5, variable=sc,
                   command=scale_change)

    check1 = Checkbutton(root, text="Включить/выключить оси координат", variable=c1, onvalue=1, offvalue=0,
                         command=check_change)
    scrollbar1 = Scrollbar(root)
    text1 = Text(root, height=43, width=30,yscrollcommand = scrollbar1.set)
    scrollbar1.config(command = text1.yview)
    main_canvas.bind("<Button>", change_00)
    __center_x, __center_y = int(main_canvas['width']) // 2, int(main_canvas['height']) // 2
    x_current, y_current = 0, 0

    """
      0   1   2   3
    +---+---+---+---+
    |   |   |       | 0
    +---+---+---+---+
    |           |   | 1
    +---+---+---+---+

    """
    main_canvas.grid(row=1, column=0, columnspan=3)
    check1.grid(row=0, column=0)
    scale1.grid(row=0, column=2, columnspan=2)
    text1.grid(row=1, column=3)
    scrollbar1.grid(row=1, column=4, sticky=N+S)


def paint():
    root.mainloop()


def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    for i in range(30):
        pen_down()
        setcolor("yellow")
        on_vector(2, 5)
        #pen_up()
        setcolor("blue")
        on_vector(0, -5)
    pen_up()
    to_point(0, 0)


init_main_window()

if __name__ == "__main__":

    test_drawman()
    paint()
