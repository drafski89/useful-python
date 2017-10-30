# Purpose: Demonstrate basic bubble sort

# Create an unsorted list. We could also read this from input
unsorted = [5,1,3,4,2,8]

# Bubble Sort function
def bubble_sort(items):
    # Position will be from last item to first item (move right to left)
    for first_pos in range (len(items)-1, -1, -1):
        # Position will be from first item to the first_pos-1 items (move left to right)
        for second_pos in range (0, first_pos):
            # If the items are reversed, perform a swap
            if items[second_pos] > items[second_pos+1]:
                # Perform a swap of the items at [second_pos] and [second_pos-1]
                temp_item = items[second_pos]
                items[second_pos] = items[second_pos+1]
                items[second_pos+1] = temp_item
    return items

# Main method
if __name__ == "__main__":
    # Print the return values from bubble sort
    print bubble_sort(unsorted)