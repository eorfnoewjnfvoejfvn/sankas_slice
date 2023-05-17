import tkinter as tk
from tkinter import messagebox, ttk
import re


class FormGUI:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Form Window")

        # Variables for form fields
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.phone_number_var = tk.StringVar()

        # Create the form fields labels and entry fields
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
        self.entry_first_name.bind("<KeyRelease>", self.validate_fields)
        self.entry_last_name.bind("<KeyRelease>", self.validate_fields)
        self.entry_phone_number.bind("<KeyRelease>", self.validate_fields)

        # Create the submit button
        self.submit_button = ttk.Button(
            self.window,
            text="Submit",
            command=self.submit_form,
            state="disabled",  # Disable the button initially
        )
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.check_fields_completed()

    def validate_fields(self, event):
        """
        Validate if all form fields are non-empty.
        If all fields have non-empty values, enable the submit button.
        Otherwise, disable the submit button.
        """
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        phone_number = self.phone_number_var.get()

        if first_name.strip() and last_name.strip() and phone_number.strip():
            self.submit_button.config(state="normal")  # Enable the submit button
        else:
            self.submit_button.config(state="disabled")  # Disable the submit button

    def check_fields_completed(self):
        """
        Check if all form fields are completed at startup.
        If all fields are completed, enable the submit button.
        Otherwise, disable the submit button.
        """
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        phone_number = self.phone_number_var.get()

        if first_name and last_name and phone_number:
            self.submit_button.config(state="normal")  # Enable the submit button
        else:
            self.submit_button.config(state="disabled")  # Disable the submit button

    def submit_form(self):
        """
        Handle form submission.
        Check for form field validations and show error messages if necessary.
        If the form is valid, show a success message, destroy the current window,
        and open a new window for menu selection.
        """
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        phone_number = self.phone_number_var.get()

        if not first_name or not last_name or not phone_number:
            # Show error message if any field is empty
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not re.match(r"^[A-Za-z]*$", first_name):
            # Show error message if the first name contains non-alphabet characters
            messagebox.showerror("Error", "Invalid first name. Use alphabets only")
            return

        if not re.match(r"^[A-Za-z]*$", last_name):
            # Show error message if the last name contains non-alphabet characters
            messagebox.showerror("Error", "Invalid last name. Use alphabets only")
            return

        if not re.match(r"^[0-9]{10}$", phone_number):
            # Show error message if the phone number is not a 10-digit number
            messagebox.showerror("Error", "Invalid phone number. Enter 10 digits.")
            return

        # Show success message if the form is valid
        messagebox.showinfo("Success", "Form submitted successfully.")
        self.window.destroy()
        new_window = tk.Tk()
        new_window.title("Menu Selection")
        menu_selection_gui = MenuSelectionGUI(new_window, self)
        new_window.mainloop()


class Category:
    def __init__(self, name):
        """
        Initialize a Category object with a given name.
        The Category object represents a category of items.
        It has a name and an empty list to store items.
        """
        self.name = name
        self.items = []

    def add_item(self, item):
        """
        Add an item to the category.
        Append the item object to the list of items in the category.
        """
        self.items.append(item)


class Item:
    def __init__(self, name, price):
        """
        Initialize an Item object with a given name and price.
        The Item object represents an item in a category.
        It has a name and a price attribute.
        """
        self.name = name
        self.price = price


class MenuSelectionGUI:
    def __init__(self, parent, form_gui):
        self.form_gui = form_gui         
        #Initialize the MenuSelectionGUI class.
        #This class represents the menu selection GUI window.
        #It displays categories, items, and a cart for ordering items.
        self.categories = [
            Category("Pizza"),
            Category("Sides"),
            Category("Drinks")
        ]

        # Adding items to categories
        # Adding items to categories
        # Pizza category
        self.categories[0].add_item(Item("Margherita", 9.99))
        self.categories[0].add_item(Item("Pepperoni", 11.99))
        self.categories[0].add_item(Item("Vegetarian", 10.99))
        self.categories[0].add_item(Item("Meat Lovers", 10.99))
        self.categories[0].add_item(Item("Cheese", 10.99))
        self.categories[0].add_item(Item("Vegan", 10.99))

        # Sides category
        self.categories[1].add_item(Item("French Fries", 3.99))
        self.categories[1].add_item(Item("Garlic Bread", 4.99))
        self.categories[1].add_item(Item("Onion Rings", 4.99))
        self.categories[1].add_item(Item("Hash Bites", 4.99))
        self.categories[1].add_item(Item("Chicken Wings", 8.99))
        self.categories[1].add_item(Item("Chicken Strips", 8.99))

        # Drinks category
        self.categories[2].add_item(Item("Cola", 1.99))
        self.categories[2].add_item(Item("Lemonade", 2.99))
        self.categories[2].add_item(Item("Iced Tea", 2.49))
        self.categories[2].add_item(Item("Pepsi", 2.49))
        self.categories[2].add_item(Item("Fanta", 2.49))
        self.categories[2].add_item(Item("Sprite", 2.49))

        self.cart = []
        self.cart_size = 12  # Fixed size of the cart

        #creates gui window
        self.parent = parent
        self.parent.title("Menu Selection")
        self.parent.geometry("500x500")