import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import json

# Class to define the components of the GUI
class Quiz:
    def __init__(self):
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
        
        self.display_question()  # Display the first question

    def display_result(self):
        # Calculate results and show in a message box
        wrong_count = self.data_size - self.correct  # Count wrong answers
        correct = f"Correct: {self.correct}"  # Format correct answers
        wrong = f"Wrong: {wrong_count}"  # Format wrong answers
        score = int(self.correct / self.data_size * 100)  # Calculate score percentage
        result = f"Score: {score}%"  # Format final score
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")  # Display results

    def check_ans(self, q_no):
        # Check if the selected option is correct
        return self.opt_selected.get() == answer[q_no]

    def next_btn(self):
        # Move to the next question
        if self.check_ans(self.q_no):  # If answer is correct, increment score
            self.correct += 1
        
        self.q_no += 1  # Move to the next question
        
        if self.q_no == self.data_size:  # If last question is reached
            self.display_result()  # Show results
            root.destroy()  # Close the application
        else:
            self.display_question()  # Display next question
            self.display_options()  # Display options for next question

        self.opt_selected.set(0)  # Reset selection to default


    def buttons(self):
        # Create a frame for buttons
        button_frame = tk.Frame(root, background="purple")
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
        self.question_label.config(text=question[self.q_no], background="green")

    def display_title(self):
        # Create and position the title label
        title = ttk.Label(root, text="IDE QUIZ", font=("Arial", 20, "bold"), background="green")
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
root.title("IDE Quiz")  # Set window title
root.configure(background='orange') # Set background color 

# Get the data from the JSON file
with open('MCQuizTkData.json') as f:
    data = json.load(f)  # Load quiz data from JSON file

# Set the question, options, and answer
question = data['question']  # Extract questions
options = data['options']  # Extract answer options
answer = data['answer']  # Extract correct answers

# Create an object of the Quiz Class
quiz = Quiz()  # Instantiate the quiz

# Configure grid weights for proper expansion
root.grid_columnconfigure(0, weight=1)  # Allow the first column to expand
for i in range(7):  # Adjust for the number of rows (including the button frame)
    root.grid_rowconfigure(i, weight=1)  # Allow all rows to expand

# Start the GUI
root.mainloop()  # Run the application