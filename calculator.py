import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Set up the window
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i in range(4):
    for j in range(4):
        b = tk.Button(root, text=buttons[i][j], font="Arial 18", width=5, height=2)
        b.grid(row=i+1, column=j, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
