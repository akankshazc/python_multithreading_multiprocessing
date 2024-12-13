# program to demonstrate thread pooling

import concurrent.futures


def worker():
    print('Worker thread running')


# create a thread pool of 3 threads
pool = concurrent.futures.ThreadPoolExecutor(max_workers=3)

# submit tasks to the pool
for _ in range(3):
    pool.submit(worker)

# shutdown the pool
pool.shutdown()

print('Main thread still running')
