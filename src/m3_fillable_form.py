import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Form")

bg_color = "#f0f0f0"  
fg_color = "#333333"  

window.configure(background=bg_color)

fields = [
    ("Name", 30),
    ("Address Line 1", 40),
    ("Address Line 2", 40),
    ("City", 30),
    ("State", 5),
    ("Zip Code", 10),
    ("Phone Number", 15),
    ("Email Address", 30)
]

for field_name, field_width in fields:
    label = tk.Label(window, text=field_name, bg=bg_color, fg=fg_color)
    label.pack(pady=5)
    entry = tk.Entry(window, width=field_width)
    entry.pack(pady=2)


submit_button = tk.Button(window, text="Submit", bg="#007bff", fg="white", width=20)
submit_button.pack(pady=10)

# Call the mainloop method to show the window
window.mainloop()