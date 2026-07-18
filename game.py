import random
from tkinter import *

from ui import QuizUI
from questions import questions, LEVELS
from constants import *


class QuizGame:

    def __init__(self):

        # ---------------- UI ---------------- #
        self.ui = QuizUI()

        # ---------------- Game Variables ---------------- #

        self.current_question = 0
        self.money = 0

        self.correct_option = 0
        self.current_options = []

        self.time_left = QUESTION_TIME
        self.timer_running = False

        # Pick 16 random questions
        self.quiz_questions = random.sample(
            questions,
            TOTAL_QUESTIONS
        )

        # Connect Buttons
        self.ui.start_button.config(
            command=self.start_game
        )

        self.ui.restart_button.config(
            command=self.restart_game
        )

        self.ui.optionA.config(
            command=lambda: self.check_answer(1)
        )

        self.ui.optionB.config(
            command=lambda: self.check_answer(2)
        )

        self.ui.optionC.config(
            command=lambda: self.check_answer(3)
        )

        self.ui.optionD.config(
            command=lambda: self.check_answer(4)
        )

    # ===================================================
    # START GAME
    # ===================================================

    def start_game(self):

        self.current_question = 0
        self.money = 0

        self.quiz_questions = random.sample(
            questions,
            TOTAL_QUESTIONS
        )

        self.ui.welcome_frame.pack_forget()

        self.ui.quiz_frame.pack(
            fill="both",
            expand=True
        )

        self.load_question()

    # ===================================================
    # LOAD QUESTION
    # ===================================================

    def load_question(self):

        question = self.quiz_questions[self.current_question]

        self.ui.question_label.config(
            text=question[0]
        )

        # Shuffle options

        self.current_options = [

            (question[1], 1),
            (question[2], 2),
            (question[3], 3),
            (question[4], 4)

        ]

        random.shuffle(self.current_options)

        # Find correct option

        for i, (_, original_pos) in enumerate(
            self.current_options
        ):

            if original_pos == question[5]:
                self.correct_option = i + 1

        buttons = [

            self.ui.optionA,
            self.ui.optionB,
            self.ui.optionC,
            self.ui.optionD

        ]

        letters = ["A", "B", "C", "D"]

        # Reset buttons

        for i in range(4):

            buttons[i].config(

                text=f"{letters[i]}. {self.current_options[i][0]}",
                bg=BUTTON_COLOR,
                fg="white",
                state=NORMAL

            )

        # ---------------- Header ---------------- #

        self.ui.question_count.config(

            text=f"Question {self.current_question+1}/{TOTAL_QUESTIONS}"

        )

        self.ui.prize_label.config(

            text=f"Prize : ₹{LEVELS[self.current_question]}"

        )

        # ---------------- Prize Ladder ---------------- #

        for lbl in self.ui.ladder_labels:

            lbl.config(

                bg=LADDER_BG,
                fg="white"

            )

        index = len(LEVELS) - 1 - self.current_question

        self.ui.ladder_labels[index].config(

            bg=LADDER_ACTIVE,
            fg=LADDER_ACTIVE_TEXT

        )

        # ---------------- Timer ---------------- #

        self.time_left = QUESTION_TIME
        self.timer_running = True

        self.ui.timer_label.config(

            text=f"Time : {QUESTION_TIME}"

        )

        self.countdown()

    # ===================================================
    # CHECK ANSWER
    # ===================================================

    def check_answer(self, choice):

        if not self.timer_running:
            return

        self.timer_running = False

        buttons = [
            self.ui.optionA,
            self.ui.optionB,
            self.ui.optionC,
            self.ui.optionD
        ]

        # Disable all buttons
        for btn in buttons:
            btn.config(state=DISABLED)

        # ---------------- Correct Answer ---------------- #

        if choice == self.correct_option:

            buttons[self.correct_option - 1].config(
                bg=CORRECT_COLOR
            )

            self.money = LEVELS[self.current_question]

            self.current_question += 1

            # Quiz Finished
            if self.current_question >= TOTAL_QUESTIONS:

                self.ui.root.after(
                    800,
                    lambda: self.show_result(
                        WIN_MESSAGE,
                        self.money
                    )
                )

                return

            # Load next question
            self.ui.root.after(
                800,
                self.load_question
            )

        # ---------------- Wrong Answer ---------------- #

        else:

            buttons[choice - 1].config(
                bg=WRONG_COLOR
            )

            buttons[self.correct_option - 1].config(
                bg=CORRECT_COLOR
            )

            self.ui.root.after(
                1200,
                lambda: self.show_result(
                    GAME_OVER,
                    self.money
                )
            )

    # ===================================================
    # COUNTDOWN TIMER
    # ===================================================

    def countdown(self):

        if not self.timer_running:
            return

        self.ui.timer_label.config(
            text=f"Time : {self.time_left}"
        )

        if self.time_left > 0:

            self.time_left -= 1

            self.ui.root.after(
                1000,
                self.countdown
            )

        else:

            self.timer_running = False

            # Disable buttons

            self.ui.optionA.config(state=DISABLED)
            self.ui.optionB.config(state=DISABLED)
            self.ui.optionC.config(state=DISABLED)
            self.ui.optionD.config(state=DISABLED)

            self.show_result(
                TIME_OVER,
                self.money
            )
    # ===================================================
    # SHOW RESULT
     # ===================================================

    def show_result(self, message, amount):

        self.ui.quiz_frame.pack_forget()

        self.result_frame = Frame(
            self.ui.root,
            bg=BG_COLOR
        )

        self.result_frame.pack(
            fill="both",
            expand=True
        )

        Label(
            self.result_frame,
            text=message,
            font=RESULT_FONT,
            bg=BG_COLOR,
            fg="white"
        ).pack(pady=40)

        Label(
            self.result_frame,
            text=f"You won ₹{amount}",
            font=("Arial", 22, "bold"),
            bg=BG_COLOR,
            fg="gold"
        ).pack(pady=20)

        Button(
            self.result_frame,
            text="🔄 Play Again",
            font=("Arial", 16, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.restart_game
        ).pack(pady=20)

        Button(
            self.result_frame,
            text="❌ Exit",
            font=("Arial", 16, "bold"),
            bg="red",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.ui.root.destroy
        ).pack()

    # ===================================================
    # RESTART GAME
    # ===================================================

    def restart_game(self):

        # Remove result screen if present
        if hasattr(self, "result_frame"):
            self.result_frame.destroy()

        self.current_question = 0
        self.money = 0

        self.quiz_questions = random.sample(
            questions,
            TOTAL_QUESTIONS
        )

        self.time_left = QUESTION_TIME
        self.timer_running = False

        self.ui.quiz_frame.pack(
            fill="both",
            expand=True
        )

        self.load_question()

    # ===================================================
    # RUN APPLICATION
    # ===================================================

    def run(self):
        self.ui.run()