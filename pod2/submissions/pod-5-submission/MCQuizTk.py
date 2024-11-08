import tkinter as tk
from tkinter import ttk
import json

# Class to define the components of the GUI
class Quiz:
    def __init__(self, master):
        self.master = master
        self.q_no = 0  # Initialize question number
        self.display_title()  # Display the quiz title
        
        # Create a label for displaying the question
        self.question_label = ttk.Label(root, wraplength=600, justify='left')
        self.question_label.grid(row=1, column=0, padx=20, pady=(2, 10), sticky='w')  # Positioning the question
        
        self.opt_selected = tk.IntVar()  # Variable to store selected option
        self.opts = self.radio_buttons()  # Create radio buttons for options
        self.display_options()  # Display the options
        self.buttons()  # Create navigation buttons
        
        self.data_size = len(question)  # Get the total number of questions
        self.correct = 0  # Initialize correct answer count
        self.answers_picked = []  # Initialize list to store picked answers
        
        self.display_question()  # Display the first question

    def display_result(self):
        result_frame = tk.Frame(self.master, bg='#2e2e2e')  # Set background color to darker gray
        result_frame.grid(row=0, column=0, padx=0, pady=0,columnspan=2,rowspan=7, sticky='nsew')  # Position the result frame
        
        score = int(self.correct / self.data_size * 100)  # Calculate score percentage
        result = f"Score: {score}%"  # Format final score
        
        # Display the results
        tk.Label(result_frame, text=result, font=('Helvetica', 16), bg='#2e2e2e', fg='white').grid(row=0, column=0, sticky='w')
        tk.Label(result_frame, text=f"Correct answers: {self.correct}", font=('Helvetica', 14), bg='#2e2e2e', fg='green').grid(row=1, column=0, sticky='w')
        tk.Label(result_frame, text=f"Wrong answers: {self.data_size - self.correct}", font=('Helvetica', 14), bg='#2e2e2e', fg='red').grid(row=2, column=0, sticky='w')
        
        # Display the questions and the answers picked
        for i in range(self.data_size):
            question_text = question[i]
            picked_answer = self.answers_picked[i]
            correct_answer = answer[i]
            tk.Label(result_frame, text=f"{question_text}", font=('Helvetica', 12), fg='yellow', bg='#2e2e2e').grid(row=3+i*3, column=0, sticky='w')  
            tk.Label(result_frame, text=f"Your answer: {picked_answer}", font=('Helvetica', 12), bg='#2e2e2e', fg='white').grid(row=4+i*3, column=0, sticky='w')
            tk.Label(result_frame, text=f"Correct answer: {correct_answer}", font=('Helvetica', 12), bg='#2e2e2e', fg='white').grid(row=5+i*3, column=0, sticky='w')
        
        # Hide the previous frame
        for widget in self.master.winfo_children():
            if widget != result_frame:
                widget.grid_forget()

    def check_ans(self, q_no):
        # Check if the selected option is correct
        return self.opt_selected.get() == answer[q_no]

    def next_btn(self):
        # Move to the next question
        if self.check_ans(self.q_no):  # If answer is correct, increment score
            self.correct += 1
        
        self.answers_picked.append(self.opt_selected.get())  # Store picked answer
        self.q_no += 1  # Move to the next question
        
        if self.q_no == self.data_size:  # If last question is reached
            self.display_result()  # Show results
        else:
            self.display_question()  # Display next question
            self.display_options()  # Display options for next question

        self.opt_selected.set(0)  # Reset selection to default


    def buttons(self):
        # Create a frame for buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=6, column=0, pady=20)  # Adjusted row for button frame

        next_button = ttk.Button(button_frame, text="Next", command=self.next_btn)
        next_button.grid(row=0, column=0, padx=10)  # Position the Next button
        
        quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
        quit_button.grid(row=0, column=1, padx=10)  # Position the Quit button

    def display_options(self):
        # Display options for the current question
        for val, option in enumerate(options[self.q_no]):  # Loop through options
            self.opts[val]['text'] = option  # Set option text

    def display_question(self):
        # Update the question label with the current question
        self.question_label.config(text=question[self.q_no])

    def display_title(self):
        # Create and position the title label
        title = ttk.Label(root, text="GUI QUIZ", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, pady=(5, 10), sticky='w')  # Position the title

    def radio_buttons(self):
        # Create radio buttons for answer options
        q_list = []  # List to store radio buttons
        for i in range(4):  # Create 4 radio buttons
            radio_btn = ttk.Radiobutton(root, variable=self.opt_selected, value=i+1)
            radio_btn.grid(row=i+2, column=0, sticky='w', padx=20, pady=2)
            q_list.append(radio_btn)  # Add button to the list
        
        return q_list  # Return the list of radio buttons

# Create a GUI Window
root = tk.Tk()  # Initialize the main window
root.geometry("800x450")  # Set window size
root.title("GUI Quiz")  # Set window title

# Get the data from the JSON file
with open('MCQuizTkData.json') as f:
    data = json.load(f)  # Load quiz data from JSON file

# Set the question, options, and answer
question = data['question']  # Extract questions
options = data['options']  # Extract answer options
answer = data['answer']  # Extract correct answers

# Create an object of the Quiz Class
quiz = Quiz(root)  # Instantiate the quiz

# Configure grid weights for proper expansion
root.grid_columnconfigure(0, weight=1)  # Allow the first column to expand
for i in range(7):  # Adjust for the number of rows (including the button frame)
    root.grid_rowconfigure(i, weight=1)  # Allow all rows to expand

# Start the GUI
root.mainloop()  # Run the application