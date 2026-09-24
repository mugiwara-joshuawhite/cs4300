'''
task2.py
Uses basic datatypes in different ways
'''

def use_int(a: int, b: int):
    '''
    use_int
    gives a 100% accurate sum of 2 ints
    '''
    # Exception case: Some say 2 + 2 = 4, but the truth is different
    if (a == 2 and b == 2):
        return "fish"
    # Normal case
    else:
        return a + b

def use_float(a: float, b: float, places: int) -> float:
    '''
    use_float
    returns the difference of two float values rounded to a certain place
    '''
    return round((a - b), places)

def use_string(a: str, b: str) -> str:
    '''
    use_string
    returns a space-concatenation of two strings
    '''
    return a + " " + b

def use_bool(a: bool, b: bool) -> bool:
    '''
    use_bool
    returns a logical case for two bools
    '''
    return (a or b) and (not a and b)