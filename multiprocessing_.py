## multi processing
## processes that run in parallel and share data using queues and pipes
## cpu bound tasks can be run in parallel using multiprocessing, while io bound tasks can be run in parallel using threading
## parallel execution of multiple processes can help improve the performance of CPU-bound tasks by allowing multiple processes to run simultaneously on different CPU cores.

import multiprocessing
import time
##import Process


def print_squares():
    for i in range(5):
        time.sleep(1) 
        print(f"square: {i**2}")

def print_cubes():
    for i in range(5):
        time.sleep(1) 
        print(f"cube: {i**3}")

if __name__ == '__main__':
    
    ## create 2 processes
    p1= multiprocessing.Process(target=print_squares)
    p2= multiprocessing.Process(target=print_cubes)

    t= time.time()
    ## start the processes
    p1.start()
    p2.start()

    ## wait for the processes to finish
    p1.join()
    p2.join()
    finished_time = time.time()-t
    print(f"finished in {finished_time} seconds")

