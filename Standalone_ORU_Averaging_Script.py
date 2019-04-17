# Objective: Read ORU data from text files and filter transmittance values, then average values for each file and print
import os

# This variable should be set to the folder containing ORU text files, modify string accordingly.
path = r"C:\Users\cnduaguibe\Desktop\ORU_data"

# Searches the given directory and prints the name of any text files (ignoring other file types)
# Also iterates through the files and averages the ORU reading values from each file, then prints to shell
for file in os.listdir(path):
    with open(os.path.join(path, file)) as opened_file:
        if file.endswith((".log", ".txt")):
            print(file)
            ORU_reading_total = 0
            number_of_readings = 0
            # Since each file containing ORU read data isn't formatted the same, the for loop below locates the reading
            # value by finding the word "reading" which always precedes the actual value.
            # Also, since each file may contain different numbers of lines of text, the script adapts to this by adding
            # to the ORU_reading_total and number_of_readings variables as it reads each line in a file so the average
            # is always accurate.
            for line in opened_file:
                reading_location = line.find('"reading":')
                start = reading_location + 10
                end = start + 7
                sliced_line = line[start:end]
                ORU_reading_total += int(sliced_line)
                number_of_readings += 1
            # If a file is blank the script will print "File is blank." under the file name.
            # The additional print statement in the if/else statement below just separates each pair of printed lines
            if number_of_readings == 0:
                print("File is blank.")
                print()
            else:
                average_reading_value = ORU_reading_total / number_of_readings
                print("Average ORU reading value is: " + str(average_reading_value))
                print()
        else:
            continue