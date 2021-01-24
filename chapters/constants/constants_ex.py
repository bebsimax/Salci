
import random

class ExerciseList:
    def __init__(self):
        self.exercises = []
    def __call__(self, exercise):
        self.exercises.append(exercise)
    def __iter__(self):
        for func in self.exercises:
            yield func
    def __getitem__(self, index):
        return self.exercises[index]
    def __len__(self):
        return len(self.exercises)
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
    solution = None
    image = None
    answer = constant.symbol
    return (text, solution, answer, image)

@exercise_decorator
def symbol_by_value_ex():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the symbol of constant with value {:.2e} ?'.format(constant.value)
    solution = None
    image = None
    answer = constant.symbol
    return (text, solution, answer, image)

@exercise_decorator
def name_by_symbol():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the name of constant with symbol {} ?'.format(constant.symbol)
    solution = None
    image = None
    answer = constant.name
    return (text, solution, answer, image)


@exercise_decorator
def name_by_value():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the name of constant with value {:.2e} ?'.format(constant.value)
    solution = None
    image = None
    answer = constant.name
    return (text, solution, answer, image)

@exercise_decorator
def value_by_name():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the value of constant named {} ?'.format(constant.name)
    solution = None
    image = None
    answer = constant.value
    return (text, solution, answer, image)


@exercise_decorator
def value_by_symbol():
    constant = random.choice(list(constant_d.registry.values()))
    text = 'What is the value of constant with symbol {} ?'.format(constant.symbol)
    solution = None
    image = None
    answer = constant.value
    return (text, solution, answer, image)









