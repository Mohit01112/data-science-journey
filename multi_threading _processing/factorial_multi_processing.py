'''
real worls example : multiprocessing for cpu-bound tasks
scenario :factorial calaculation
facytorial calcultaions,especially for large numbers, can be computationally intensive and time-consuming. By using multiprocessing, we can distribute the workload across multiple CPU cores, allowing for faster calculations and improved performance.
involve significant computational overhead, especially for large numbers. By using multiprocessing, we can distribute the workload across multiple CPU cores, allowing for faster calculations and improved performance.
.multiprocessing can be used to distribute the workload across multiple CPU cores, improving the performance.
'''

import multiprocessing
import math 
import sys
import time

## increase the maximum recursion limit to handle large factorial calculations
sys.set_int_max_str_digits(100000000)

## function to commpute factorials of a given number

def compute_factorial(number):
    print(f"Calculating factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':
    numbers = [10000, 20000, 30000, 40000, 50000]  

    start_time = time.time()

    ## create a process pool with the number of available CPU cores
    with multiprocessing.Pool() as Pool:
        results = Pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"results: {results}")
    print(f"Time taken : {end_time - start_time} seconds")
