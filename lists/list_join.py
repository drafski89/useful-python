# Purpose:  Demonstrating list combining in Python 2

# Define the list we will be using
start_list = [0,1,2,3,4,5,6,7,8,9]

# Main method
if __name__ == "__main__":
    # Print the initial list
    print "The initial list is:"
    print start_list
    
    # Convert all items to strings from ints
    print "Convert all items in list to a string instead of ints"
    for item in range(len(start_list)):
        start_list[item] = str(start_list[item])
    
    # Create a string with no spaces
    print "Convert list to string with no spaces"
    print "".join(start_list)
    
    # Create a string with spaces
    print "Convert list to string with spaces between values"
    print " ".join(start_list)
    