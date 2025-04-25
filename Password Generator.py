import tkinter as tk
from tkinter import StringVar, messagebox, simpledialog
import random
import string

def generate_password():
    length = simpledialog.askinteger("Password Length", "Enter password length (6-18):", minvalue=6, maxvalue=18)
    if length is None:
        return
    
    characters = ""
    allowed_symbols = "!?$^&*@#~.<>+=_"  # Only these symbols are allowed
    
    if var_symbols.get():
        characters += allowed_symbols
    if var_numbers.get():
        characters += string.digits
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one option!")
        return
    
    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set("*" * length)
    hidden_password.set(password)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def show_password(event):
    entry.config(show="")
    password_var.set(hidden_password.get())

def hide_password(event):
    entry.config(show="*")
    password_var.set("*" * len(hidden_password.get()))

def scroll_text():
    text = "Created By M1   "
    marquee_label.config(text=text)
    def update_text(x_pos):
        marquee_label.place(x=x_pos, y=root.winfo_height() - 30)
        if x_pos + marquee_label.winfo_reqwidth() > 0:
            root.after(20, update_text, x_pos - 2)
        else:
            root.after(20, update_text, root.winfo_width())
    update_text(root.winfo_width())

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x320")
root.configure(bg="black")

var_symbols = tk.BooleanVar(value=False)
var_numbers = tk.BooleanVar(value=False)
var_uppercase = tk.BooleanVar(value=False)
var_lowercase = tk.BooleanVar(value=False)
password_var = StringVar()
hidden_password = StringVar()

title_label = tk.Label(root, text="Password Generator", font=("Arial", 14), fg="white", bg="black")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="black")
frame.pack()

tk.Checkbutton(frame, text="Symbols", variable=var_symbols, bg="black", fg="white", selectcolor="black").grid(row=0, column=0, padx=10, pady=10)
tk.Checkbutton(frame, text="Numbers", variable=var_numbers, bg="black", fg="white", selectcolor="black").grid(row=0, column=1, padx=10, pady=10)
tk.Checkbutton(frame, text="Uppercase", variable=var_uppercase, bg="black", fg="white", selectcolor="black").grid(row=1, column=0, padx=10, pady=10)
tk.Checkbutton(frame, text="Lowercase", variable=var_lowercase, bg="black", fg="white", selectcolor="black").grid(row=1, column=1, padx=10, pady=10)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="gray", fg="white")
generate_btn.pack(pady=20)

entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), justify="center", state="readonly", show="*")
entry.pack(pady=10)
entry.bind("<Enter>", show_password)
entry.bind("<Leave>", hide_password)

marquee_label = tk.Label(root, text="", font=("Arial", 10), fg="white", bg="black", anchor="w")
marquee_label.pack(side="bottom", fill="x", pady=5)
root.after(100, scroll_text)

root.mainloop()