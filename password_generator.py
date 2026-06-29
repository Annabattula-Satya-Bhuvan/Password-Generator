import tkinter as tk
from tkinter import messagebox
import string
import secrets

# -----------------------------
# Password Generator Function
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
            messagebox.showerror("Error", "Select at least one option.")
            return

        password = ''.join(secrets.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

        messagebox.showinfo("Copied", "Password copied to clipboard!")

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Premium Password Generator")
root.geometry("500x520")
root.configure(bg="#0b0f19")
root.resizable(False, False)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Segoe UI", 22, "bold"),
    bg="#0b0f19",
    fg="#00BFFF"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Generate Strong & Secure Passwords",
    font=("Segoe UI", 11),
    bg="#0b0f19",
    fg="white"
)

subtitle.pack()

# -----------------------------
# Length
# -----------------------------
tk.Label(
    root,
    text="Password Length",
    bg="#0b0f19",
    fg="white",
    font=("Segoe UI",11)
).pack(pady=(25,5))

length_entry = tk.Entry(
    root,
    width=20,
    font=("Segoe UI",14),
    justify="center"
)

length_entry.insert(0,"12")
length_entry.pack()

# -----------------------------
# Options
# -----------------------------
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

frame = tk.Frame(root,bg="#0b0f19")
frame.pack(pady=25)

tk.Checkbutton(
    frame,
    text="Uppercase",
    variable=upper_var,
    bg="#0b0f19",
    fg="white",
    selectcolor="#1b2336",
    activebackground="#0b0f19"
).grid(row=0,column=0,padx=20,pady=8)

tk.Checkbutton(
    frame,
    text="Lowercase",
    variable=lower_var,
    bg="#0b0f19",
    fg="white",
    selectcolor="#1b2336",
    activebackground="#0b0f19"
).grid(row=0,column=1,padx=20,pady=8)

tk.Checkbutton(
    frame,
    text="Numbers",
    variable=number_var,
    bg="#0b0f19",
    fg="white",
    selectcolor="#1b2336",
    activebackground="#0b0f19"
).grid(row=1,column=0,padx=20,pady=8)

tk.Checkbutton(
    frame,
    text="Symbols",
    variable=symbol_var,
    bg="#0b0f19",
    fg="white",
    selectcolor="#1b2336",
    activebackground="#0b0f19"
).grid(row=1,column=1,padx=20,pady=8)

# -----------------------------
# Generate Button
# -----------------------------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#007BFF",
    fg="white",
    font=("Segoe UI",12,"bold"),
    width=22,
    height=2
)

generate_btn.pack(pady=10)

# -----------------------------
# Result
# -----------------------------
password_entry = tk.Entry(
    root,
    width=32,
    font=("Consolas",14),
    justify="center"
)

password_entry.pack(pady=20)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#00BFFF",
    fg="black",
    font=("Segoe UI",11,"bold"),
    width=20
)

copy_btn.pack()

root.mainloop()
