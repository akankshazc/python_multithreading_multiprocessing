# Program to show the usage of Server processes

import multiprocessing


def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))


def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")


if __name__ == "__main__":
    # creating a server process
    with multiprocessing.Manager() as manager:

        # creating a list in server process memory
        records = manager.list([('Harry', 10), ('Ron', 9), ('Hermoine', 8)])

        # new record to be inserted
        new_record = ('Ginny', 7)

        # creating new processes
        p1 = multiprocessing.Process(
            target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(
            target=print_records, args=(records,))

        # running processes
        p1.start()
        p2.start()

        # wait until processes are finished
        p1.join()
        p2.join()

        # print records list
        print("Records: ", records)
