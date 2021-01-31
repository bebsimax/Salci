

import sys
import os
import tkinter as tk
import random

from importlib import import_module
from PIL import Image, ImageTk

main_folder = os.path.dirname(os.path.abspath(__file__))
chapters = os.path.join(main_folder, 'chapters')
if chapters not in sys.path:
    sys.path.append(chapters)
common = os.path.join(main_folder, 'common')
if common not in sys.path:
    sys.path.append(common)


class Navigation(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        self.Chapter_Listbox= tk.Listbox(self, bg='orange',
                                         selectmode='single',
                                         height=5, width=20)
        self.chapters = os.listdir(chapters)
        for index, chapter in enumerate(self.chapters, start=1):
            self.Chapter_Listbox.insert(index, str(index)+'.'+chapter)
        
        self.Chapter_Scrollbar= tk.Scrollbar(self)
        self.Chapter_Listbox.config(yscrollcommand = self.Chapter_Scrollbar.set)
        self.Chapter_Scrollbar.config(command = self.Chapter_Listbox.yview)
        
        
        self.Ex_Listbox= tk.Listbox(self, bg='green',
                                    selectmode='single',
                                    height=5, width=20)
        
        self.Ex_Scrollbar= tk.Scrollbar(self)
        self.Ex_Listbox.config(yscrollcommand = self.Ex_Scrollbar.set)
        self.Ex_Scrollbar.config(command = self.Ex_Listbox.yview)
        
        self.Ch_Button = tk.Button(self,
                                   bg='purple',
                                   text='Load Chapter',
                                   command = self.load_ch)
        
        
        
        self.Ex_Button = tk.Button(self, bg='light blue',
                                   text='Load Exercise',
                                   command = self.load_ex)
        

        
        
        
        
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.Chapter_Listbox.grid(row=0, column=0)
        self.Chapter_Scrollbar.grid(row=0, column=1)
        self.Ch_Button.grid(row=0, column=2)

        self.Ex_Listbox.grid(row=0, column=6)
        self.Ex_Scrollbar.grid(row=0, column=7)
        self.Ex_Button.grid(row=0, column=8)

    def load_ch(self):
        self.Ex_Listbox.delete(0, tk.END)
        try:
            name = self.Chapter_Listbox.get(self.Chapter_Listbox.curselection())
        except:
            return
        name = name.split('.')
        ch_number = name[0]
        name = name[1]
        module_name = name+'_ex'
        ch_path = os.path.join(chapters, name)
        if ch_path not in sys.path:
            sys.path.append(ch_path)
        ex_module = import_module(module_name)
        self.exercise_decorator = ex_module.exercise_decorator
        for number in range(len(ex_module.exercise_decorator)):
            self.Ex_Listbox.insert(number+1, str(ch_number)+'.'+str(number+1))

    def load_ex(self):
        try:
            number = self.Ex_Listbox.get(self.Ex_Listbox.curselection())
        except:
            return
        number = number.split('.')[1]
        ex = self.exercise_decorator[int(number)-1]
        
        text, solution, answer, image = ex()
        
        self.parent.Entry.answer= answer
        self.parent.Solution.solution = solution
        
        self.clear_text()
        self.insert_text(text)
        
        
        self.clear_sol()
        self.insert_pre_sol(solution)
        
        self.clear_image()
        self.insert_image(image)
        
        
    def clear_text(self):
        self.parent.Text.Text.delete('1.0', tk.END)
        
        
    def insert_text(self, text):
        self.parent.Text.Text.insert(tk.END, text)
        
        
    def clear_sol(self):
        self.parent.Solution.Text.delete('1.0', tk.END)

    
    def insert_pre_sol(self, solution):
        if solution:
            pre_sol = 'To reveal the solution press \'Show Solution\' button'
            self.parent.Solution.Text.insert(tk.END, pre_sol)
        else:
            no_sol = 'No solution given to this task'
            self.parent.Solution.Text.insert(tk.END, no_sol)

    def clear_image(self):
        pass

    def insert_image(self, image):
        pass
    

    




class Text(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        self.Text = tk.Text(self,
                            bg='pink',
                            height=20, width=70)
        
        self.Scrollbar= tk.Scrollbar(self)
        self.Scrollbar.config(command=self.Text.yview)
        self.Text.config(yscrollcommand=self.Scrollbar.set)
        
        
        self.Text.pack(side=tk.LEFT, fill=tk.Y)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



class Plot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.Canvas = tk.Canvas(self, width=400, height=400)
        self.gray = ImageTk.PhotoImage(Image.open('gray.jpg'))
        self.Canvas.create_image(300,200, image=self.gray)
        
        
        
        
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.Canvas.grid(row=0, column=0)




class Solution(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        self.Text = tk.Text(self,
                            bg='lightblue',
                            height=20,
                            width=70)


        self.Scrollbar= tk.Scrollbar(self)
        self.Scrollbar.config(command=self.Text.yview)
        self.Text.config(yscrollcommand=self.Scrollbar.set)
        
        
        self.Text.pack(side=tk.LEFT, fill=tk.Y)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



class Entry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent





class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.Navigation_h = root_h*0.1
        self.Navigation_w = root_w
        self.Text_h = root_h*0.45
        self.Text_w = root_w/2
        self.Plot_h = root_h*0.6
        self.Plot_w = root_w/2
        self.Solution_h = root_h*0.45
        self.Solution_w = root_w/2
        self.Entry_h = root_h*0.3
        self.Entry_w = root_w/2
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
                           height= self.Entry_h,
                           width= self.Entry_w)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.Navigation.grid(row=0, column=0, columnspan=2)
        self.Text.grid(row=1, rowspan=3, column=0)
        self.Solution.grid(row=4, rowspan=3, column=0)
        self.Plot.grid(row=1, rowspan=4, column=1)
        self.Entry.grid(row=5, rowspan=2, column=1)



#main
if __name__ == "__main__":
    global root
    root = tk.Tk()
    global root_h
    global root_w
    root_h, root_w = (800, 1200)
    root.geometry('{}x{}'.format(root_w, root_h))
    root.title('Salci')

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
