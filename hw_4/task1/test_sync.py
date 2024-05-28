import time


from fib import fibonacci_of


if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        _ = fibonacci_of(30)
    end = time.time()
    print(f"Время синхронное: {end - start}")