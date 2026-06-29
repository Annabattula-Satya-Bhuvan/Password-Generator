import tkinter as tk
from tkinter import messagebox
import string, secrets, random

BG="#0b0f19"; CARD="#151a2d"; BLUE="#0099ff"; FG="white"

def pool():
    s=""
    if up.get(): s+=string.ascii_uppercase
    if low.get(): s+=string.ascii_lowercase
    if num.get(): s+=string.digits
    if sym.get(): s+=string.punctuation
    return s

def strength(p):
    score=0
    score+=len(p)>=8
    score+=len(p)>=12
    score+=any(c.isupper() for c in p)
    score+=any(c.islower() for c in p)
    score+=any(c.isdigit() for c in p)
    score+=any(c in string.punctuation for c in p)
    if score<=2:return "Weak","red"
    if score<=4:return "Medium","orange"
    return "Strong","lime"

def generate():
    chars=pool()
    if not chars:
        messagebox.showerror("Error","Select at least one character type.")
        return
    try:l=int(length.get())
    except: 
        messagebox.showerror("Error","Enter a valid length.");return
    if l<4:
        messagebox.showerror("Error","Minimum length is 4.");return
    pwd=[]
    if up.get(): pwd.append(secrets.choice(string.ascii_uppercase))
    if low.get(): pwd.append(secrets.choice(string.ascii_lowercase))
    if num.get(): pwd.append(secrets.choice(string.digits))
    if sym.get(): pwd.append(secrets.choice(string.punctuation))
    while len(pwd)<l:
        pwd.append(secrets.choice(chars))
    random.shuffle(pwd)
    p="".join(pwd[:l])
    out.config(state="normal")
    out.delete(0,"end"); out.insert(0,p); out.config(state="readonly")
    t,c=strength(p); lbl.config(text=t,fg=c)

def copy():
    p=out.get()
    if p:
        root.clipboard_clear(); root.clipboard_append(p)
        messagebox.showinfo("Copied","Password copied.")

def save():
    p=out.get()
    if p:
        with open("password_history.txt","a") as f:f.write(p+"\n")
        messagebox.showinfo("Saved","Saved to password_history.txt")

def toggle():
    out.config(show="" if show.get() else "*")

root=tk.Tk()
root.title("Premium Password Generator")
root.geometry("520x500")
root.configure(bg=BG)

tk.Label(root,text="🔐 Premium Password Generator",bg=BG,fg=BLUE,font=("Segoe UI",20,"bold")).pack(pady=15)
card=tk.Frame(root,bg=CARD,padx=20,pady=20)
card.pack(padx=20,pady=10,fill="both",expand=True)

tk.Label(card,text="Length",bg=CARD,fg=FG).pack(anchor="w")
length=tk.Entry(card); length.insert(0,"12"); length.pack(fill="x",pady=5)

up=tk.BooleanVar(value=True);low=tk.BooleanVar(value=True);num=tk.BooleanVar(value=True);sym=tk.BooleanVar(value=True);show=tk.BooleanVar()
for txt,var in [("Uppercase",up),("Lowercase",low),("Numbers",num),("Symbols",sym)]:
    tk.Checkbutton(card,text=txt,variable=var,bg=CARD,fg=FG,selectcolor=CARD,activebackground=CARD).pack(anchor="w")

tk.Button(card,text="Generate",command=generate,bg=BLUE,fg="white").pack(fill="x",pady=10)
out=tk.Entry(card,font=("Consolas",13),show="*",state="readonly",readonlybackground="#0d1323",readonlyforeground="#00ffff")
out.pack(fill="x",pady=5)
tk.Checkbutton(card,text="Show Password",variable=show,command=toggle,bg=CARD,fg=FG,selectcolor=CARD).pack(anchor="w")
lbl=tk.Label(card,text="-",bg=CARD,fg="white",font=("Segoe UI",11,"bold")); lbl.pack(pady=8)
bf=tk.Frame(card,bg=CARD); bf.pack()
tk.Button(bf,text="Copy",command=copy,bg="#008cff",fg="white").grid(row=0,column=0,padx=5)
tk.Button(bf,text="Save",command=save,bg="#2962ff",fg="white").grid(row=0,column=1,padx=5)
tk.Button(bf,text="Clear",command=lambda:(out.config(state="normal"),out.delete(0,"end"),out.config(state="readonly"),lbl.config(text="-",fg="white")),bg="#555",fg="white").grid(row=0,column=2,padx=5)
root.mainloop()
