import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])


# window setup
window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
frame = tk.Frame(window)
label = tk.Label(frame, text= "0", font = ("Arial", 30), anchor="e", width = column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")
frame.pack()
window.mainloop()