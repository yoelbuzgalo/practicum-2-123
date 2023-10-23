"""
A unit test provded to verify that the implementation of the array_to_integer
function is working correctly for at least some test cases.

Additional test cases will be used when grading the function.
"""

from question2 import *
import arrays

def test_array_to_integer_empty():
    # setup
    an_array = arrays.Array(0)
    expected = None

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual

def test_array_to_integer_9():
    # setup
    an_array = arrays.Array(1)
    an_array[0] = 9
    expected = 9

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual

def test_array_to_integer_12436():
    # setup
    an_array = arrays.Array(5)
    an_array[0] = 6
    an_array[1] = 3
    an_array[2] = 4
    an_array[3] = 2
    an_array[4] = 1
    expected = 12346

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual



# additional grading tests - do not provide to students
def test_array_to_integer_57():
    # setup
    an_array = arrays.Array(2)
    an_array[0] = 7
    an_array[1] = 5
    expected = 57

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual

def test_array_to_integer_000():
    # setup
    an_array = arrays.Array(3)
    an_array[0] = 0
    an_array[1] = 0
    an_array[2] = 0
    expected = 0

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual

def test_array_to_integer_1234567890():
    # setup
    an_array = arrays.Array(11)
    an_array[0]  = 0
    an_array[1]  = 9
    an_array[2]  = 8
    an_array[3]  = 7
    an_array[4]  = 6
    an_array[5]  = 5
    an_array[6]  = 4
    an_array[7]  = 3
    an_array[8]  = 2
    an_array[9]  = 1
    an_array[10] = 0
    expected = 1234567890

    # invoke
    actual = array_to_integer(an_array)

    # analyze
    expected == actual
