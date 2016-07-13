from tkinter import *

# Переменные - состояние Чертежника
# Масштаб
__draftman_scale=15
# Рисовать Оси координат?
__grid_drawing=True
# координаты центра в точках Черепахи
__center_x=0
__center_y=0
# Список выполненных операций
_operation=[]

def print_status():
    """
    Печать статуса
    :return:
    """
    print(__center_x, __center_y, __draftman_scale, __grid_drawing)

def change_00(event):
    """
    Изменение точки начала координат
    :param event:
    :return: None
    """
    global __center_x,  __center_y
    __center_x = event.x
    __center_y = event.y
    print_status()


def scale_change(self):
    """
    Изменяет масштаб чертежа
    :param self:
    :return:
    """
    global __draftman_scale
    __draftman_scale =scale1.get()
    print_status()


def check_change():
    """
    Включает или выключает систему координат
    :param self:
    :return:
    """
    global __grid_drawing
    __grid_drawing= c1.get() == 1
    print_status()


def init_main_window():
    """
    Начальная инициализация экрана
    :return:
    """
    global root, main_canvas, scale1, check1, text1, c1, __center_x,  __center_y
    root = Tk()
    root.title("Чертежник")
    c1 = IntVar()
    sc = IntVar()
    sc.set(__draftman_scale)
    if __grid_drawing:
        c1.set(1)
    else:
        c1.set(0)
    main_canvas = Canvas(root, width=600, height=600, bg="lightblue", cursor="pencil")

    scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=5, to=100, tickinterval=10, resolution=5, variable=sc,
                   command=scale_change)

    check1 = Checkbutton(root, text="Включить/выключить оси координат", variable=c1, onvalue=1, offvalue=0,
                         command=check_change)

    text1 = Text(root, height=43, width=30)

    main_canvas.bind("<Button>", change_00)
    __center_x, __center_y= int(main_canvas['width']) / 2, int(main_canvas['width']) / 2

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


if __name__ == "__main__":
    init_main_window()
    root.mainloop()
