# Purpose: Demonstrate insertion sort on a list

# Create an unsorted list. We could also read this from input
unsorted = [5,1,3,4,2,8]

# Insertion Sort function
def insertion_sort(items):
    # Position will be from 1 to length
    for pos in range (1, len(items)):
        # While we haven't fallen off the start of the list (if smallest item)
        # and we should swap the item with the item next to it
        while 0 < pos and items[pos] < items[pos - 1]:
            # Perform a swap of the items at [pos] and [pos-1]
            temp_item = items[pos]
            items[pos] = items[pos-1]
            items[pos-1] = temp_item
    # Return the sorted list
    return items
    
# Main method
if __name__ == "__main__":
    # Print the return values from insertion sort
    print insertion_sort(unsorted)