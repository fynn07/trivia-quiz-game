import tkinter
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = tkinter.Label()
        self.score.config(text=f"Score = 0", fg="white", bg=THEME_COLOR, font=('bold'))
        self.score.grid(padx=20, pady=20, row=0, column=1)

        self.canvas = tkinter.Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,text="testing text", fill=THEME_COLOR, font=('arial', 20, 'italic'), width=285)
        self.canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)

        CHECK_IMAGE = tkinter.PhotoImage(file='quiz_app/images/true.png')
        FALSE_IMAGE = tkinter.PhotoImage(file='quiz_app/images/false.png')

        self.true_button = tkinter.Button()
        self.true_button.config(image=CHECK_IMAGE, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(padx=20, pady=20, row=2, column=0)

        self.false_button = tkinter.Button()
        self.false_button.config(image=FALSE_IMAGE, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(padx=20, pady=20, row=2, column=1)
    
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score = {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, tex="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
            
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
        
        