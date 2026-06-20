### mmultiprocessing  with processpoolexecutor
from concurrent.futures import ProcessPoolExecutor
from time import time
import time
t=time.time()


def print_squares(number):
   time.sleep(1)
   return f"square:{number**2}"

numbers=[1,2,3,4,5]

if __name__ == '__main__':
   
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(print_squares, numbers)

    for result in results:
        print(result)
    print(f"finished in {time.time()-t} seconds")