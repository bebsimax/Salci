import matplotlib.pyplot as plt
import os

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

this_folder = os.path.dirname(os.path.abspath(__file__))
this_folder = this_folder.split('\\')
this_folder = this_folder[:-2]
main_folder = ''
for part in this_folder:
    main_folder += part+'\\'
else:
    main_folder += 'image.jpg'



y = [4, 3, 1, 2, 4, 8, 1, 3]
x = [a for a in range(len(y))]

plt.plot(x,y)



plt.savefig(main_folder, dpi=200)



@exercise_decorator
def symbol_by_name_ex():
    text='dupsko'
    solution = None
    answer = 'pikczer'
    image = None
    return (text, solution, answer, image)