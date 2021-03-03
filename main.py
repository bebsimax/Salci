import sys
import os
import tkinter as tk
import random
import matplotlib.pyplot as plt
from importlib import import_module
from PIL import ImageTk, Image
from common import ExerciseList, PackedExercise

main_folder = os.path.dirname(os.path.abspath(__file__))
chapters = os.path.join(main_folder, "chapters")
if chapters not in sys.path:
    sys.path.append(chapters)
common = os.path.join(main_folder, "common")
if common not in sys.path:
    sys.path.append(common)


class Navigation(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.Chapter_Listbox = tk.Listbox(self, bg="orange", selectmode="single", height=5, width=20)
        self.chapters = os.listdir(chapters)
        for index, chapter in enumerate(self.chapters, start=1):
            self.Chapter_Listbox.insert(index, chapter)
        
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
        module_name = name + "_ex"
        ch_path = os.path.join(chapters, name)
        if ch_path not in sys.path:
            sys.path.append(ch_path)
        ex_module = import_module(module_name)
        self.exercise_decorator = ex_module.exercise_decorator
        for number in range(len(ex_module.exercise_decorator)):
            self.Ex_Listbox.insert(number+1, str(number+1))
        self.Ex_Button.config(state=tk.NORMAL)

    def load_ex(self, clear=False):

        packed_exercise = self.get_function()
        if packed_exercise is None:
            return
        # unpack the contents
        self.parent.Entry.answer = packed_exercise.answer
        self.parent.Solution.solution = packed_exercise.solution
        # replace the text boxes
        self.parent.Text.replace_text(packed_exercise.text)
        self.parent.Solution.insert_pre_sol(self.parent.Solution.solution)
        # set the text and entry to initial state
        if clear is True:
            self.parent.Entry.set_initial()
        # check for return matplotlib figure, paint the canvas
        if packed_exercise.image:
            self.parent.Plot.insert_image(packed_exercise.image)
        else:
            if not self.parent.Plot.is_blank:
                self.parent.Plot.set_to_blank()
        # enable the buttons
        self.parent.Entry.Button_Submit.config(state=tk.NORMAL)
        self.parent.Entry.Button_Show_Answer.config(state=tk.NORMAL)
        self.parent.Entry.Button_Next.config(state=tk.NORMAL)
        self.parent.Entry.Button_Prev.config(state=tk.NORMAL)

    def get_function(self):
        try:
            self.number = self.Ex_Listbox.get(self.Ex_Listbox.curselection())
        except:
            return
        self.number = int(self.number)-1
        ex = self.exercise_decorator[self.number]
        return ex()

    def load_next(self, event=None):
        self.Ex_Listbox.selection_clear(0, tk.END)
        try:
            self.Ex_Listbox.selection_set(self.number+1)
            self.load_ex(True)
        except:
            self.parent.Entry.Text.delete("1.0", tk.END)
            self.parent.Entry.Text.insert(tk.END, "Out of exercises")
            return

    def load_previous(self, event=None):
        self.Ex_Listbox.selection_clear(0, tk.END)
        #try:
        self.Ex_Listbox.selection_set(int(self.number)-1)
        self.load_ex(clear=True)
        #except:
           # self.parent.Entry.Text.delete("1.0", tk.END)
          #  self.parent.Entry.Text.insert(tk.END, "Out of exercises")
           # return


class Text(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.Text = tk.Text(self,
                            bg='pink',
                            height=20, width=70,
                            font=("Helvetica", 11))
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

    def replace_text(self, text):
        self.Text.delete("1.0", tk.END)
        self.Text.insert(tk.END, text)


class Plot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.is_blank = True
        white = Image.open("white.jpg")
        self.white = ImageTk.PhotoImage(white)
        self.Canvas = tk.Canvas(self, width=600, height=400)
        self.Canvas.pack(side=tk.LEFT, fill=tk.X)
        # TODO generate white with matplotlib
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
                            width=70,
                            font=("Helvetica", 11))

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
        self.answer_initial_text = "Press \"Show Answer\" to reveal Answer"
        self.Text_initial_text = """After you submit your answer
this text will be replaced
with hint about the answer.
The hits are:
1. "Exact match" - if +/- 0.5% from answer
2. "Close" - if +/- 5% from answer
3. "Way off" - in rest of the cases"""
        self.Text = tk.Text(self, bg="pink", height=8, font=("Helvetica", 10))
        self.Text.tag_configure("center", justify="center")
        self.Text.insert("1.0", self.Text_initial_text, "center")
        self.text_responses = {"match"  : "Exact match",
                               "close"  : "Close",
                               "off"    : "Way off",
                               "unknown": "Unknown input"}
        # ranges for match and close hint
        # 0.5% and 5%
        self.match_eps = 0.005
        self.close_eps = 0.05

        self.Text_Answer = tk.Text(self, bg="green", height=1, font=("Helvetica", 11), padx=-50)
        self.Text_Answer.tag_configure("center", justify="center")
        self.Text_Answer.insert("1.0", self.answer_initial_text, "center")
        self.Button_Submit = tk.Button(self, text="Submit (\u23ce)", width=10, state=tk.DISABLED, command=self.check_submit)
        self.Button_Show_Answer = tk.Button(self, text="Show Answer", command=self.show_answer, state=tk.DISABLED)
        self.Button_Show_Solution = tk.Button(self, text="Show Solution", state=tk.DISABLED, command=self.parent.Solution.insert_solution)
        self.Button_Prev = tk.Button(self, text="Prev Exercise (<-)", state=tk.DISABLED, command=self.parent.Navigation.load_previous)
        self.Button_Next = tk.Button(self, text="Next Exercise (->)", state=tk.DISABLED, command=self.parent.Navigation.load_next)
        self.Button_Random = tk.Button(self, text="Random Exercise", state=tk.DISABLED)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Label.grid(row=0, column=1)
        self.Entry.grid(row=0, column=2)
        self.Button_Submit.grid(row=0, column=3)
        self.Text.grid(row=1, rowspan=3, column=0, columnspan=3)
        self.Text_Answer.grid(row=4, rowspan=2, column=0, columnspan=3)
        self.Button_Next.grid(row=1, column=3)
        self.Button_Prev.grid(row=2,column=3)
        self.Button_Random.grid(row=3, column=3)
        self.Button_Show_Solution.grid(row=4, column=3)
        self.Button_Show_Answer.grid(row=5, column=3)

    def show_answer(self):
        if self.answer is None:
            return
        self.Text_Answer.delete('1.0', tk.END)
        if isinstance(self.answer, float):
            self.Text_Answer.insert("1.0", "{:.2e}".format(self.answer), "center")
        else:
            self.Text_Answer.insert("1.0", self.answer, "center")

    def check_submit(self, event=None):
        submit = self.Entry.get()
        if submit is "":
            return
        self.Text.delete("1.0", tk.END)
        self.Text.insert("1.0", self.is_submit_correct(submit, self.answer), "center")

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
            if answer < 0:
                temp = lower_match_range
                lower_match_range = upper_match_range
                upper_match_range = temp
                temp = lower_close_range
                lower_close_range = upper_close_range
                upper_close_range = temp
            if lower_match_range < submit < upper_match_range:
                return self.text_responses["match"]
            elif lower_close_range < submit < upper_close_range:
                return self.text_responses["close"]
            else:
                return self.text_responses["off"]

    def set_initial(self):
        self.Text.delete("1.0", tk.END)
        self.Text.insert("1.0", self.Text_initial_text, "center")
        self.Text_Answer.delete("1.0", tk.END)
        self.Text_Answer.insert("1.0", self.answer_initial_text, "center")
        self.Entry.delete(0, tk.END)


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
        parent.bind("<Right>", self.Navigation.load_next)
        parent.bind("<Left>", self.Navigation.load_previous)
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
        parent.bind("<Return>", self.Entry.check_submit)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # TODO: replace text and plot
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
