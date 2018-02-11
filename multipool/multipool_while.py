# Example to show what happens if many workers in a pool get into a while-True loop
# The workers do not move onto the next jobs because they are stuck on the current jobs

import multiprocessing
import time


TOTAL_RUNS = 16
NUMBER_CORES = multiprocessing.cpu_count() * 2


def count():
    x = 1
    while x < 10000000:
        x += 1


def loop(job_id):
    while True:
        # Print out the job id so we know which thread we are in
        print 'The job id: ' + str(job_id)
        # Count just to delay and make the CPU work
        # time.sleep() would do the same thing but the CPU would not have to work
        count()


if __name__ == "__main__":
    p = multiprocessing.Pool(NUMBER_CORES)
    p.map(loop, [x for x in range(0, TOTAL_RUNS)])
