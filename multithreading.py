## multithreading
## when should we use multithreading?
## I/o-bound tasks,: tasks that spend a lot of time waiting for input/output operations to complete, such as reading/writing files, making network requests, or interacting with databases.
###concurrent execution of multiple threads can help improve the performance of I/O-bound tasks by allowing other threads to continue executing while one thread is waiting for an I/O operation to complete.
 
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2) # simulating a time-consuming I/O operation
        print(f"number: {i}")

def print_letters():
    for letter in"abcde":
        time.sleep(0) # simulating a time-consuming I/O operation
        print(f"letter: {letter}")


## create 2 threads

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)


t= time.time()
## start the threads 
thread1.start()
thread2.start()

## wait for the threads to finish 
thread1.join()
thread2.join()

finihed_time = time.time()-t
print(f"finished in {finihed_time} seconds")

