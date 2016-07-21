from tkinter import *
from random import choice, randint


# Глобальные константы
timer_delay = 10 # Время между изменениями обстановки в миллисекундах
num_of_targets = 20 # Число мишеней

class Ball:
    """
    класс - родитель для мишеней и снарядов
    """
    def __init__(self, x=0, y=0, r=10, vx=1, vy=0, color='red', a=0):
        """
        Коструктор класса - родителя создает шарик с заданными параметрами
        :param x: координата по x
        :param y: координата по y
        :param r: радиус шарика
        :param color: цвет шарика
        """
        # сохраняем параметры во внутренних атрибутах класса
        self._x = x
        self._y = y
        self._r = r
        self._vx = vx
        self._vy = vy
        self._color = color
        self._a = a # ускорение

        self._picture = canvas.create_oval(x, y, x + 2 * r, y + 2 * r, width=1, fill=color,outline=color)

    def move_ball(self):
        """
        перемещает шарик без контроля выхода за экран !!! движение равноускоренное _a - ускорение
        :return: None
        """
        canvas.move(self._picture, self._vx, self._vy)
        self._x += self._vx
        self._y += self._vy + self._a/2
        self._vy += self._a

    def delete_ball(self):
        """
        Удалеем гравфичесое изображение шарика сам объект не удаляется
        :return: None
        """
        canvas.delete(self._picture)

class Target(Ball):
    """
    Класс для мишени построен на основе класса Шарик
    """
    minimal_radius = 6 #  Минимальный радиус мишени
    maximal_radius = 20 # Максимальный радиус мишени
    available_colors = ['green', 'blue', 'red', 'yellow','gray'] # Доступные цвета
    __xmin = 20
    __ymin = 0

    def __init__(self):
        """
        Создает шарик в случайном месте, случайного радиуса и цвета
        """
        h = int(canvas['height'])
        w = int(canvas['width'])
        R = randint(Target.minimal_radius, Target.maximal_radius)
        x = randint(self.__xmin, w - 1 - 2 * R)
        y = randint(self.__ymin, h - 1 - 2 * R)
        color = choice(Target.available_colors)
        vx = randint(-1, 1)
        vy = randint(-1, 1)
        while vx == 0 and vy == 0:
            vx = randint(-1, 1)
            vy = randint(-1, 1)
        super().__init__(x, y, R, vx, vy, color)

    def move_target(self):
        """
        Перемащает мишень с учетом границ
        :return: None
        """
        h = int(canvas['height'])
        w = int(canvas['width'])
        if self._x + self._vx >=w-2*self._r or self._x + self._vx <=self.__xmin:
            self._vx = - self._vx
        if self._y + self._vy >= h - 2 * self._r or self._y + self._vy <= self.__ymin:
            self._vy = - self._vy
        super().move_ball()


def do_shoot():
    pass


def init_game():
    global targets, gun, shells
    targets = [Target() for i in range(num_of_targets)]


    pass


def start_game():
    pass

def timer_event():
    # все периодические рассчёты, которые я хочу, делаю здесь
    for target in targets:
        target._a=0.001
        target.move_target()
    canvas.after(timer_delay, timer_event)



def init_main_window():
    """
    Создает окно и элементы упраления
    :return:
    """
    global root, canvas, score_text, score_value

    root = Tk()
    root.title("Cannon Game")
    # создаем элементы управления
    score_value=IntVar()
    canvas = Canvas(root, width=800, height=600, bg="white", cursor="pencil")
    score_text = Entry(root, textvariable=score_value)
    button1 = Button(root, text="Start game", command=start_game)
    # привязка событий

    canvas.bind("<Button>", do_shoot)
    #canvas.bind("<Motion>", move_all_balls)
    #Создание геометрии
    canvas.grid(row=1, column=0, columnspan=3)
    button1.grid(row=0, column=0)
    score_text.grid(row=0, column=2)


if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
