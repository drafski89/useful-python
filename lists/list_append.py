# Purpose:  Demonstrating list appending in Python 2

# Define the list we will be using
start_list = [0,1,2,3,4,5,6,7,8,9]

# Main method
if __name__ == "__main__":
    # Print the initial list
    print "The initial list is:"
    print start_list
    
    # Append a value onto the list
    print "Appending on \"10\""
    start_list.append(10)
    print start_list
    
    # Append another list on
    append_list = [1,2,3]
    print "Appending on a list: " + str(append_list)
    start_list.append(append_list)
    print start_list
    
    # Append each item onto the list, not the whole list
    print "Whoops, that appended the new list as only 1 item. Let's try that again"
    for item in range(len(append_list)):
        start_list.append(append_list[item])
    print start_list