import time
import multiprocessing


from fib import fibonacci_of


if __name__ == "__main__":
    start = time.time()
    processes = [multiprocessing.Process(target=fibonacci_of, args=(30,)) for i in range(10)]
    for process in processes:
        process.start()
    for thread in processes:
        thread.join()
    end = time.time()
    print(f"Время с процессами: {end - start}")