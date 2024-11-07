#!/usr/bin/python3
    """
    Returns a list of attributes and methods of an object.

    This function uses the built-in dir() function to get a list of all 
    attributes and methods of the given object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: A list of strings representing the names of the attributes 
              and methods of the object.
    """

def lookup(obj):
    return dir(obj)
