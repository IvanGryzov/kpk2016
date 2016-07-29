# -*- coding: utf-8 -*-
#
#  Life Game
#  
#  Copyright 2016 Ivan Gryzov <ivan_gryzov@mail.ru>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from tkinter import *
import tkinter.filedialog as FileDialog
import pickle

# Глобальные парамерры

colors = ["lightblue", "black"] # Цвета мертвой/живой клеток
nun_of_cells = 100 # Размер поля по вертикали и горизонтали
size_of_cell = 20 # Размер клетки на экране
neighbors=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)] # Смещения клеток - соседей
autoplay=False # Автоматическое выполнение шагов
timer_delay=500 # Задержка между шагами в миллисекундах


def quit_apps():
    """
    Обеспечивает выхов из программы
    :return:
    """
    root.destroy()


def load_file():
    """
    Загружает файлт с конфигурацией Используется модуль pickle
    :return:
    """
    global cells
    file_name = FileDialog.Open(root, filetypes=[('*.life files', '.life')]).show()
    if file_name == '':
        return
    if not file_name.endswith(".life"):
        file_name += ".life"
    try:
        f = open(file_name, "rb")
        cells = pickle.load(f) # Загрузка упакованного объекта Cells из файла (файл не текстовый !!!!!!!!!!)
        f.close()
        repaint_all()
    except:
        pass


def save_file():
    """
    Сохраняет файл с конфигурацией Используется модуль pickle
    :return:
    """
    file_name = FileDialog.SaveAs(root, filetypes=[('*.life files', '.life')]).show()
    if file_name == '':
        return
    if not file_name.endswith(".life"):
        file_name += ".life"
    try:
        f = open(file_name, "wb")
        pickle.dump(cells, f) # Упаковка объекта Cells в файл(не текстовый !!!!!!!!!!)
        f.close()
    except:
        pass


def play_step():
    """
    Выподняет один шаг игры
    :return:
    """
    global cells, autoplay, game_over

    new_cells = [[0] * nun_of_cells for i in range(nun_of_cells)]
    null_field = [[0] * nun_of_cells for i in range(nun_of_cells)]
    for x0 in range(nun_of_cells):
        for y0 in range(nun_of_cells):
            summa = 0
            for dx, dy in neighbors:
                x = (x0 + dx + nun_of_cells) % nun_of_cells
                y = (y0 + dy + nun_of_cells) % nun_of_cells
                summa += cells[x][y]

            if cells[x0][y0]==0 and summa==3:
                new_cells[x0][y0] = 1
            elif cells[x0][y0]==1 and summa in [2,3]:
                new_cells[x0][y0] = 1
            else:
                new_cells[x0][y0] = 0
    message.set("Working")
    if str(cells)==str(new_cells) or str(new_cells) == str(null_field):
        autoplay = False
        game_over = True
    cells=new_cells
    counter.set(counter.get() + 1)
    repaint_all()


def play():
    """
    Запускает непрерывный процесс эволюции клеток
    :return:
    """
    global autoplay
    autoplay = True


def stop():
    """
    Останавливает эволюцию клеток
    :return:
    """
    global autoplay
    autoplay = False
    message.set("Idle")


def timer_event():
    """
    Выполнение непрерывного процесса эволюции
    :return:
    """
    if autoplay:
        play_step()
        message.set("Working")
    elif game_over:
        message.set("Game over")
    else:
        message.set("Idle")
    canvas.after(timer_delay, timer_event)

def repaint_all():
    """
    Перересовывыет все клетки
    :return:
    """
    for x in range(nun_of_cells):
        for y in range(nun_of_cells):
            canvas.itemconfig(screen[x][y], fill=colors[cells[x][y]])


def clear_cells():
    """
    Очищает все поле и перерисовывает клетки
    :return:
    """
    global autoplay, game_over
    autoplay = False
    game_over = False
    # Обнуление количества шагов
    counter.set(0)
    for x in range(nun_of_cells):
        for y in range(nun_of_cells):
            cells[x][y] = 0
    repaint_all()


def change_cell(event):
    """
    редактирование одной клетки
    :param event:
    :return:
    """
    global game_over
    x, y = int(canvas.canvasx(event.x) // size_of_cell), int(canvas.canvasy(event.y) // size_of_cell)
    cells[x][y] = abs(cells[x][y] - 1)
    canvas.itemconfig(screen[x][y], fill=colors[cells[x][y]])
    game_over = False
    counter.set(0)


def init_life_game():
    """
    Начальная инициализация игры
    :return:
    """
    global root, canvas, screen, cells, autoplay, counter, message, game_over
    root = Tk()
    root.title("Life")
    panel_frame = Frame(root, height=40, bg='lightgray')
    counter = IntVar()
    message = StringVar()
    step_count=Label(panel_frame, textvariable=counter, width=8, bg='lightgray')
    step_text = Label(panel_frame, text="Step:", width=6, bg='lightgray')
    message_text = Label(panel_frame, width=10, textvariable=message, bg='lightgray')
    message.set("Idle")
    canvas = Canvas(root, width=600, height=600, bg="lightblue", cursor="pencil")
    # полосы прокрутки
    hsb = Scrollbar(root, orient="h", command=canvas.xview)
    vsb = Scrollbar(root, orient="v", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    panel_frame.grid(row=0, column=0)
    canvas.grid(row=1, column=0, sticky="nsew")
    hsb.grid(row=2, column=0, stick="ew")
    vsb.grid(row=1, column=1, sticky="ns")
    # Холси и кнопки
    canvas.configure(scrollregion=(0, 0, nun_of_cells * size_of_cell, nun_of_cells * size_of_cell))
    load_button = Button(panel_frame, text='Load', command=load_file)
    save_button = Button(panel_frame, text='Save', command=save_file)
    quit_button = Button(panel_frame, text='Quit', command=quit_apps)
    play_button = Button(panel_frame, text='Play', command=play)
    step_button = Button(panel_frame, text='Step', command=play_step)
    stop_button = Button(panel_frame, text='Stop', command=stop)
    clear_button = Button(panel_frame, text='Clear', command=clear_cells)
    # Геометрия
    load_button.grid(row=0, column=1)
    save_button.grid(row=0, column=2)
    play_button.grid(row=0, column=3)
    step_button.grid(row=0, column=4)
    stop_button.grid(row=0, column=5)
    clear_button.grid(row=0, column=6)
    quit_button.grid(row=0, column=7)
    step_count.grid(row=0, column=9)
    step_text.grid(row=0, column=8)
    message_text.grid(row=0, column=10)
    # Инициализация поля из клеток
    screen = [[0] * nun_of_cells for i in range(nun_of_cells)]
    cells = [[0] * nun_of_cells for i in range(nun_of_cells)]

    autoplay = False
    game_over = False

    for x in range(nun_of_cells):
        for y in range(nun_of_cells):
            screen[x][y] = canvas.create_rectangle(x * size_of_cell, y * size_of_cell, x * size_of_cell + size_of_cell,
                                                   y * size_of_cell + size_of_cell)
    # Кнопка - изменение состояния клетки
    canvas.bind("<Button>", change_cell)


if __name__ == '__main__':
    init_life_game()
    timer_event()
    root.mainloop()
