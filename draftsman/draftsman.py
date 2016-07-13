from tkinter import *

root = Tk()
c1 = IntVar()
main_canvas = Canvas(root, width=600, height=600, bg="lightblue", cursor="pencil")
scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=5, to=100, tickinterval=10, resolution=5)
check1 = Checkbutton(root, text="Включить/выключить оси координат", variable=c1, onvalue=1, offvalue=0)
text = Text(root, height=43, width=30)
"""
  0   1   2   3
+---+---+---+---+
|   |   |   |   | 0
+---+---+---+---+
|   |   |   |   | 1
+---+---+---+---+

"""
main_canvas.grid(row=1, column=0, columnspan=3)
check1.grid(row=0, column=0)
scale1.grid(row=0, column=2, columnspan=2)
text.grid(row=1, column=3)

root.mainloop()
