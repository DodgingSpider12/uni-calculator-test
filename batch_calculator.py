"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):

    status = "OK"
    result = ""
    error_code = ""

    # check if no numbers have been entered, and return error if that is so
    if ((a_text == "") or (b_text == "")):
        status = "ERROR"
        result = ""
        error_code = "INVALID NUMBER"

        return (status, result, error_code)

    # check if number is a string or not
    for i in range (0, len(a_text) -1):
        if a_text[i].isalpha() == True:
            status = "ERROR"
            result = ""
            error_code = "INVALID NUMBER"

            return (status, result, error_code)

    for i in range (0, len(b_text)-1):
        if b_text[i].isalpha() == True:
            status = "ERROR"
            result = ""
            error_code = "INVALID NUMBER"  

            return (status, result, error_code)      
    
    # convert number strings into integers
    numA = float(a_text.strip())
    numB = float(b_text.strip())



    # call correct function for each different operation
    if operation == "add":
        result = add(numA,numB)
        status = "OK"

    elif operation == "subtract":   
        result = subtract(numA, numB)
        status = "OK"

    elif operation == "multiply":
        result = multiply(numA, numB)
        status = "OK"

    elif operation == "divide":
        # check for division by 0, and return error if it is the case
        if (numA == 0) or (numB == 0):
            result == ""
            error_code = "DIVISION BY ZERO"
            status = "ERROR"

            return (status, result, error_code)
        
        else:
            result = divide(numA, numB)
            status = "OK"

    # return error if unsupported operation is used
    else:
        status = "ERROR"
        result = ""
        error_code = "UNSUPPORTED OPERATION"

    return (status, result, error_code)

    
    

    
    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
    raise NotImplementedError("Complete process_calculation for the coursework")
