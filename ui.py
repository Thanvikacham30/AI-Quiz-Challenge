from tkinter import *
from constants import *

class QuizUI:

    def __init__(self):

        # ================= Window ================= #

        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        # ================= Welcome Screen ================= #

        self.welcome_frame = Frame(self.root, bg=BG_COLOR)
        self.welcome_frame.pack(fill="both", expand=True)

        Label(
            self.welcome_frame,
            text="🤖 AI QUIZ CHALLENGE",
            font=TITLE_FONT,
            bg=BG_COLOR,
            fg="white"
        ).pack(pady=50)

        Label(
            self.welcome_frame,
            text=WELCOME_MESSAGE,
            font=SUBTITLE_FONT,
            bg=BG_COLOR,
            fg="cyan"
        ).pack()

        Label(
            self.welcome_frame,
            text="🏆 Win up to ₹1 Crore",
            font=("Arial",20,"bold"),
            bg=BG_COLOR,
            fg="gold"
        ).pack(pady=20)

        self.start_button = Button(
            self.welcome_frame,
            text=START,
            font=("Arial",18,"bold"),
            bg=BUTTON_COLOR,
            fg="white",
            padx=25,
            pady=10,
            cursor="hand2"
        )

        self.start_button.pack(pady=30)

        # ================= Quiz Screen ================= #

        self.quiz_frame = Frame(
            self.root,
            bg=BG_COLOR
        )

        # Header

        header = Frame(
            self.quiz_frame,
            bg=HEADER_COLOR,
            height=60
        )

        header.pack(fill="x")

        self.question_count = Label(
            header,
            text="Question 1/16",
            font=HEADER_FONT,
            bg=HEADER_COLOR,
            fg="cyan"
        )

        self.question_count.pack(
            side=LEFT,
            padx=20
        )

        self.prize_label = Label(
            header,
            text="Prize : ₹100",
            font=HEADER_FONT,
            bg=HEADER_COLOR,
            fg="gold"
        )

        self.prize_label.pack(
            side=LEFT,
            padx=180
        )

        self.timer_label = Label(
            header,
            text="Time : 20",
            font=HEADER_FONT,
            bg=HEADER_COLOR,
            fg="red"
        )

        self.timer_label.pack(
            side=RIGHT,
            padx=20
        )

        # ================= Question ================= #

        question_frame = Frame(
            self.quiz_frame,
            bg=HEADER_COLOR
        )

        question_frame.pack(
            fill="x",
            padx=20,
            pady=30
        )

        self.question_label = Label(
            question_frame,
            text="Question",
            font=QUESTION_FONT,
            bg=HEADER_COLOR,
            fg="white",
            wraplength=700,
            justify=LEFT,
            padx=20,
            pady=20
        )

        self.question_label.pack(
            anchor="w"
        )

        # ================= Options ================= #

        option_frame = Frame(
            self.quiz_frame,
            bg=BG_COLOR
        )

        option_frame.pack()

        self.optionA = Button(
            option_frame,
            width=BUTTON_WIDTH,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg="white",
            pady=BUTTON_PADY
        )

        self.optionB = Button(
            option_frame,
            width=BUTTON_WIDTH,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg="white",
            pady=BUTTON_PADY
        )

        self.optionC = Button(
            option_frame,
            width=BUTTON_WIDTH,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg="white",
            pady=BUTTON_PADY
        )

        self.optionD = Button(
            option_frame,
            width=BUTTON_WIDTH,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg="white",
            pady=BUTTON_PADY
        )

        self.optionA.grid(row=0,column=0,pady=10)
        self.optionB.grid(row=1,column=0,pady=10)
        self.optionC.grid(row=2,column=0,pady=10)
        self.optionD.grid(row=3,column=0,pady=10)

        # ================= Prize Ladder ================= #

        ladder = Frame(
            self.quiz_frame,
            bg=LADDER_BG
        )

        ladder.place(
            x=760,
            y=140
        )

        Label(
            ladder,
            text=PRIZE_LADDER,
            font=LADDER_TITLE_FONT,
            bg=LADDER_BG,
            fg="white"
        ).pack()

        self.ladder_labels = []

        for amount in reversed(LEVELS):

            lbl = Label(
                ladder,
                text=f"₹{amount}",
                font=LADDER_FONT,
                bg=LADDER_BG,
                fg="white",
                width=15
            )

            lbl.pack()

            self.ladder_labels.append(lbl)

        # ================= Restart Button ================= #

        self.restart_button = Button(
            self.root,
            text=RESTART,
            font=("Arial",14,"bold"),
            bg="green",
            fg="white",
            cursor="hand2"
        )

        self.restart_button.pack(
            pady=10
        )

    # ================= Run ================= #

    def run(self):
        self.root.mainloop()