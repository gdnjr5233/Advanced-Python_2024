import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_threading(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    return end_time - start_time

def run_multiprocessing(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    return end_time - start_time

def run_synchronous(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n = 35
    threading_time = run_threading(n)
    multiprocessing_time = run_multiprocessing(n)
    synchronous_time = run_synchronous(n)

    with open("results.txt", "w") as file:
        file.write("Threading -> {:.4f} seconds\n".format(threading_time))
        file.write("Multiprocessing -> {:.4f} seconds\n".format(multiprocessing_time))
        file.write("Synchronous -> {:.4f} seconds\n".format(synchronous_time))