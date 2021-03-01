from main import PackedExercise, ExerciseList
import random
import matplotlib.pyplot as plt

exercise_decorator = ExerciseList()


import os
this_folder = os.path.dirname(os.path.abspath(__file__))

class Constant():
    def __init__(self, name, symbol, value):
        self.name = name
        self.symbol = symbol
        self.value = value
    def __repr__(self):
        return '''
    Constant: {}
    Symbol: {}
    Value: {:.2e}'''.format(self.name, self.symbol, self.value)
    def __mul__(self, other):
        return self.value*other
    def __rmul__(self, other):
        return self.value*other

class Constant_Dir():
    def __init__(self):
        self.registry = {}

    def __call__(self, constant):
        self.registry.update({'{}'.format(constant.name):constant})


constant_d = Constant_Dir()


constants = os.path.join(this_folder, 'constants.txt')

for line in open(constants):
    line = line.split(',')
    name, symbol, value = (line[0], line[1], float(line[2]))
    this_constant = Constant(name, symbol, value)
    constant_d(this_constant)







@exercise_decorator
def symbol_by_name_ex():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the symbol of constant named {} ?'.format(constant.name)

    y = [random.randint(0,10) for a in range(10)]
    x = [a for a in range(len(y))]
    plt.plot(x, y)
    plt.grid()
    figure = plt.gcf()
    figure.set_size_inches(5.8, 4)
    image = figure
    answer = constant.symbol
    return PackedExercise(text=text, answer=answer, image=image, solution="au")

@exercise_decorator
def symbol_by_value_ex():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the symbol of constant with value {:.2e} ?'.format(constant.value)
    answer = constant.symbol
    return PackedExercise(text=text, answer=answer)

@exercise_decorator
def name_by_symbol():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the name of constant with symbol {} ?'.format(constant.symbol)
    answer = constant.name
    return PackedExercise(text=text, answer=answer)


@exercise_decorator
def name_by_value():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the name of constant with value {:.2e} ?'.format(constant.value)
    answer = constant.name
    return PackedExercise(text=text, answer=answer)

@exercise_decorator
def value_by_name():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the value of constant named {} ?'.format(constant.name)
    answer = constant.value
    return PackedExercise(text=text, answer=answer)


@exercise_decorator
def value_by_symbol():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the value of constant with symbol {} ?'.format(constant.symbol)
    answer = constant.value
    return PackedExercise(text=text, answer=answer)









