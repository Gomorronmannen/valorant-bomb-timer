import tkinter as tkr
from python_imagesearch.imagesearch import imagesearch
from ctypes import windll

root = tkr.Tk()

# --- Set overlay size and position (middle left) ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
overlay_width = 150
overlay_height = 60
x_pos = 0  # far left
y_pos = screen_height // 2 - overlay_height // 2  # vertically centered
root.geometry(f"{overlay_width}x{overlay_height}+{x_pos}+{y_pos}")

root.overrideredirect(True)   # No border or title
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "black")  # Make black fully transparent
root.wm_attributes("-alpha", 1.0)  # text fully visible
root.resizable(0, 0)

# --- Make overlay non-clickable + non-focusable ---
hwnd = windll.user32.GetParent(root.winfo_id())
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20
WS_EX_NOACTIVATE = 0x08000000
styles = windll.user32.GetWindowLongW(hwnd, -20)
windll.user32.SetWindowLongW(hwnd, -20, styles | WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_NOACTIVATE)
# ---------------------------------------------------

# Timer label (black bg will be transparent)
timer_display = tkr.Label(root, font=('Trebuchet MS', 20, 'bold'), fg='green', bg='black')
timer_display.pack(expand=True, fill='both')

seconds = 44

# ANSI color codes
RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"   # purple
CYAN    = "\033[36m"
WHITE   = "\033[37m"
BOLD    = "\033[1m"

# --- Banner ---
print(CYAN + "═══════════════════════════════════════════════" + RESET)
print(
    BOLD + GREEN + " Valorant Spike Timer "
    + RESET + CYAN + " │ " + RESET
    + WHITE + "Made by: "
    + MAGENTA + BOLD + "Gomorronmannen" + RESET
)
print(CYAN + "═══════════════════════════════════════════════" + RESET)
print("")

# --- Description ---
print(WHITE + " This version uses " + BOLD + YELLOW + "AI in Python" + RESET + WHITE + " to automatically detect" + RESET)
print(WHITE + " when the spike has been planted & start a " + BOLD + "45s countdown" + RESET)
print(WHITE + " for when the spike will explode and if you have the time" + RESET)
print(WHITE + " to defuse." + RESET)
print("")

# --- Status ---
print(GREEN + BOLD + " ✔  Overlay activation success" + RESET)
print(RED   + BOLD + " ⚠  PLEASE DO NOT CLOSE THIS WINDOW OR IT WILL NOT WORK" + RESET)
print("")

# --- Profile ---
print(BLUE + BOLD + " 🌐  My Profile: " + RESET + "https://gomorronmannen.github.io/my-profile/")
print("")
print(CYAN + "═══════════════════════════════════════════════" + RESET)




def countdown(time):
    if time > 0:
        mins, secs = divmod(time, 60)

        def color_change(t_time):
            if t_time > 10:
                return 'green'
            elif 7 <= t_time <= 10:
                return 'yellow'
            else:
                return 'red'

        timer_display.config(
            text="{:02d}:{:02d}".format(mins, secs),
            fg=color_change(time)
        )

        root.after(1000, countdown, time - 1)
    else:
        root.wm_attributes('-alpha', 0.01)
        search_image()


def start_countdown():
    root.wm_attributes('-alpha', 1.0)  # make text fully visible
    countdown(seconds)


def search_image():
    pos = imagesearch("./github.png")
    pos1 = imagesearch("./github1.png")
    if pos[0] & pos1[0] != -1:
        start_countdown()
    else:
        root.after(100, search_image)


root.after(100, search_image)
root.mainloop()
