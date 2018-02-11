# Example to show basic parallelism using pool in Python 2
# 
# When NUMBER_CORES == 1 there will clearly be 1 core at 80% usage
# Other cores will also increase, but not nearly as much
# 
# When NUMBER_CORES == actual number of cores (non-hyperthreaded), all
# cores show as 100% usage

# Base multithreading code from Python 2 Documentation
# Modifications by Andrew Brandt

import multiprocessing
from multiprocessing import Pool
import time

COUNT_TO_NUMBER = 10000000

# count function
# Purpose: Count from 1 to COUNT_TO_NUMBER
# Returns: None
def count(x):
    # While we are less than the COUNT_TO_NUMBER
    while x < COUNT_TO_NUMBER:
        # Increment by 1
        x = x + 1

def constant_per_core_pool(output_file):
    output_file.write("ConstantPerCore\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant per run: " + str(run)
        NUMBER_CORES = run

        ITERATIONS_PER_CORE = 4

        NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE
        
        # Multiple cores
        multi_time_start = time.time()
        p = Pool(NUMBER_CORES)
        p.map(count,[1 for x in range (NUMBER_ITERATIONS)])
        multi_time_stop = time.time()

        # Single core
        single_time_start = time.time()
        for single_run in range(NUMBER_ITERATIONS):
            count(1)
        single_time_stop = time.time()
        
        # Calculate total time used in multi and single workloads
        multi_time_total = multi_time_stop - multi_time_start
        single_time_total = single_time_stop - single_time_start
        
        # Percentage Improvement = (Single - Parallel) / Single
        improvement = (single_time_total - multi_time_total) / single_time_total
        
        # Write the data to the file
        output_file.write("" + str(run) + "," + str(multi_time_total) + "," + str(single_time_total) + "," + str(improvement) + "\n")

def constant_total_pool(output_file):
    output_file.write("ConstantTotalIterations\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant Total, Run: " + str(run)
        NUMBER_CORES = run

        ITERATIONS_PER_CORE = 4

        #NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE
        # Constant total iterations
        NUMBER_ITERATIONS = 16
        
        # Multiple cores
        multi_time_start = time.time()
        p = Pool(NUMBER_CORES)
        p.map(count,[1 for x in range (0, NUMBER_ITERATIONS)])
        multi_time_stop = time.time()

        # Single core
        single_time_start = time.time()
        for single_run in range(NUMBER_ITERATIONS):
            count(1)
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
    with open("multipool_results.csv", "w") as output_file:
        output_file.write("CoreCount,ParallelTime,SerialTime,Improvement\n")
        constant_per_core_pool(output_file)
        constant_total_pool(output_file) 
    print "Complete!"