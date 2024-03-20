import pandas as pd

def enter_text_from_console():
    """
    Function to enter text from the console.

    Returns:
        str: Text entered by the user.
    """
    return input("Enter text: ")

def read_from_file(file_path):
    """
    Function to read from a file using Python's built-in capabilities.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        str: Contents of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def read_from_file_with_pandas(file_path):
    """
    Function to read from a file using the pandas library.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        DataFrame: Data read from the file using pandas.
    """
    return pd.read_csv(file_path)


