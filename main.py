import tkinter as tk
import pandas as pd
from app import *


def main() -> None:
    
    try:
        df = pd.read_csv('./expenses.csv')
    except Exception as e:
        data = {
            "Date": [],
            "Description":  [],
            "Amount": [],
            "Type": []
        }
        df = pd.DataFrame(data)


    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop
    print("hey")

if __name__ == "__main__":
    main()