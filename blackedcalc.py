import math
import tkinter as tk

root = tk.Tk()
root.title("Black Hole gravity node calculator")
root.geometry("600x500")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

Scaledradius = None 
mass = None
Schildradius = None
divider = None

top_label = tk.Label(root, text="Enter the desired black hole radius in standard notation (KM):")
top_label.grid(row=5, column=0, padx=10, pady=10)

mass_label = tk.Label(root, text="Enter the mass of the black hole in solar masses (optional, for Schwarzschild radius calculation):")
mass_label.grid(row=3, column=0, padx=10, pady=10)

mass_entry = tk.Entry(root)
mass_entry.grid(row=4, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=6, column=0, padx=10, pady=10)

mult_label = tk.Label(root, text="Enter the factor to scale the radius (e.g., 1 (stock ksp), 2.5(Jnsq) 10(real solar system).):")
mult_label.grid(row=7, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=8, column=0, padx=10, pady=10)

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

def calculate_schwarzschild_radius():
    global mass
    try:
        mass = float(mass_entry.get())
        Schildradius = (2 * 6.67430e-11 * mass * 1.98847e30) / (299792458 ** 2) / 1000
        entry.config(text=f"Calculated Schwarzschild radius: {Schildradius:.3f} km")
    except ValueError:
        result_label.config(text="Please enter a valid number for the mass.")









button_frame = tk.Frame(root)
button_frame.grid(row=9, column=0, columnspan=2, padx=0, pady=0)

calculate_button = tk.Button(button_frame, text="Calculate Gravity", command=calculate_gravity)
calculate_button.pack(side="left", padx=(0, 5))

swrtbutton = tk.Button(button_frame, text="Calculate Schwarzschild Radius", command=calculate_schwarzschild_radius)
swrtbutton.pack(side="left")

result_label = tk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)





root.mainloop()


