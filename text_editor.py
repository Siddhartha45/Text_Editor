from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

w = Tk()
w.title("Text Editor")
w.rowconfigure(0, minsize=800, weight=1)
w.columnconfigure(1, minsize=800, weight=1)

def openfile():     #function for opening file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_area.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_area.insert(END, text)
    w.title(f"Text Editor - {filepath}")

def saveas():       #function for saving file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_area.get(1.0, END)
        output_file.write(text)
    w.title(f"Text Editor - {filepath}")

text_area = Text(w, bd=2)
button_area = Frame(w)
open_button = Button(button_area, text="Open", command=openfile)
save_button = Button(button_area, text="Save as", command=saveas)

open_button.grid(row=0, column=0, sticky="ew", padx=8, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=8)
text_area.grid(row=0, column=1, sticky="nsew")
button_area.grid(row=0, column=0, sticky="ns")

w.mainloop()