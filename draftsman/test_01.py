from draftsman import *

def f(x):
    return x*x

pen_up()
x = -9.0
to_point(x, f(x))
pen_down()
while x <= 9:
    to_point(x, f(x))
    x += 0.1
paint()