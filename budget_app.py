import tkinter as tk
from tkinter import messagebox
import pandas as pd

class BudgetApp(tk.Frame):

    def __init__(self, root, df: pd.DataFrame, filepath: str) -> None:
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


    def add_entry(self) -> None:
        """
            Adds entries to the .csv file based on user input.
        """
        # Get the values entered in the fields
        date = self.entry_date.get()
        description =self.entry_description.get()
        amount = self.entry_amount.get()
        entry_type = self.entry_type.get()


        # Data validation
        # TODO: Better data validation? 
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

            
            # Romve the user inputes entries displayed, as they have been saved to the csv.
            self.entry_date.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
            self.entry_amount.delete(0, tk.END)
            self.entry_type.delete(0, tk.END)

        else: 
            messagebox.showerror("Error", "All fields are required.")

    
    def view_entries(self) -> None:
        """
            Creates a window that displays the .csv file information. Calls are from buttons to functions that enables editing and deleting entries from the .csv file.
        """
        self.top = tk.Toplevel(self.root) # Creates a new window.
        self.top.title("View Entries")

        # Create the textboxwrapper.
        text = tk.Text(self.top, width=125) # TODO: Make hight and width of the view entries window dynamic in the future.
        text.pack()

        # pandas.DataFrame.iterrows() yields index and row data
        for index, row in self.df.iterrows():
            text.insert(tk.END, f"Date: {row['Date']} | Description: {row['Description']} | Amount: {row['Amount']} NOK | Type: {row['Type']} \n")
        
            edit_button = tk.Button(self.top, text="Edit", command= lambda i = index: self.edit_entry(i))
            delete_button = tk.Button(self.top, text="Delete", command= lambda i = index: self.delete_entry(i))
            text.window_create(tk.END, window=edit_button)
            text.window_create(tk.END, window=delete_button)
            text.insert(tk.END, "\n")

    def edit_entry(self, index: int) -> None:
        """
            Edits entries in the .csv file

            Args:
                index (int): index of the row that is to be edited.
        """
        # Create a new window and sets the title
        self.edit_top = tk.Toplevel(self.root)
        self.edit_top.title("Edit Entry")

        self.edit_date = tk.Entry(self.edit_top)
        self.edit_date.insert(0, self.df.at[index, 'Date'])
        self.edit_date.pack()

        self.edit_description = tk.Entry(self.edit_top)
        self.edit_description.insert(0, self.df.at[index, 'Description'])
        self.edit_description.pack()

        self.edit_amount = tk.Entry(self.edit_top)
        self.edit_amount.insert(0, self.df.at[index, 'Amount'])
        self.edit_amount.pack()

        self.edit_type = tk.Entry(self.edit_top)
        self.edit_type.insert(0, self.df.at[index, 'Type'])
        self.edit_type.pack()

        save_button = tk.Button(self.edit_top, text="Save", command= lambda i = index: self.save_edit(i))
        save_button.pack()

    def save_edit(self, index: int) -> None:
        """
            Saves the edited row information to the .csv file. 

            Args:
                index (int): index of the row that is to be edited.
        """
        self.df.at[index, 'Date'] = self.edit_date.get()
        self.df.at[index, 'Description'] = self.edit_description.get()
        self.df.at[index, 'Amount'] = self.edit_amount.get()
        self.df.at[index, 'Type'] = self.edit_type.get()

        self.df.to_csv(self.filepath, index=False)
        messagebox.showinfo("Success", "Entry updated successfully.")

        self.edit_top.destroy()
        self.top.destroy()
        self.view_entries()

    def delete_entry(self, index: int) -> None:
        """
            Deletes entries from the .csv files

            Args:
                index (int): index of the row that is to be deleted.

        """
        
        self.df.drop(index, inplace=True) #inplace=True does not return a copied dataframe without the entry, but performs the operation in the dataframe and returns None.
        self.df.reset_index(drop=True, inplace=True) 
        self.df.to_csv(self.filepath, index=False)
        messagebox.showinfo("Success", "Entry Deleted succesfully")

        self.top.destroy()
        self.view_entries()
