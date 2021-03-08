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


