# Program to understand the concept of Pool in multiprocessing

import multiprocessing
import os


def square(n):
    print(f"Worker process id for {n}: {os.getpid()}")
    return n * n


if __name__ == "__main__":

    # input list
    mylist = [1, 2, 3, 4, 5]

    # creating a pool object
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(square, mylist)

    print(result)
    print("Main process id:", os.getpid())
