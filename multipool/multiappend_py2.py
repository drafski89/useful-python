#!/usr/bin/env python

# Purpose:  Demonstrate correct way to use multiprocessing in Python2
#           Show how to append jobs into a list so they can all be tracked
#           Different from creating a pool of workers

# Imports
import multiprocessing
from multiprocessing import Lock
import time

# Constant number of (cores in machine
# Set == 1 for single core performance
# Set == cores for maximum performance
# No performance difference between actual and hyperthreaded core count

# Laptops: 2 cores, 4 threads
# Desktops: 4 cores, 8 threads
# Servers: 4 - 16 cores, 8 - 32 threads
# tucsan3 = 8 cores, 16 threads
# Explicitly declare number of cores to use
NUMBER_CORES = 8
# Use max number of cores (from system count)
# NUMBER_CORES = multiprocessing.cpu_count()

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
# Purpose:  Count from 1 to COUNT_TO_NUMBER
# Inputs:   lock - printing lock
#           job_id - the job id
# Returns:  void
def count(lock, job_id):
    x = 1
    # While we are less than the COUNT_TO_NUMBER
    while x < COUNT_TO_NUMBER:
        # Increment by 1
        x = x + 1
    # Acquire the lock to printing out
    lock.acquire()
    # Print that we have finished a count by printing job id
    # print str(job_id)
    # Print that we have finished a count with a message
    # print "Finished a count"
    # Relese the lock
    lock.release()

# check_processes function
# Purpose:  Check to see if any jobs in a list are alive
# Inputs:   list_of_jobs - List of jobs created
# Returns:  True if any job is alive, otherwise False
def check_processes(list_of_jobs):
    # For each job in the list of jobs
    for job in list_of_jobs:
        # If this job is alive, return True
        if job.is_alive():
            return True
    # We have checked all jobs, none alive, return False
    return False

# multiple_cores function
# Purpose:  Start many counters in different cores
# Inputs:   lock - the output print lock
# Returns:  void
def multiple_cores(lock):
    jobs_local = []
    # For each job in the total number of iterations we will run
    for job_count in range (NUMBER_ITERATIONS):
        # Hand off the job id into the counting method
        next_process = multiprocessing.Process(target=count, args=(lock,job_count))
        # Start the job in the queue
        next_process.start()
        # Append it to the queue to be processed
        jobs_local.append(next_process)
    # While the last job is alive (so while we still have counts to run)
    # Infinite loop as long as the last job has not completed yet
    # counter = 0
    while check_processes(jobs_local):
        # counter += 1
        # print counter
        time.sleep(0.01)
        pass

# single_core function
# Purpose:  Start a counter in a single core many times iteratively
# Inputs:   lock - the output print lock
# Returns:  void
def single_core(lock):
    # For loop to perform NUMBER_ITERATIONS counts
    for x in range(0, NUMBER_ITERATIONS):
        # Count from 1
        count(lock, x)
      
# Main function
if __name__ == '__main__':
    # List to hold all parallel jobs we will run
    jobs = []
    # Create the lock so the output will be clean
    lock = Lock()
    
    # Print starting the multi processor work
    print "\nMultiple workers in pool\n" + DIVIDER
    # Store the start time value
    multi_time_start = time.time()
    # Run the program using multiple cores
    multiple_cores(lock)
    # Store the stop time value
    multi_time_stop = time.time()
    # Print that we have finished
    print "\nParallel - Done"
    
    # Print starting the single processor work
    print "\nSingle worker\n" + DIVIDER
    # Store the start time value
    single_time_start = time.time()
    # Run the program using a single core
    single_core(lock)
    # Store the stop time value
    single_time_stop = time.time()
    # Print that we have finished
    print "\nSerial - Done"
    
    # Calculate total time used in multi and single workloads
    multi_time_total = multi_time_stop - multi_time_start
    single_time_total = single_time_stop - single_time_start
    
    # Print the results to the user
    print "\nCompleted!"
    print DIVIDER
    print "Multi time: ", multi_time_total
    print "Single time: ", single_time_total
    print "\n"