import pandas as pd

def collectData(filepath: str):
    """
    Creates a dataframe from either a csv file or making an empty one if one is not available
    at the entered filepath.

    Args:
        filepath (str): filepath of an existing or wished csv file.

    Returns:
        pd.DataFrame: A dataframe.
    """
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print("Could not find ", filepath, ", creating a new dataframe.")
        data = {
            "Date": [],
            "Description":  [],
            "Amount": [],
            "Type": []
        }
        df = pd.DataFrame(data)
    return df