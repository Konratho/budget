from budget_app import *
from utils import *

filepath: str = ".\\history.csv" 
print("You're using the filepath:", filepath)


def main() -> None:
    # Collect earlier saved data
    df = collectData(filepath)

    # Start tkinter
    root = tk.Tk()
    BudgetApp(root, df, filepath)
    root.mainloop()

if __name__ == "__main__":
    main()