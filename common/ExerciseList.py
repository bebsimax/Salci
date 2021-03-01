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
