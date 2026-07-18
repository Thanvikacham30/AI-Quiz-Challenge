"""
constants.py
-------------
Stores all UI constants such as colors, fonts,
window settings, timer values, and prize ladder.
"""

# =========================
# WINDOW SETTINGS
# =========================

WINDOW_TITLE = "AI Quiz Challenge"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650
WINDOW_SIZE = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"

# =========================
# COLORS
# =========================

BG_COLOR = "#0F172A"
HEADER_COLOR = "#1E293B"
BUTTON_COLOR = "#2563EB"

BUTTON_HOVER = "#1D4ED8"

CORRECT_COLOR = "#16A34A"
WRONG_COLOR = "#DC2626"

TEXT_COLOR = "white"
QUESTION_COLOR = "white"

TITLE_COLOR = "cyan"
PRIZE_COLOR = "gold"
TIMER_COLOR = "red"

LADDER_BG = "#1E293B"
LADDER_ACTIVE = "gold"
LADDER_ACTIVE_TEXT = "black"

WELCOME_TITLE = "white"
WELCOME_SUBTITLE = "cyan"

# =========================
# FONTS
# =========================

TITLE_FONT = ("Poppins", 32, "bold")

SUBTITLE_FONT = ("Arial", 18)

QUESTION_FONT = ("Arial", 20, "bold")

BUTTON_FONT = ("Arial", 15)

HEADER_FONT = ("Arial", 16, "bold")

LADDER_FONT = ("Arial", 12)

LADDER_TITLE_FONT = ("Arial", 15, "bold")

RESULT_FONT = ("Arial", 30, "bold")

SMALL_FONT = ("Arial", 10)

# =========================
# BUTTON SETTINGS
# =========================

BUTTON_WIDTH = 40
BUTTON_PADY = 10

BUTTON_RELIEF = "flat"

# =========================
# QUIZ SETTINGS
# =========================

TOTAL_QUESTIONS = 16

QUESTION_TIME = 20

# =========================
# PRIZE LADDER
# =========================

LEVELS = [
    "100",
    "200",
    "500",
    "1,000",
    "2,000",
    "5,000",
    "10,000",
    "20,000",
    "40,000",
    "1 Lakh",
    "2.5 Lakh",
    "5 Lakh",
    "10 Lakh",
    "25 Lakh",
    "50 Lakh",
    "1 Crore"
]

# =========================
# SAFE LEVELS
# =========================

SAFE_LEVELS = {
    4: "2,000",
    9: "1 Lakh",
    14: "50 Lakh"
}

# =========================
# MESSAGES
# =========================

WELCOME_MESSAGE = "Test Your Artificial Intelligence Knowledge"

WIN_MESSAGE = "🎉 Congratulations!"

GAME_OVER = "❌ Game Over"

TIME_OVER = "⏰ Time Over!"

PLAY_AGAIN = "Play Again"

EXIT = "Exit"

START = "START QUIZ"

RESTART = "Restart"

PRIZE_LADDER = "Prize Ladder"