# Purpose: Demonstrate basic file handling with Python 2

# Declare the input and output file names (same directory)
# Note: Possible to declare the full path if reading from another directory
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

# Open the input file as "r" reading
with open(INPUT_FILE_NAME, "r") as input_file:
    # Print successful opening
    print "\nWe have opened the input file: " + INPUT_FILE_NAME
    
    # Open the output file as "w" writing
    # Also possible to open file as "a" append
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        # Print successful opening
        print "We have opened the output file: " + OUTPUT_FILE_NAME + "\n"
        
        # For each line in the input file
        # The count is the current line count
        for count, line in enumerate(input_file):
            # Print the line count and the line read from the input file
            print "The line count is: " + str(count)
            print "The raw line read in is: " + line
            # The line read in will have a trailing new line character
            # To remove, perform a strip
            line = line.strip()
            # Print the stripped line
            print "The strip line read in is: " + line
            # Write the line read to the output file
            output_file.write(line)
            # Print successful writing to the output file
            print "Wrote the line to the output file. \n"

# No need to exit the files
# Python will handle closing the files correctly
print "Program complete!\n"            