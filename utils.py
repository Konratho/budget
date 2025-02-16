import pandas as pd

def collectData(filepath: str):
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        data = {
            "Date": [],
            "Description":  [],
            "Amount": [],
            "Type": []
        }
        df = pd.DataFrame(data)
    return df