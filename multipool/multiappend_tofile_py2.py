#!/usr/bin/env python

# Imports
import multiprocessing
from multiprocessing import Lock
import time

OUTPUT_FILE_NAME = "multiappend_results"

# Constant for the count function to count to
# Higher number will show greater differences in multithreading
COUNT_TO_NUMBER = 10000000

# count function
# Purpose:  Count from 1 to COUNT_TO_NUMBER
# Inputs:   None
# Returns:  void
def count():
    x = 1
    # While we are less than the COUNT_TO_NUMBER
    while x < COUNT_TO_NUMBER:
        # Increment by 1
        x = x + 1

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
# Inputs:   NUMBER_ITERATIONS - Total number of iterations to perform
# Returns:  void
def multiple_cores(NUMBER_ITERATIONS):
    jobs_local = []
    # For each job in the total number of iterations we will run
    for job_count in range (NUMBER_ITERATIONS):
        # Hand off the job id into the counting method
        next_process = multiprocessing.Process(target=count)
        # Start the job in the queue
        next_process.start()
        # Append it to the queue to be processed
        jobs_local.append(next_process)
    # While the last job is alive (so while we still have counts to run)
    # Infinite loop as long as the last job has not completed yet
    while check_processes(jobs_local):
        time.sleep(0.01)
        pass

# single_core function
# Purpose:  Start a counter in a single core many times iteratively
# Inputs:   NUMBER_ITERATIONS - Total number of iterations to perform
# Returns:  void
def single_core(NUMBER_ITERATIONS):
    # For loop to perform NUMBER_ITERATIONS counts
    for x in range(0, NUMBER_ITERATIONS):
        # Count from 1
        count()

def constant_per_core():
    # Open the output file
    with open(OUTPUT_FILE_NAME + "_constant_per_core.csv", "w") as output_file:
        output_file.write("CoreCount,ParallelTime,SerialTime,Improvement\n")
        for run in range(1, multiprocessing.cpu_count()+1):
            print "Constant per run: " + str(run)
            NUMBER_CORES = run

            ITERATIONS_PER_CORE = 4

            NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE
            
            # Multiple cores
            multi_time_start = time.time()
            multiple_cores(NUMBER_ITERATIONS)
            multi_time_stop = time.time()

            # Single core
            single_time_start = time.time()
            single_core(NUMBER_ITERATIONS)
            single_time_stop = time.time()
            
            # Calculate total time used in multi and single workloads
            multi_time_total = multi_time_stop - multi_time_start
            single_time_total = single_time_stop - single_time_start
            
            # Percentage Improvement = (Single - Parallel) / Single
            improvement = (single_time_total - multi_time_total) / single_time_total
            
            # Write the data to the file
            output_file.write("" + str(run) + "," + str(multi_time_total) + "," + str(single_time_total) + "," + str(improvement) + "\n")

def constant_total():
    # Open the output file
    with open(OUTPUT_FILE_NAME + "_constant_total.csv", "w") as output_file:
        output_file.write("CoreCount,ParallelTime,SerialTime,Improvement\n")
        for run in range(1, multiprocessing.cpu_count()+1):
            print "Constant Total, Run: " + str(run)

            NUMBER_ITERATIONS = 16
            
            # Multiple cores
            multi_time_start = time.time()
            multiple_cores(NUMBER_ITERATIONS)
            multi_time_stop = time.time()

            # Single core
            single_time_start = time.time()
            single_core(NUMBER_ITERATIONS)
            single_time_stop = time.time()
            
            # Calculate total time used in multi and single workloads
            multi_time_total = multi_time_stop - multi_time_start
            single_time_total = single_time_stop - single_time_start
            
            # Percentage Improvement = (Single - Parallel) / Single
            improvement = (single_time_total - multi_time_total) / single_time_total
            
            # Write the data to the file
            output_file.write("" + str(run) + "," + str(multi_time_total) + "," + str(single_time_total) + "," + str(improvement) + "\n")

# Main function
if __name__ == '__main__':
    constant_per_core()
    constant_total()
    print "Completed!"