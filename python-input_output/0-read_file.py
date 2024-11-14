#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to an empty string, which can be set
                        to a valid file path by the caller.

    Behavior:
        - Opens the specified file in read mode with UTF-8 encoding.
        - Reads and prints the entire content of the file to stdout.
        - Uses the `with` statement to ensure the file is closed automatically.
        - Does not handle file permission issues or missing file errors.

    Example:
        >>> read_file("example.txt")
        (Prints the content of "example.txt" to stdout)

    Note:
        This function assumes the file exists and is accessible with read permissions.
        It also assumes UTF-8 encoding for the text file.

    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
