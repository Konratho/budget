import tkinter as tk
from tkinter import messagebox

class BudgetApp(tk.Frame):

    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")

        # Data entries
        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.label_date.grid(row=0, column=0)
        self.entry_date =tk.Entry(root)
        self.entry_date.grid(row=0, column=1)

        self.label_description = tk.Label(root, text="Description:")
        self.label_description.grid(row=1, column=0)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=1, column=1)

        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.grid(row=2, column=0)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=2, column=1)

        self.label_type = tk.Label(root, text="Type (Income/Expense):")
        self.label_type.grid(row=3, column=0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=3, column=1)

        # Buttons
        self.button_add = tk.Button(root, text="Add entry", command=self.add_entry)
        self.button_add.grid(row=4, column=0, columnspan=2)

        self.button_view = tk.Button(root, text="View Entries", command=self.view_entries)
        self.button_view.grid(row=5, column=0, columnspan=2)

        



    def add_entry(self):
        
        date = self.entry_date.get()
        description =self.entry_description.get()
        amount = self.entry_amount.get()
        type = self.entry_type.get()

        print(f"{date}, {description}, {amount}, {type}")

    
    def view_entries(self):
        pass


