# Purpose:  Demonstrating splitting strings cleanly in Python 2

# Define the string we will be working with
test_string = "This is a test string"

# Main method
if __name__ == "__main__":
    # Print initial string
    print "The string we are starting with is:"
    print test_string
    # Remove the first letter
    print "We can remove the first letter and keep rest with [1:]"
    print test_string[1:]
    # Remove the last letter
    print "We can remove the last letter and keep rest with [:-1]"
    print test_string[:-1]
    # Split the string on " "
    print "We can split the string to smaller strings with the split command, define delimiter as \" \""
    print test_string.split(" ")
    # Split the string on "e"
    print "We can change what delimiter we use. Now using \"e\""
    print test_string.split("e")