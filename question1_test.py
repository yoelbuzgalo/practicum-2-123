from question1 import *

"""
Note: the analyze step converts the returned array (actual) to a string and is
compared to the expected which is the string representation of an array.
String are only used for the analyze step.  To be clear, your function should
return an array.                                                
"""
def test_empty_string():
    # setup
    a_string = ""
    expected = "[]"

    # invoke
    actual = create_ascii_array (a_string)

    # analyze
    assert str(actual) == expected

def test_one_char_string():
    # setup
    a_string = "a"
    expected = "[97]"

    # invoke
    actual = create_ascii_array (a_string)

    # analyze
    assert str(actual) == expected

def test_long_string():
    # setup
    a_string = "Go Tigers!"
    expected = "[71, 111, 32, 84, 105, 103, 101, 114, 115, 33]"

    # invoke
    actual = create_ascii_array (a_string)

    # analyze
    assert str(actual) == expected