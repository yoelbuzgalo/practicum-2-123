"Imports and constants should go here."
FILENAME = "question3.csv"
import csv

def find_suspect(filename,victim,weapon,room):
    """ Your solution goes here, see instructions for details """
    try:
        with open(filename) as file:
            header = next(file) # Stores and skips the header line in the .csv file
            csv_reader = csv.reader(file) # Initializes csv reader to read the file and store in csv_reader variable
            # Iterate over the csv_reader, each line represents as a record
            for record in csv_reader:
                # If the victim, weapon and room parameters match the record's victim, weapon and room values; return its record's suspect value
                if record[1] == victim and record[2] == weapon and record[3] == room:
                    return record[0] # Return the suspect name
            else:
                # Otherwise raise a ValueError for the exception to handle the error
                raise ValueError()
    except FileNotFoundError:
        print(filename, "does not exist")
        return
    except ValueError:
        print("No suspect is found for the given victim, weapon and room")
        return
    

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