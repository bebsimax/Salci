import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def draw_arrow_2d(start, end, both=False):
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    x = [start_x, end_x]
    y = [start_y, end_y]
    length = ((end_x-start_x)**2 + (end_y-start_y)**2)**0.5
    a = (end_y - start_y)/(end_x - start_x)
    b = start_y-a*start_x
    alfa = np.arctan(a)
    arrow_size = length/10
    arrow_angle = 30
    print(alfa)

    dx = np.cos(alfa) * arrow_size
    dy = np.sin(alfa) * arrow_size
    print("dx {:.2e}, dy {:.2e}".format(dx, dy))
    plt.plot(end_x, end_y, 'o')
    plt.plot(end_x - dx, end_y - dy, 'o')
    #plt.plot(1.71, 3.356, 'o')
    plt.plot(x, y, 'black')

start = [1, -3]
end = [2, 4]

draw_arrow_2d(start, end)


plt.show()


