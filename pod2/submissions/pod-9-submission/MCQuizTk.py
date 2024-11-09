
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.question_label = ttk.Label(root, wraplength=600, justify='left')
        self.question_label.grid(row=1, column=0, padx=20, pady=(2, 10), sticky='w')
        self.opt_selected = tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0
        self.display_question()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        return self.opt_selected.get() == answer[q_no]

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
            mb.showinfo("Correct!", "Your answer is correct!")
        else:
            correct_answer = options[self.q_no][answer[self.q_no] - 1]
            mb.showinfo("Incorrect", f"Your answer is incorrect.\nThe correct answer is: {correct_answer}")
        
        self.q_no += 1
        
        if self.q_no == self.data_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()

        self.opt_selected.set(0)

    def buttons(self):
        button_frame = tk.Frame(root)
        button_frame.grid(row=6, column=0, pady=20)
        next_button = ttk.Button(button_frame, text="Next", command=self.next_btn)
        next_button.grid(row=0, column=0, padx=10)
        quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
        quit_button.grid(row=0, column=1, padx=10)

    def display_options(self):
        for val, option in enumerate(options[self.q_no]):
            self.opts[val]['text'] = option

    def display_question(self):
        self.question_label.config(text=question[self.q_no])

    def display_title(self):
        title = ttk.Label(root, text="GUI QUIZ", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, pady=(5, 10), sticky='w')

    def radio_buttons(self):
        q_list = []
        for i in range(4):
            radio_btn = ttk.Radiobutton(root, variable=self.opt_selected, value=i+1)
            radio_btn.grid(row=i+2, column=0, sticky='w', padx=20, pady=2)
            q_list.append(radio_btn)
        return q_list

root = tk.Tk()
root.geometry("800x450")
root.title("GUI Quiz")

with open('MCQuizTkData.json') as f:
    data = json.load(f)

question = data['question']
options = data['options']
answer = data['answer']

quiz = Quiz()

root.grid_columnconfigure(0, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
