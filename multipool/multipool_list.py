# Imports
import multiprocessing
from multiprocessing import Lock
import time


NUMBER_ITERATIONS = 64


# count function
# Purpose:  Count from 1 to COUNT_TO_NUMBER
# Inputs:   lock - printing lock
#           job_id - the job id
# Returns:  void
def count(lock, job_id):
    while True:
        x = 1
        # While we are less than the COUNT_TO_NUMBER
        while x < 10000000:
            # Increment by 1
            x = x + 1
        # Acquire the lock to printing out
        lock.acquire()
        # Print that we have finished a count by printing job id
        print str(job_id)
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


if __name__ == '__main__':
    # Create the lock so the output will be clean
    lock = Lock()
    # Run the program using multiple cores
    multiple_cores(lock)