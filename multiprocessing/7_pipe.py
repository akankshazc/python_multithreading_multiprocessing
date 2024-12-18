# Program to demonstrate communication between processes using a pipe

import multiprocessing


def sender(conn, msgs):
    """
    function to send messages to other end of pipe
    """
    for msg in msgs:
        conn.send(msg)
        print(f"Sent the message: {msg}")
    conn.close()


def receiver(conn):
    """
    function to receive messages from other
    end of pipe
    """
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print(f"Received the message: {msg}")


if __name__ == "__main__":

    # messages to be sent
    msgs = ["Protego", "Wingardium Leviosa", "Expelliarmus", "END"]

    # creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # running processes
    p1.start()
    p2.start()

    # wait until processes finish
    p1.join()
    p2.join()
