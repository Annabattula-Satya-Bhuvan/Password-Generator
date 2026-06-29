import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets
import random

# ===========================
# Color Theme
# ===========================
BG_COLOR = "#0B0F19"
CARD_COLOR = "#151A2D"
PRIMARY = "#0099FF"
SECONDARY = "#1E293B"
TEXT = "#FFFFFF"
SUCCESS = "#00E676"
WARNING = "#FFC107"
DANGER = "#FF5252"

# ===========================
# Main Window
# ===========================
root = tk.Tk()
root.title("Premium Password Generator")
root.geometry("700x650")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCheckbutton",
    background=CARD_COLOR,
    foreground="white",
    font=("Segoe UI", 10)
)

# ===========================
# Variables
# ===========================
length_var = tk.IntVar(value=12)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

show_var = tk.BooleanVar(value=False)

# ===========================
# Character Pool
# ===========================
def get_characters():

    chars = ""

    if upper_var.get():
        chars += string.ascii_uppercase

    if lower_var.get():
        chars += string.ascii_lowercase

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    return chars

# ===========================
# Password Strength
# ===========================
def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak", DANGER

    elif score <= 4:
        return "Medium", WARNING

    else:
        return "Strong", SUCCESS

# ===========================
# Generate Password
# ===========================
def generate_password():

    characters = get_characters()

    if not characters:
        messagebox.showerror(
            "Error",
            "Please select at least one character type."
        )
        return

    length = length_var.get()

    if length < 4:
        messagebox.showerror(
            "Error",
            "Password length must be at least 4."
        )
        return

    password = ""

    if upper_var.get():
        password += secrets.choice(string.ascii_uppercase)

    if lower_var.get():
        password += secrets.choice(string.ascii_lowercase)

    if number_var.get():
        password += secrets.choice(string.digits)

    if symbol_var.get():
        password += secrets.choice(string.punctuation)

    while len(password) < length:
        password += secrets.choice(characters)

    password = list(password)
    random.shuffle(password)
    password = "".join(password[:length])

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    strength, color = password_strength(password)

    strength_label.config(
        text=strength,
        fg=color
    )

# ===========================
# Copy Password
# ===========================
def copy_password():

    password = password_entry.get()

    if password == "":
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied successfully!"
    )

# ===========================
# Save Password
# ===========================
def save_password():

    password = password_entry.get()

    if password == "":
        return

    with open("password_history.txt", "a") as file:
        file.write(password + "\n")

    messagebox.showinfo(
        "Saved",
        "Password saved successfully!"
    )

# ===========================
# Show / Hide Password
# ===========================
def toggle_password():

    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
