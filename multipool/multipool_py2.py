# Example to show basic parallelism using pool in Python 2
# 
# When NUMBER_CORES == 1 there will clearly be 1 core at 80% usage
# Other cores will also increase, but not nearly as much
# 
# When NUMBER_CORES == actual number of cores (non-hyperthreaded), all
# cores show as 100% usage

# Base multithreading code from Python 2 Documentation
# Modifications by Andrew Brandt

from multiprocessing import Pool
import time

# Constant number of (cores in machine)
# Set == 1 for single core performance
# Set == cores for maximum performance

# Laptop: 2
# Tower: 4
# Servers: 4-16, tucsan3 = 8
NUMBER_CORES = 16

# Constant number of loops performed per core
# Set higher number to show greater difference between multi and single
ITERATIONS_PER_CORE = 4

# Calculate the total number of iterations performed
# Example: 
# NUMBER_CORES = 2
# ITERATIONS_PER_CORE = 4
# NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE
# 8 = 2 * 4
NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE

# Constant for the count function to count to
# Higher number will show greater differences in multithreading
COUNT_TO_NUMBER = 10000000

# String to hold a divider
DIVIDER = "-----------------------------------------------"

# count function
# Purpose: Count from 1 to COUNT_TO_NUMBER
# Returns: None
def count(x):
    # While we are less than the COUNT_TO_NUMBER
    while x < COUNT_TO_NUMBER:
        # Increment by 1
        x = x + 1
    # Print that we have finished a count with a .
    print ".",
    # Print that we have finished a count with a message
    # print "Finished a count"
    
# Main function
if __name__ == '__main__':
    # Print that we are starting the system with the NUMBER_CORES
    print "\nStarting, using {0} cores.".format(NUMBER_CORES)
    
    # Print starting the multi processor work
    print "\nMultiple workers in pool\n" + DIVIDER
    # Store the start time value
    multiTimeStart = time.time()
    # Create a pool of workers same as NUMBER_CORES
    p = Pool(NUMBER_CORES)
    # Map each count function into the pool
    # Generate a list of 1's, NUMBER_ITERATIONS long
    p.map(count,[1 for x in range (0, NUMBER_ITERATIONS)])
    # Store the stop time value
    multiTimeStop = time.time()
    # Print that we have finished
    print "\nDone"
    
    # Print starting the single processor work
    print "\nSingle worker\n" + DIVIDER
    # Store the start time value
    singleTimeStart = time.time()
    # For loop to perform NUMBER_ITERATIONS counts
    for x in range(0, NUMBER_ITERATIONS):
        # Count from 1
        count(1)
    # Store the stop time value
    singleTimeStop = time.time()
    # Print that we have finished
    print "\nDone"
    
    # Calculate total time used in multi and single workloads
    multiTimeTotal = multiTimeStop - multiTimeStart
    singleTimeTotal = singleTimeStop - singleTimeStart
    
    # Print the results to the user
    print "\nCompleted!"
    print DIVIDER
    print "Multi time: ", multiTimeTotal
    print "Single time: ", singleTimeTotal
    print "\n"