"Imports and constants should go here."
FILENAME = "question3.csv"

def find_suspect(filename,victim,weapon,room):
    """ Your solution goes here, see instructions for details """

def print_case (suspect,victim,weapon,room):
     """ Output helper function """
     print ("Suspect: ",suspect,", Victim: ",victim,", Weapon: ",weapon,", Room: ",room,sep="")

def main():
    """ Sample test cases, you will need to write more to fully test your code. This function 
        is not graded. """
    try:
         filename = "bad_file_name.csv"
         find_suspect(filename,"","","")
    except FileNotFoundError:
         print("Error:",filename," does not exist.")

    victim = "Evangeline Fairchild"
    weapon = "Trophy"
    room = "Kitchen"
    suspect = find_suspect(FILENAME, victim, weapon, room)
    print_case (suspect, victim, weapon, room)

    victim = "Bart Simpson"
    weapon = "Wet Noodle"
    room = "Treehouse"
    try:
        suspect = find_suspect (FILENAME, victim, weapon, room)
    except ValueError:
        print_case ("None", victim, weapon, room)

if __name__ == "__main__":
     main()