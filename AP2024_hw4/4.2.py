import time
import math
import concurrent.futures
import logging
import multiprocessing

logging.basicConfig(filename='integration.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate_with_executor(executor, func, a, b, n_jobs):
    futures = []
    with executor(max_workers=n_jobs) as pool:
        for i in range(n_jobs):
            start_time = time.time()
            future = pool.submit(integrate, func, a, b)
            end_time = time.time()
            futures.append(future)
        result = sum(future.result() for future in concurrent.futures.as_completed(futures))
        logging.info(f"{executor.__name__} with n_jobs={n_jobs}: {end_time - start_time} seconds")
    return result

def main():
    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = list(range(1, cpu_num * 2 + 1))

    thread_execution_times = {}
    process_execution_times = {}

    for n_jobs in n_jobs_list:
        # ThreadPoolExecutor
        start_time = time.time()
        integrate_with_executor(concurrent.futures.ThreadPoolExecutor, math.cos, 0, math.pi / 2, n_jobs)
        end_time = time.time()
        thread_execution_times[n_jobs] = end_time - start_time

        # ProcessPoolExecutor
        start_time = time.time()
        integrate_with_executor(concurrent.futures.ProcessPoolExecutor, math.cos, 0, math.pi / 2, n_jobs)
        end_time = time.time()
        process_execution_times[n_jobs] = end_time - start_time

    with open('execution_times_comparison.txt', 'w') as file:
        file.write("ThreadPoolExecutor execution times:\n")
        for n_jobs, execution_time in thread_execution_times.items():
            file.write(f"{n_jobs} workers: {execution_time} seconds\n")
        
        file.write("\nProcessPoolExecutor execution times:\n")
        for n_jobs, execution_time in process_execution_times.items():
            file.write(f"{n_jobs} workers: {execution_time} seconds\n")

if __name__ == "__main__":
    main()
