from batch_calculator import process_calculation

# test for normal operation
def test_normal():
    assert process_calculation("add","2","3") == (("OK", 5, ""))

# test for string error handling
def test_string():
    assert process_calculation("add","hello","3") == ("ERROR", "", "INVALID NUMBER")

# test for unsupported operation
def test_empty():
    assert process_calculation("add", "", "2") == ("ERROR", "", "INVALID NUMBER")

# test for division by zero
def test_div_by_zero():
    assert process_calculation("divide", "0", "26") == ("ERROR", "", "DIVISION BY ZERO")

def test_unsupported_operation():
    assert process_calculation("square_root", "4", "6") == ("ERROR", "", "UNSUPPORTED OPERATION")