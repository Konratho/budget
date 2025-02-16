import tkinter as tk
from tkinter import messagebox
import pandas as pd

class BudgetApp(tk.Frame):

    def __init__(self, root, df: pd.DataFrame, filepath: str):
        self.root = root
        self.root.title("Budget Tracker")
        
        self.df = df
        self.filepath = filepath

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
        
        # Get the values entered in the fields
        date = self.entry_date.get()
        description =self.entry_description.get()
        amount = self.entry_amount.get()
        entry_type = self.entry_type.get()


        # Data validation
        # For now: Only checks if something has been entered in the fields.
        if date and description and amount and entry_type:

            new_entry = pd.DataFrame({
                            "Date": [date],
                            "Description":  [description],
                            "Amount": [amount],
                            "Type": [entry_type]
                        })
            
            # Add the new entry to the complete dataframe, and write it to the CSV.
            self.df = pd.concat([self.df, new_entry], ignore_index=True)
            self.df.to_csv(self.filepath, index=False)
            messagebox.showinfo("Success", "Entry saved.")

            
            # Delete the entries in the app, as they have been saved in the csv.
            self.entry_date.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
            self.entry_amount.delete(0, tk.END)
            self.entry_type.delete(0, tk.END)

        else: 
            messagebox.showerror("Error", "All fields are required.")

    
    def view_entries(self):
        self.top = tk.Toplevel(self.root) # Creates a new window.
        self.top.title("View Entries")

        text = tk.Text(self.top)
        text.pack()

        for index, row in self.df.iterrows():
            text.insert(tk.END, f"Date: {row['Date']} | Description: {row['Description']} | Amount: {row['Amount']} | Type: {row['Type']} \n")
        
            edit_button = tk.Button(self.top, text="Edit", command= lambda i = index: self.edit_entry(i))
            delete_button = tk.Button(self.top, text="Delete", command= lambda i = index: self.delete_entry(i))
            text.window_create(tk.END, window=edit_button)
            text.window_create(tk.END, window=delete_button)
            text.insert(tk.END, "\n")