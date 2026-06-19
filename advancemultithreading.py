## multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1) 
    print(f"number: {number}")

numbers = [1, 2, 3, 4, 5,3,4,5,6,7,8,9,98765,4,23]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result) 