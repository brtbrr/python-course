import time
import math
import concurrent.futures
import multiprocessing


def _integrate(f, a, b, n_iter):
    res = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        res += f(a + i * step) * step

    return res

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, type="proc"):
    bucket = (b - a) / n_jobs
    res = 0

    if type == "proc":
        executor_type = concurrent.futures.ProcessPoolExecutor
    elif type == "thread":
        executor_type = concurrent.futures.ThreadPoolExecutor
    else:
        raise NotImplementedError(f"executor type support only: proc, thread")
    
    with executor_type(max_workers=n_jobs) as executor:
        futures = [executor.submit(_integrate, f, a + i * bucket, a + (i+1) * bucket, n_iter // n_jobs) for i in range(n_jobs)]
        for future in concurrent.futures.as_completed(futures):
            res += future.result()

    return res

if __name__ == "__main__":
    num_cpus = multiprocessing.cpu_count()

    for executor_type in ["proc", "thread"]:
        for num_cpu in range(1, num_cpus * 2):
            start = time.time()
            res = integrate(math.cos, 0, math.pi / 2, n_jobs=num_cpu, type=executor_type)
            end = time.time()
            print(f"Время выполнения с executor_type: {executor_type}, num_cpu: {num_cpu} равно: {end - start}")