from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool

def some_function(num):
    print(str(num**2) + '\n')

def run_threadpool(list_of_args, threads):
    pool = ThreadPool(threads)
    #pass the function that we will be multithreading along with args per thread
    results = pool.map(some_function, list_of_args)
    pool.close()
    #complete the process with join
    pool.join()
    return results

def run_processpool(list_of_args, threads):
    pool = ProcessPool(threads)
    #pass the function that we will be multiprocessing along with args per process
    results = pool.map(some_function, list_of_args)
    pool.close()
    #complete the process with join
    pool.join()
    return results

run_threadpool([3, 4, 5], threads=4)
run_processpool([5, 6, 7], threads=4)
