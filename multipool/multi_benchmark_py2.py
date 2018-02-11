import multiprocessing
import time

ITERATIONS_PER_CORE = 4
CONSTANT_ITERATIONS = ITERATIONS_PER_CORE * multiprocessing.cpu_count()
COUNT_TO_NUMBER = 10000000

def count(x):
    x = 1
    # While we are less than the COUNT_TO_NUMBER
    while x < COUNT_TO_NUMBER:
        # Increment by 1
        x = x + 1

def constant_per_core_pool(output_file):
    output_file.write("Constant_Core_Iterations_Pool\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant Core Pool, Run: " + str(run)
        NUMBER_CORES = run

        NUMBER_ITERATIONS = NUMBER_CORES * ITERATIONS_PER_CORE
        
        # Multiple cores
        multi_time_start = time.time()
        p = multiprocessing.Pool(NUMBER_CORES)
        p.map(count, [1 for x in range (0, CONSTANT_ITERATIONS)])
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
    output_file.write("Constant_Total_Iterations_Pool\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant Total Pool, Run: " + str(run)
        NUMBER_CORES = run
        
        # Multiple cores
        multi_time_start = time.time()
        p = multiprocessing.Pool(NUMBER_CORES)
        p.map(count,[1 for x in range (0, CONSTANT_ITERATIONS)])
        multi_time_stop = time.time()

        # Single core
        single_time_start = time.time()
        for single_run in range(CONSTANT_ITERATIONS):
            count(1)
        single_time_stop = time.time()
        
        # Calculate total time used in multi and single workloads
        multi_time_total = multi_time_stop - multi_time_start
        single_time_total = single_time_stop - single_time_start
        
        # Percentage Improvement = (Single - Parallel) / Single
        improvement = (single_time_total - multi_time_total) / single_time_total
        
        # Write the data to the file
        output_file.write("" + str(run) + "," + str(multi_time_total) + "," + str(single_time_total) + "," + str(improvement) + "\n")

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
        next_process = multiprocessing.Process(target=count, args=(job_count,))
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
        count(1)

def constant_per_core_list(output_file):
    # Open the output file
    output_file.write("Constant_Core_Iterations_List\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant Core List, Run: " + str(run)
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

def constant_total_list(output_file):
    output_file.write("Constant_Total_Iterations_List\n")
    for run in range(1, multiprocessing.cpu_count()+1):
        print "Constant Total List, Run: " + str(run)

        # Multiple cores
        multi_time_start = time.time()
        multiple_cores(CONSTANT_ITERATIONS)
        multi_time_stop = time.time()

        # Single core
        single_time_start = time.time()
        single_core(CONSTANT_ITERATIONS)
        single_time_stop = time.time()
        
        # Calculate total time used in multi and single workloads
        multi_time_total = multi_time_stop - multi_time_start
        single_time_total = single_time_stop - single_time_start
        
        # Percentage Improvement = (Single - Parallel) / Single
        improvement = (single_time_total - multi_time_total) / single_time_total
        
        # Write the data to the file
        output_file.write("" + str(run) + "," + str(multi_time_total) + "," + str(single_time_total) + "," + str(improvement) + "\n")
        
if __name__ == '__main__':
    with open("multi_results.csv", "w") as output_file:
        output_file.write("CoreCount,ParallelTime,SerialTime,Improvement\n")
        constant_per_core_pool(output_file)
        constant_total_pool(output_file)
        constant_per_core_list(output_file)
        constant_total_list(output_file)
    print "Complete!"