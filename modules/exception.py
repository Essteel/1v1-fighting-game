""" Custom exception classes for python stret fight game

Classes
-------
RangeError
InputError
"""

class RangeError(Exception):
    """ Subclass of Exception which checks if user input is between 1-4 """

class InputError(Exception):
    """ Subclass of Exception checks if user input is 'q' or 'a' """
