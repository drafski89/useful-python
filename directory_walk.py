# Purpose:  Demonstrate how to walk through a directory in Python 2

# Import the operating system library
from os import walk

if __name__ == "__main__":
    # We will walk through each directory recursively
    # All this is handled in the for loop
    # root:         String holding the root of the walk
    # directory:    List of all directories inside the root
    # file:         List of all files in the current root directory
    # Start at .\  (Current location of this script)
    for root, directory, files in walk('.'):
        # Print a divider for readability
        print "--------------------"
        # Print the current working root directory
        print "The root is: \t\t\t" + str(root)
        # Print all directories in the current root directory
        print "Directories in root are: \t" + str(directory)
        # Print all the files in the current root directory
        print "The files are: \t\t\t" + str(files)
        # Print a new line for readability
        print "\n"