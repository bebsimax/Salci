
import sys
import os
import tkinter as tk
import random
import matplotlib.pyplot as plt
from importlib import import_module
from PIL import ImageTk, Image

main_folder = os.path.dirname(os.path.abspath(__file__))
chapters = os.path.join(main_folder, "chapters")
if chapters not in sys.path:
    sys.path.append(chapters)


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


class PackedExercise:
    def __init__(self, text, answer, solution=None, image=None):
        self.text = text
        self.solution = solution
        self.answer = answer
        self.image = image


class Navigation(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.Chapter_Listbox = tk.Listbox(self, bg="orange", selectmode="single", height=5, width=20)
        self.chapters = os.listdir(chapters)
        for index, chapter in enumerate(self.chapters, start=1):
            self.Chapter_Listbox.insert(index, str(index) + "." + chapter)
        
        self.Chapter_Scrollbar = tk.Scrollbar(self)
        self.Chapter_Listbox.config(yscrollcommand=self.Chapter_Scrollbar.set)
        self.Chapter_Scrollbar.config(command=self.Chapter_Listbox.yview)

        self.Ex_Listbox = tk.Listbox(self,
                                     bg="green",
                                     selectmode="single",
                                     height=5, width=20)
        
        self.Ex_Scrollbar = tk.Scrollbar(self)
        self.Ex_Listbox.config(yscrollcommand=self.Ex_Scrollbar.set)
        self.Ex_Scrollbar.config(command=self.Ex_Listbox.yview)
        
        self.Ch_Button = tk.Button(self,
                                   bg="purple",
                                   text="Load Chapter",
                                   command=self.load_ch,
                                   bd=4)
        self.Ex_Button = tk.Button(self, bg="light blue",
                                   text="Load Exercise",
                                   command=self.load_ex,
                                   state=tk.DISABLED)
        self.Chapter_Listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.Chapter_Scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.Ch_Button.pack(side=tk.LEFT, fill=tk.Y)
        self.Ex_Listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.Ex_Scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.Ex_Button.pack(side=tk.LEFT, fill=tk.Y)

    def load_ch(self):
        self.Ex_Listbox.delete(0, tk.END)
        try:
            name = self.Chapter_Listbox.get(self.Chapter_Listbox.curselection())
        except:
            return
        name = name.split(".")
        ch_number = name[0]
        name = name[1]
        module_name = name + "_ex"
        ch_path = os.path.join(chapters, name)
        if ch_path not in sys.path:
            sys.path.append(ch_path)
        ex_module = import_module(module_name)
        self.exercise_decorator = ex_module.exercise_decorator
        for number in range(len(ex_module.exercise_decorator)):
            self.Ex_Listbox.insert(number+1, str(ch_number) + ". " + str(number+1))
        self.Ex_Button.config(state=tk.NORMAL)
    def load_ex(self):
        try:
            number = self.Ex_Listbox.get(self.Ex_Listbox.curselection())
        except:
            return
        number = number.split(".")[1]
        ex = self.exercise_decorator[int(number)-1]
        
        packed_exercise = ex()
        
        self.parent.Entry.answer = packed_exercise.answer
        self.parent.Solution.solution = packed_exercise.solution

        self.clear_text()
        self.insert_text(packed_exercise.text)

        self.parent.Solution.insert_pre_sol(self.parent.Solution.solution)

        if packed_exercise.image:
            self.parent.Plot.insert_image(packed_exercise.image)
        else:
            if not self.parent.Plot.is_blank:
                self.parent.Plot.set_to_blank()
        self.parent.Entry.Button_Submit.config(state=tk.NORMAL)
        self.parent.Entry.Button_Show_Answer.config(state=tk.NORMAL)

    def clear_text(self):
        self.parent.Text.Text.delete("1.0", tk.END)

    def insert_text(self, text):
        self.parent.Text.Text.insert(tk.END, text)






class Text(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.Text = tk.Text(self,
                            bg='pink',
                            height=20, width=70)
        self.Text.insert(tk.END, """To load exercise:
1. Select chapter from first list
2. Press load chapter
3. Select exercise number
4. Press load exercise""")
        
        self.Scrollbar = tk.Scrollbar(self)
        self.Scrollbar.config(command=self.Text.yview)
        self.Text.config(yscrollcommand=self.Scrollbar.set)

        self.Text.pack(side=tk.LEFT, fill=tk.Y)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


class Plot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.is_blank = True
        white = Image.open("white.jpg")
        self.white = ImageTk.PhotoImage(white)
        self.Canvas = tk.Canvas(self, width=600, height=400)
        self.Canvas.pack(side=tk.LEFT, fill=tk.X)
        self.image_id = self.Canvas.create_image(0,
                                                 0,
                                                 anchor=tk.NW,
                                                 image=self.white)

    def set_to_blank(self):
        self.Canvas.itemconfig(self.image_id, image=self.white)
        self.is_blank = True

    def insert_image(self, figure):
        plt.savefig("chart.jpg", format="jpg")
        chart = Image.open("chart.jpg")
        self.chart = ImageTk.PhotoImage(chart)
        self.Canvas.itemconfig(self.image_id, image=self.chart)
        plt.clf()
        os.remove("chart.jpg")
        self.is_blank = False


class Solution(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.Text = tk.Text(self,
                            bg="lightblue",
                            height=20,
                            width=70)

        self.Scrollbar = tk.Scrollbar(self)
        self.Scrollbar.config(command=self.Text.yview)
        self.Text.config(yscrollcommand=self.Scrollbar.set)

        self.Text.pack(side=tk.LEFT, fill=tk.Y)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    def insert_pre_sol(self, solution):
        if solution:
            self.Text.delete("1.0", tk.END)
            pre_solution = "To reveal the solution press \"Show Solution\" button"
            self.parent.Entry.Button_Show_Solution.config(state=tk.NORMAL)
        else:
            self.Text.delete("1.0", tk.END)
            pre_solution = "No solution given to this task"
            self.parent.Entry.Button_Show_Solution.config(state=tk.DISABLED)
        self.Text.insert(tk.END, pre_solution)

    def insert_solution(self):
        self.Text.delete("1.0", tk.END)
        self.Text.insert(tk.END, self.solution)


class Entry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.Label = tk.Label(self, text="Type your answer here:")
        self.Entry = tk.Entry(self)
        self.answer = None
        self.Text = tk.Text(self, bg="pink", height=8)
        self.Text.insert(tk.END, """After you submit your answer
this text will be replaced
with hint about the answer.
The hits are:
1. "Exact match" - if +/- 0.5% from answer
2. "Close" - if +/- 5% from answer
3. "Way off" - in rest of the cases""")
        self.text_responses = {"match"  : "Exact match",
                               "close"  : "Close",
                               "off"    : "Way off",
                               "unknown": "Unknown input"}

        self.match_eps = 0.005
        self.close_eps = 0.05

        self.Text_Answer = tk.Text(self, bg="green", height=1)
        self.Text_Answer.insert(tk.END, "Press \"Show Answer\" to reveal Answer")
        self.Button_Submit = tk.Button(self, text="Submit", width=10, state=tk.DISABLED, command=self.check_submit)
        self.Button_Show_Answer = tk.Button(self, text="Show Answer", command=self.show_answer, state=tk.DISABLED)
        self.Button_Show_Solution = tk.Button(self, text="Show Solution", state=tk.DISABLED, command=self.parent.Solution.insert_solution)
        self.Button_Next = tk.Button(self, text="Next Exercise", state=tk.DISABLED)
        self.Button_Random = tk.Button(self, text="Random Exercise", state=tk.DISABLED)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Label.grid(row=0, column=1)
        self.Entry.grid(row=0, column=2)
        self.Button_Submit.grid(row=0, column=3)
        self.Text.grid(row=1, rowspan=3, column=0, columnspan=3)
        self.Text_Answer.grid(row=4, column=0, columnspan=3)
        self.Button_Next.grid(row=1, column=3)
        self.Button_Random.grid(row=2, column=3)
        self.Button_Show_Solution.grid(row=3, column=3)
        self.Button_Show_Answer.grid(row=4, column=3)

    def show_answer(self):
        if self.answer is None:
            return
        self.Text_Answer.delete('1.0', tk.END)
        if isinstance(self.answer, float):
            self.Text_Answer.insert(tk.END, "{:.2e}".format(self.answer))
        else:
            self.Text_Answer.insert(tk.END, self.answer)


    def check_submit(self):
        submit = self.Entry.get()
        if submit is "":
            return
        self.Text.delete("1.0", tk.END)
        self.Text.insert(tk.END, self.is_submit_correct(submit, self.answer))

    def is_submit_correct(self, submit, answer):
        if isinstance(answer, str):
            if submit == answer:
                return self.text_responses["match"]
            else:
                return self.text_responses["off"]
        else:
            if "," in submit:
                submit.replace(",", ".")
            try:
                submit = float(submit)
            except ValueError:
                return self.text_responses["unknown"]

            lower_match_range = answer - answer * self.match_eps
            upper_match_range = answer + answer * self.match_eps
            lower_close_range = answer - answer * self.close_eps
            upper_close_range = answer + answer * self.close_eps
            if lower_match_range < submit < upper_match_range:
                return self.text_responses["match"]
            elif lower_close_range < submit < upper_close_range:
                return self.text_responses["close"]
            else:
                return self.text_responses["off"]






class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.Navigation_h = root_h * 0.1
        self.Navigation_w = root_w
        self.Text_h = root_h * 0.45
        self.Text_w = root_w / 2
        self.Plot_h = root_h * 0.6
        self.Plot_w = root_w / 2
        self.Solution_h = root_h * 0.45
        self.Solution_w = root_w / 2
        self.Entry_h = root_h * 0.3
        self.Entry_w = root_w / 2
        self.parent = parent
        self.Navigation = Navigation(self,
                                     bg='grey',
                                     height=self.Navigation_h,
                                     width=self.Navigation_w)
        
        self.Text = Text(self,
                         bg='black',
                         height=self.Text_h,
                         width=self.Text_w)
        
        self.Plot = Plot(self,
                         bg='red',
                         height=self.Plot_h,
                         width=self.Plot_w)
        
        self.Solution = Solution(self,
                                 bg='pink',
                                 height=self.Solution_h,
                                 width=self.Solution_w)
        self.Entry = Entry(self,
                           bg='blue',
                           height=self.Entry_h,
                           width=self.Entry_w)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.Navigation.grid(row=0, column=0, columnspan=2)
        self.Text.grid(row=1, rowspan=3, column=0)
        self.Solution.grid(row=4, rowspan=3, column=0)
        self.Plot.grid(row=1, rowspan=4, column=1)
        self.Entry.grid(row=5, rowspan=2, column=1)


if __name__ == "__main__":
    global root
    root = tk.Tk()
    global root_h
    global root_w
    root_h, root_w = (800, 1350)
    root.geometry('{}x{}'.format(root_w, root_h))
    root.title('Salci')

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
