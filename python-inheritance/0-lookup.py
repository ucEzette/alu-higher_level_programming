def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    This function retrieves a list of the attributes and methods associated 
    with the provided object using the built-in `dir()` function. This list 
    includes all the properties (both data and methods) that belong to the 
    object, including special methods (those prefixed and suffixed with '__').

    Args:
        obj: The object whose attributes and methods are to be returned.

    Returns:
        list: A list of strings representing the names of the attributes 
              and methods of the object.
    """
    return dir(obj)
