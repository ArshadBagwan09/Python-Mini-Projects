import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First Window")  # Title
window.geometry("300x300")  # Window size

# Label
label = tk.Label(window, text="Enter your name:")
label.pack(pady=10)

# Text Entry (Input box)
entry = tk.Entry(window)
entry.pack(pady=5)

# Checkbox
check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="I agree to terms", variable=check_var)
checkbox.pack(pady=5)


# Button Function
def on_click():
    name = entry.get()
    checked = check_var.get()
    print(f"Name: {name}")
    print(f"Agreed: {checked}")


# Button
button = tk.Button(window, text="Submit", command=on_click)
button.pack(pady=20)

# Start the GUI
window.mainloop()
