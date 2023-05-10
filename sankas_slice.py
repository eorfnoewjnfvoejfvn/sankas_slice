import tkinter as tk
from tkinter import messagebox, ttk

class FormGUI:
    def __init__(self, order_summary):
        self.order_summary = order_summary
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

        # Validate fields on entry
        self.entry_first_name.bind("<KeyRelease>", self.validate_first_name)
        self.entry_last_name.bind("<KeyRelease>", self.validate_last_name)
        self.entry_phone_number.bind("<KeyRelease>", self.validate_phone_number)

        # Create the submit button
        self.submit_button = ttk.Button(self.window, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.submit_button.config(state="disabled")

    def validate_first_name(self, event):
            first_name = self.first_name_var.get()
            if not re.match(r"^[A-Za-z]*$", first_name):
                self.entry_first_name.config(style="Error.TEntry")
                self.submit_button.config(state="disabled")
            else:
                self.entry_first_name.config(style="TEntry")
                self.check_fields_completed()

    def validate_last_name(self, event):
            last_name = self.last_name_var.get()
            if not re.match(r"^[A-Za-z]*$", last_name):
                self.entry_last_name.config(style="Error.TEntry")
                self.submit_button.config(state="disabled")
            else:
                self.entry_last_name.config(style="TEntry")
                self.check_fields_completed()

    def validate_phone_number(self, event):
            phone_number = self.phone_number_var.get()
            if not re.match(r"^\d{10}$", phone_number):
                self.entry_phone_number.config(style="Error.TEntry")
                self.submit_button.config(state="disabled")
            else:
                self.entry_phone_number.config(style="TEntry")
                self.check_fields_completed()

    def check_fields_completed(self):
            first_name = self.first_name_var.get()
            last_name = self.last_name_var.get()
            phone_number = self.phone_number_var.get()

            if first_name and last_name and phone_number:
                self.submit_button.config(state="normal")
            else:
                self.submit_button.config(state="disabled")

    def submit_form(self):
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        phone_number = self.phone_number_var.get()

        if not first_name or not last_name or not phone_number:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not re.match(r"^[A-Za-z]*$", first_name):
            messagebox.showerror("Error", "Invalid first name.")
            return

        if not re.match(r"^[A-Za-z]*$", last_name):
            messagebox.showerror("Error", "Invalid last name.")
            return

        if not re.match(r"^\d{10}$", phone_number):
            messagebox.showerror("Error", "Invalid phone number.")
            return

        messagebox.showinfo("Success", " Detail's Colletected successfully.")
        self.window.destroy()


class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create an instance of the FormGUI class
form = FormGUI()

# Start the main event loop
form.window.mainloop()

