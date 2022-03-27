from tkinter import messagebox
def Stats(r1, r2, r3, r4):
    if r1 > 0 and r2 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns found at 0° and 90° only!")
    if r1 > 0 and r3 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns found at 0° and 180° only!")
    if r1 > 0 and r4 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns found at 0° and 270° only!")
    if r2 > 0 and r3 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns found at 90° and 180° only!")
    if r2 > 0 and r4 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns found at 90° and 270° only!")
    if r3 > 0 and r4 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "Pattern found at 180° and 270° only!")
    if r1 > 0 and r2 > 0 and r3 > 0 and r4 > 0:
        messagebox.showinfo("Pattern Matching Statistics", "All rotations found successfully!")
    if r1 == 0 and r2 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 0° and 90° Not Found!")
    elif r1 == 0 and r3 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 0° and 180° Not Found!")
    elif r1 == 0 and r4 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 0° and 270° Not Found!")
    elif r2 == 0 and r3 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 90° and 180° Not Found!")
    elif r2 == 0 and r4 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 90° and 270° Not Found!")
    elif r3 == 0 and r4 == 0:
        messagebox.showinfo("Pattern Matching Statistics", "Patterns at 180° and 270° Not Found!")