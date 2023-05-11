from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:
    def __init__(self):
        self.window = window
        self.question_num = 0

        title = Label(self.window, text="Harry Potter Quiz", width=50, bg="red", fg="white",
                      font=("Times new roman", 20, "bold", ))
        info_title = Label(self.window, text="If you don't know the answer click next, however the question will be counted as wrong!",
                           font=("Times new roman", 14, "bold", ), anchor='center', background='#F2F0E8')
        info_title.place(x=50, y=330)
        title.place(x=0, y=2)
        self.display_question()

        self.option_selected = IntVar()
        self.options = self.radio_buttons()
        self.display_options()

        next_button = Button(self.window, text="Next", command=self.next_button, width=10, bg="blue", fg="white",
                             font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)
        quit_button = Button(self.window, text="Quit", command=self.window.destroy, width=5, bg="green", fg="white",
                             font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)

        self.data_size = len(question)
        self.correct = 0

    def display_question(self):
        """Shows the current question on the screen"""
        question_num = Label(self.window, text=question[self.question_num], width=60,
                             font=('Times new roman', 16, 'bold'), anchor='w', background='#F2F0E8')
        question_num.place(x=70, y=100)

    def display_options(self):
        """This method is used to ensure all the radio buttons are deselected. It then displays the options
        for the current question."""
        num = 0
        self.option_selected.set(0)
        for option in options[self.question_num]:
            self.options[num]['text'] = option
            num += 1

    def radio_buttons(self):
        """This method shows the radio buttons to select the question on the screen at the specified position.
        It also returns a list of radio button which are later used to add the options to them."""
        question_list = []
        y_pos = 150

        while len(question_list) < 4:
            radio_btn = Radiobutton(self.window, text=" ", variable=self.option_selected,
                                    value=len(question_list) + 1, font=("Times new roman", 14), background='#F2F0E8')
            question_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return question_list

    def check_ans(self, q_no):
        """Checks if the selected answer is correct."""
        if self.option_selected.get() == answer[q_no]:
            return True

    def next_button(self):
        """This method is used to check the answer of the current question by calling the
        check_ans and question_num. If the question is correct it increases the count by 1
        snd then increases the count by 1. If it's the last question then it calls the display_result function."""

        if self.check_ans(self.question_num):
            self.correct += 1
        self.question_num += 1

        if self.question_num == self.data_size:
            self.display_result()
            self.window.destroy()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

# Creates GUI Window


window = Tk()
window['bg'] ='#F2F0E8'
window.geometry("800x450")
window.title("Harry Potter Quiz")
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])
quiz = Quiz()
window.mainloop()
