import arrays

def create_ascii_array (a_string):
    """ Your solution goes here, see instructions for details """
    
    an_array = arrays.Array(len(a_string), "") # Initializes an array with a length of the string and a prototype of empty strings

    # iterates over an array and assigns for each index the ASCII value of the same index character in a string
    for index in range(len(an_array)):
        # Convert character to an integer ASCII value and assign it to array at its given index
        an_array[index] = ord(a_string[index])
    return an_array # Returns the array value after iteration is done

def main ():
    """ You may add other ad-hoc tests here, this will not be graded """
    print (create_ascii_array("Dog"))
    print(create_ascii_array("ABC"))

if __name__ == "__main__":
    main ()