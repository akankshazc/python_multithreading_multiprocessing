# Program to illustrate communication between processes using queue

import multiprocessing


def square_list(mylist, q):
    """
    function to square a given list
    """
    # append squares of mylist to queue
    for num in mylist:
        q.put(num * num)


def print_queue(q):
    """
    function to print queue elements
    """
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    # input list
    mylist = [1, 2, 3, 4, 5]

    # creating a queue
    q = multiprocessing.Queue()

    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes finish
    p1.join()
    p2.join()

    # both processes finished
    print("Done!")
