

def output_text_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): Text to be output to the console.
    """
    print(text)

def write_to_file(file_path, data):
    """
    Function to write to a file using Python's built-in capabilities.

    Args:
        file_path (str): Path to the file to be written.
        data: Data to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)
