from tkinter import *
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']


def start_command():
    global score
    score.set(0)
    canvas.delete("all")
    init_ball_catch_game()


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
        score.set(score.get()+1)
        create_random_ball()


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    """
    k = 0
    for obj in canvas.find_all():
        #dx = randint(-1, 1)
        #dy = randint(-1, 1)
        h = int(canvas['height'])
        w = int(canvas['width'])
        x1, y1, x2, y2 = canvas.coords(obj)
        if x1<3 or x2>w-3:
            v[k][0]=-v[k][0]
        if y1 < 3 or y2>h-3:
            v[k][1] = -v[k][1]
        canvas.move(obj, v[k][0],v[k][1])
        k+=1


def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста!
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    fillcolor=random_color()
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fillcolor, outline=fillcolor)


def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)


def init_ball_catch_game():
    """
    Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    global v
    v=[]
    for i in range(ball_initial_number):
        vx = randint(-1, 1)
        vy = randint(-1, 1)
        while vx==0 and vy==0:
            vx = randint(-1, 1)
            vy = randint(-1, 1)
        v.append([vx,vy])
        create_random_ball()


def init_main_window():
    global root, canvas, text1, score, v

    root = Tk()
    root.title("Поймай шарик")
    v=[]
    score=IntVar()
    canvas = Canvas(root, width=600, height=600, bg="white", cursor="pencil")
    text1 = Entry(root, textvariable=score)
    button1 = Button(root, text="Start game", command=start_command)

    #button2 = Button(root, text="Button 2", command=reset_command)
    #button1.bind("<Button>", print_hello)

    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.grid(row=1, column=0, columnspan=3)
    button1.grid(row=0, column=0)
    text1.grid(row=0, column=2)


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите поиграть ещё!")