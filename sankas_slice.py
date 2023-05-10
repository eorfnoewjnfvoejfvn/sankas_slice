import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re


import tkinter as tk
from tkinter import ttk

class FormGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Form Window")

        # Variables for form fields
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.phone_number_var = tk.StringVar()

        # Create the form fields
        self.label_first_name = ttk.Label(self.window, text="First Name:")
        self.label_first_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_first_name = ttk.Entry(self.window, textvariable=self.first_name_var)
        self.entry_first_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_last_name = ttk.Label(self.window, text="Last Name:")
        self.label_last_name.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_last_name = ttk.Entry(self.window, textvariable=self.last_name_var)
        self.entry_last_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_phone_number = ttk.Label(self.window, text="Phone Number:")
        self.label_phone_number.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_phone_number = ttk.Entry(self.window, textvariable=self.phone_number_var)
        self.entry_phone_number.grid(row=2, column=1, padx=10, pady=10)

        # Add a submit button
        self.submit_button = ttk.Button(self.window, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create an instance of the FormGUI class
form = FormGUI()

# Start the main event loop
form.window.mainloop()

