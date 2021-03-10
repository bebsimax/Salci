import matplotlib.pyplot as plt
import numpy as np
import random


def draw_arrow_2d(start, end, both=False):
    if end[0]<start[0]:
        temp = end
        end = start
        start = temp
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    length = ((end_x-start_x)**2 + (end_y-start_y)**2)**0.5
    a = (end_y - start_y)/(end_x - start_x)
    alfa = np.arctan(a)
    arrow_size = length/10
    dx1 = np.cos(alfa) * arrow_size
    dy1 = np.sin(alfa) * arrow_size
    x1 = end_x - dx1
    y1 = end_y - dy1
    a2 = -1/a
    alfa2 = np.arctan(a2)
    dx2 = np.cos(alfa2)*arrow_size/2
    dy2 = np.sin(alfa2)*arrow_size/2
    x2 = x1 + dx2
    y2 = y1 + dy2
    x3 = x1 - dx2
    y3 = y1 - dy2
    plt.plot([end_x, x2], [end_y, y2], "black")
    plt.plot([end_x, x3], [end_y, y3], "black")
    plt.plot([x2, x3], [y2, y3], "black")

    if both is True:
        x_1 = start_x + dx1
        y_1 = start_y + dy1
        x2 = x_1 + dx2
        y2 = y_1 + dy2
        x3 = x_1 - dx2
        y3 = y_1 - dy2
        plt.plot([start_x, x2], [start_y, y2], "black")
        plt.plot([start_x, x3], [start_y, y3], "black")
        plt.plot([x2, x3], [y2, y3], "black")

    if both is True:
        x = [x_1, x1]
        y = [y_1, y1]
    else:
        x = [start_x, x1]
        y = [start_y, y1]

    plt.plot(x, y, 'black')


def draw_rectangle(start, end):
    if end[0]<start[0]:
        temp = end
        end = start
        start = temp
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    dx = end_x - start_x
    dy = end_y - start_y
    plt.plot([start_x, start_x+dx], [start_y, start_y], "black")
    plt.plot([start_x, start_x], [start_y, start_y + dy], "black")
    plt.plot([start_x + dx, start_x + dx], [start_y, start_y + dy], "black")
    plt.plot([start_x, start_x + dx], [start_y + dy, start_y + dy], "black")


def draw_circle(start, radius):
    a = start[0]
    b = start[1]
    r = radius
    x = []
    y = []
    y_m = []
    for t in range(0, 314):
        t = t/100
        x.append(a + r*np.cos(t))
        y.append(b + r*np.sin(t))
        y_m.append(b - r*np.sin(t))
    plt.plot(x, y, "black")
    plt.plot(x, y_m, "black")



def draw_triangle(start, size, angle=-90):
    alfa1 = np.deg2rad(angle) + np.deg2rad(30)
    alfa2 = np.deg2rad(angle) + np.deg2rad(-30)
    xs = start[0]
    ys = start[1]
    dx1 = size * np.cos(alfa1)
    dy1 = size * np.sin(alfa1)
    x1 = xs + dx1
    y1 = ys + dy1
    dx2 = size * np.cos(alfa2)
    dy2 = size * np.sin(alfa2)
    x2 = xs + dx2
    y2 = ys + dy2
    plt.plot([xs, x1], [ys, y1], "black")
    plt.plot([xs, x2], [ys, y2], "blue")
    plt.plot([x1, x2], [y1, y2], "orange")






for x in range(10):
    x = [random.randint(-50, 50) for x in range(2)]
    y = random.randint(-360, 360)
    z = random.randint(5, 10)
    draw_triangle(start=x, size=z, angle=y)
#draw_triangle([-10, -15], 20, -200)
plt.grid(b=True)
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()
