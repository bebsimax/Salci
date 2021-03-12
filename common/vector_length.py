def vector_length(start, end):
    x_start, y_start = start[0], start[1]
    x_end, y_end = end[0], end[1]
    return ((x_end-x_start)**2+(y_end-y_start)**2)**0.5


