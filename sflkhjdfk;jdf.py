import math
import tkinter as tk

root = tk.Tk()
root.title("Black Hole gravity node calculator")
root.geometry("400x300")

Scaledradius = None 
mass = None
Schildradius = None
divider = None

top_label = tk.Label(root, text="Enter the desired black hole radius in standard notation (KM):")
top_label.grid(row=0, column=0, padx=10, pady=10)



entry = tk.Entry(root)
entry.grid(row=1, column=0, padx=10, pady=10)

mult_label = tk.Label(root, text="Enter the divisor to scale the radius (e.g., 1 (stock ksp), 2.5(Jnsq) 10(),):")
mult_label.grid(row=0, column=1, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

def calculate_gravity():
    global Schildradius
    try:
        Schildradiusradius = float(entry.get())
        scaler = float(entry2.get())
        Scaledradius = ((Schildradiusradius / 10) * scaler)
        gravity = (Scaledradius / 5) ** 2
        result_label.config(text=f"Calculated gravity: {gravity:.3f}")
    except ValueError:
        result_label.config(text="Please enter a valid number for the radius.")

calculate_button = tk.Button(root, text="Calculate Gravity", command=calculate_gravity)
calculate_button.grid(row=2, column=0, padx=10, pady=10)



result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, padx=10, pady=10)





root.mainloop()


