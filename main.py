from BudgetApp import *
from utils import *

def main() -> None:
    
    # Collect earlier saved data
    collectData('.\history.csv')

    # Start tkinter
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()