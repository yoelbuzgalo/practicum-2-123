""" imports and constants should go here """

def array_to_integer (an_array, index=0, prev=0):
    """ Your solution goes here, see instructions for details """
    
    # Base case
    if index > (len(an_array)-1):
        return prev
    
    raised_value = prev + an_array[index] * (10**index) # Calculate the raised value

    return array_to_integer(an_array, index + 1, raised_value) # Call the next stack with next index + raised_value