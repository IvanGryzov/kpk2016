from tkinter import *
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']


def start_command():
    pass


def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)

    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        # FIXME: нужно учесть объект в очках
        create_random_ball()


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста!
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)


def init_ball_catch_game():
    """
    Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root = Tk()
    root.title("Поймай шарик")

    canvas = Canvas(root, width=600, height=600, bg="white", cursor="pencil")
    text1 = Text(root, height=1, width=6, wrap=NONE)
    button1 = Button(root, text="Button 1", command=start_command)

    #button2 = Button(root, text="Button 2", command=reset_command)
    #button1.bind("<Button>", print_hello)

    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.grid(row=1, column=0, columnspan=3)
    button1.grid(row=0, column=0)
    text1.grid(row=0, column=2)
    """

    scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=5, to=100, tickinterval=10, resolution=5, variable=sc,
                   command=scale_change)

    check1 = Checkbutton(root, text="Включить/выключить оси координат", variable=c1, onvalue=1, offvalue=0,
                         command=check_change)
    scrollbar1 = Scrollbar(root)

    scrollbar1.config(command = text1.yview)
    main_canvas.bind("<Button>", change_00)
    __center_x, __center_y = int(main_canvas['width']) // 2, int(main_canvas['height']) // 2
    x_current, y_current = 0, 0


    main_canvas.grid(row=1, column=0, columnspan=3)
    check1.grid(row=0, column=0)
    scale1.grid(row=0, column=2, columnspan=2)
    text1.grid(row=1, column=3)
    scrollbar1.grid(row=1, column=4, sticky=N+S)
    """



if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите поиграть ещё!")