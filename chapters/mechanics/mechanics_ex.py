from PackedExercise import PackedExercise
from ExerciseList import ExerciseList
from greek_letters import greek_letters
from vector_length import vector_length
import random
import numpy as np
from plot_drawing import *
exercise_decorator = ExerciseList()


@exercise_decorator
def vectors():
    start_p1 = [0, 0]
    end_p1 = [random.randint(1, 10) for x in range(2)]
    end_p2 = [random.randint(1, 10) for x in range(2)]
    phi = random.randint(1, 180)
    phi_greek = greek_letters["Small"]["Phi"]
    p1_length = vector_length(start_p1, end_p1)
    p2_length = vector_length(start_p1, end_p2)
    answer = (p1_length**2+p2_length**2+2*p1_length*p2_length*np.cos(phi))
    draw_arrow_2d(start_p1, end_p1)
    draw_arrow_2d(start_p1, end_p2)
    image = plt.gcf()
    image.set_size_inches(5.8, 4)
    y_max = max(end_p1[1], end_p2[1])
    plt.xlim(0, y_max)
    plt.ylim(0, y_max)
    answer = ()
    text = """P1 = """.format(phi_greek)
    solution = """au"""
    return PackedExercise(text=text, answer=answer, solution=solution, image=image)
