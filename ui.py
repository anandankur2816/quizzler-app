import time
from tkinter import *
from quiz_brain import QuizBrain
from functools import partial
THEME_COLOR = "#375362"


class GUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.title("Quizzler")
        self.sc = 0
        self.score = Label(text=f"Score: {self.sc}", highlightthickness=0, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question will appear here be patient.",
            fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.l_image = PhotoImage(file="images/true.png")
        self.r_image = PhotoImage(file="images/false.png")
        self.l_button = Button(image=self.l_image,  highlightthickness=0, command=partial(self.check_ans, "true"))
        self.l_button.grid(column=1, row=2)
        self.r_button = Button(image=self.r_image, command=partial(self.check_ans, "false"), highlightthickness=0)
        self.r_button.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the "
                                        f"end of the quiz.\n Final score:{self.sc}")
            self.l_button.config(state="disabled")
            self.r_button.config(state="disabled")

    def check_ans(self, value: str):
        if self.quiz.check_answer(value):
            self.canvas.config(bg="green")
            self.sc += 1
            self.score["text"] = f"Score:{self.sc}"
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
