# Code from Python 2 Documentation
# Modification by Andrew Brandt

# Purpose: Demonstrate how to use Lock

# Import Process and Lock
from multiprocessing import Process, Lock

# printer_function_lock
# Purpose:  Print a number out to the console using Lock
# Returns:  void
def printer_function_lock(lock, number):
    # Lock the output to this process
    lock.acquire()
    # Print the number
    print number
    # Release the lock from this process
    lock.release()

if __name__ == '__main__':
    # Create the Lock on output
    lock = Lock()
    
    print "Now printing with the lock:"
    # Count to 10
    for iteration_number in range(10):
        # Print 1 to 10 using lock (these will be in order)
        Process(target=printer_function_lock, args=(lock, iteration_number)).start()