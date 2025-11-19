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

# color 

orange = '#505050'

grey = '#D4D4D2'

black = '#1C1C1C'

white = '#ffffff'

darkgray = "#505050"

# window setup
window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
frame = tk.Frame(window)
label = tk.Label(frame, text= "0", font = ("Arial", 30), anchor="e", width = column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")


# button setup


for row in range(row_count):

    for column in range(column_count):

        value = button_values[row][column]

        button = tk.Button(frame, text=value, 

            width=column_count-1, 

            height=1, 

            font=("Arial", 30),

            command =lambda value=value: button_clicked(value))

        

        if value in right_symbols:

            button.config(background = grey, foreground =black)

        elif value in top_symbols:

            button.config(background =orange, foreground =black)

        else:

            button.config(background =darkgray, foreground= black)

        button.grid(row=row + 1, column=column)


           
def button_clicked(value):
    pass






frame.pack()

window.update()

window.width = window.winfo_width()

window.height = window.winfo_height()

screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()



window.x = int((screen_width/2) - (window.width/2))

window.y = int((screen_height/2) - (window.height/2))

window.geometry(f"{window.width}x{window.height}+{window.x}+{window.y}")



window.mainloop()







window.mainloop()