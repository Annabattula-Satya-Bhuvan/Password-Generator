import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets

# -----------------------------
# Colors
# -----------------------------
BG = "#0B0F19"
CARD = "#151C2E"
BLUE = "#00A8FF"
TEXT = "#FFFFFF"
GREEN = "#00E676"
ORANGE = "#FFB300"
RED = "#FF5252"

# -----------------------------
# Generate Password
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

        update_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length.")

# -----------------------------
# Password Strength
# -----------------------------
def update_strength(password):

    score = 0

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        strength_label.config(text="Weak", fg=RED)

    elif score <= 4:
        strength_label.config(text="Medium", fg=ORANGE)

    else:
        strength_label.config(text="Strong", fg=GREEN)

# -----------------------------
# Copy Password
# -----------------------------
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

# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle_password():

    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# -----------------------------
# Save Password
# -----------------------------
def save_password():

    password = password_entry.get()

    if password == "":
        return

    with open("password_history.txt","a") as file:
        file.write(password+"\n")

    messagebox.showinfo(
        "Saved",
        "Password saved to password_history.txt"
    )

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Premium Password Generator")

root.geometry("600x650")

root.configure(bg=BG)

root.resizable(False,False)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(

    root,

    text="🔐 Premium Password Generator",

    font=("Segoe UI",24,"bold"),

    bg=BG,

    fg=BLUE

)

title.pack(pady=20)

subtitle = tk.Label(

    root,

    text="Generate Secure Random Passwords",

    font=("Segoe UI",11),

    bg=BG,

    fg="white"

)

subtitle.pack()

# -----------------------------
# Card
# -----------------------------
card = tk.Frame(

    root,

    bg=CARD,

    padx=30,

    pady=25

)

card.pack(pady=30)

# Password Length

tk.Label(

    card,

    text="Password Length",

    font=("Segoe UI",11),

    bg=CARD,

    fg=TEXT

).pack(anchor="w")

length_entry = ttk.Entry(card,font=("Segoe UI",12),width=20)

length_entry.insert(0,"12")

length_entry.pack(pady=10)

# Checkboxes

upper_var=tk.BooleanVar(value=True)
lower_var=tk.BooleanVar(value=True)
number_var=tk.BooleanVar(value=True)
symbol_var=tk.BooleanVar(value=True)

ttk.Checkbutton(card,text="Uppercase",variable=upper_var).pack(anchor="w")
ttk.Checkbutton(card,text="Lowercase",variable=lower_var).pack(anchor="w")
ttk.Checkbutton(card,text="Numbers",variable=number_var).pack(anchor="w")
ttk.Checkbutton(card,text="Symbols",variable=symbol_var).pack(anchor="w")

# Generate Button

generate_btn=tk.Button(

    card,

    text="Generate Password",

    command=generate_password,

    bg=BLUE,

    fg="white",

    font=("Segoe UI",12,"bold"),

    relief="flat",

    padx=20,

    pady=10

)

generate_btn.pack(fill="x",pady=20)

# Password Field

password_entry=tk.Entry(

    card,

    font=("Consolas",14),

    justify="center",

    width=35,

    show="*",

    state="readonly"

)

password_entry.pack()

# Show Password

show_var=tk.BooleanVar()

tk.Checkbutton(

    card,

    text="Show Password",

    variable=show_var,

    command=toggle_password,

    bg=CARD,

    fg="white",

    selectcolor=CARD

).pack(anchor="w",pady=10)

# Strength

strength_title=tk.Label(

    card,

    text="Password Strength:",

    bg=CARD,

    fg="white",

    font=("Segoe UI",11)

)

strength_title.pack()

strength_label=tk.Label(

    card,

    text="-",

    bg=CARD,

    fg=GREEN,

    font=("Segoe UI",13,"bold")

)

strength_label.pack()

# Buttons

button_frame=tk.Frame(card,bg=CARD)

button_frame.pack(pady=20)

copy_btn=tk.Button(

    button_frame,

    text="Copy",

    command=copy_password,

    bg="#0099FF",

    fg="white",

    width=12

)

copy_btn.grid(row=0,column=0,padx=10)

save_btn=tk.Button(

    button_frame,

    text="Save",

    command=save_password,

    bg="#2962FF",

    fg="white",

    width=12

)

save_btn.grid(row=0,column=1,padx=10)

# Footer

footer=tk.Label(

    root,

    text="Designed with Python • Tkinter • Secrets Module",

    bg=BG,

    fg="#8DA9C4",

    font=("Segoe UI",9)

)

footer.pack(side="bottom",pady=15)

root.mainloop()
