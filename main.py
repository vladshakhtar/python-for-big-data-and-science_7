from app.io.input import *
from app.io.output import *


def main():
    # Enter text from the console
    text_from_console = enter_text_from_console()
    # Output text to the console
    output_text_to_console(text_from_console)
    # Write text to a file using built-in Python capabilities
    write_to_file("output.txt", text_from_console)

    # Read from a file using Python's built-in capabilities
    file_content = read_from_file("output.txt")
    # Output text read from the file to the console
    output_text_to_console("Text read from file:\n" + file_content)

    # Read from a file using pandas
    # The function read_from_file_with_pandas assumes a CSV file for demonstration
    df = read_from_file_with_pandas("example.csv")
    # Display data from the file
    print("Data read from file using pandas:")
    print(df)

if __name__ == "__main__":
    main()