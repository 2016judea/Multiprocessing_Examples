from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
from multiprocessing import Lock

#create a pool
#pool = ProcessPool(8)
pool = ThreadPool(4)
global points
points = []
global lock
lock = Lock()

#lock function to synchronize the points variable
def get_points(lock):
    with lock:
        return points

#the function being concurrently ran with global var protection
def some_function(arg1, arg2):
    print("arg1 is: " + str(arg1))
    print("arg1 is: " + str(arg2))
    point = 500
    get_points(lock).append(point)

#run function as concurrent threads
pool.apply_async(some_function(135, 12))
pool.apply_async(some_function(14, 122))
