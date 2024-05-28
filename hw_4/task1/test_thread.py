import time
import threading


from fib import fibonacci_of


if __name__ == "__main__":
    start = time.time()
    threads = [threading.Thread(target=fibonacci_of, args=(30,)) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"Время с потоками: {end - start}")