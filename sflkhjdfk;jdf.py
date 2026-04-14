import math
import tkinter as tk

root = tk.Tk()
root.title("Black Hole gravity node calculator")
root.geometry("400x300")

radius = None 

top_label = tk.Label(root, text="Enter the desired black hole radius in standard notation (KM):")
top_label.grid(row=0, column=0, padx=10, pady=10)



entry = tk.Entry(root)
entry.grid(row=1, column=0, padx=10, pady=10)


def calculate_gravity():
    global radius
    try:
        radius = float(entry.get())
        gravity = (radius / 5) ** 2
        result_label.config(text=f"Calculated gravity: {gravity:.3f}")
    except ValueError:
        result_label.config(text="Please enter a valid number for the radius.")

calculate_button = tk.Button(root, text="Calculate Gravity", command=calculate_gravity)
calculate_button.grid(row=2, column=0, padx=10, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, padx=10, pady=10)





root.mainloop()