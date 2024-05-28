import multiprocessing
import time
import codecs
from datetime import datetime

def log_message(file, message):
    with open(file, 'a') as f:
        f.write(f"{datetime.now()} - {message}\n")

def process_A(input_queue, output_queue, log_file):
    while True:
        msg = input_queue.get()
        if msg == 'STOP':
            output_queue.put('STOP')
            log_message(log_file, "Process A received STOP signal.")
            break
        lower_msg = msg.lower()
        log_message(log_file, f"Process A received message: {msg}")
        log_message(log_file, f"Process A processed message to: {lower_msg}")
        time.sleep(5)
        output_queue.put(lower_msg)
        log_message(log_file, f"Process A sent message to Process B: {lower_msg}")

def process_B(input_queue, main_queue, log_file):
    while True:
        msg = input_queue.get()
        if msg == 'STOP':
            main_queue.put('STOP')
            log_message(log_file, "Process B received STOP signal.")
            break
        encoded_msg = codecs.encode(msg, 'rot_13')
        print(encoded_msg)
        log_message(log_file, f"Process B received message: {msg}")
        log_message(log_file, f"Process B encoded message to: {encoded_msg}")
        main_queue.put(encoded_msg)
        log_message(log_file, f"Process B sent message to Main Process: {encoded_msg}")

def main():
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    main_queue = multiprocessing.Queue()
    log_file = '/Users/olegzagorulko/vscode_work/python-course/hw_4/artifacts/task3.txt'

    proc_A = multiprocessing.Process(target=process_A, args=(input_queue, output_queue, log_file))
    proc_B = multiprocessing.Process(target=process_B, args=(output_queue, main_queue, log_file))

    proc_A.start()
    proc_B.start()

    try:
        while True:
            msg = input("Enter message: ")
            if msg == 'exit':
                input_queue.put('STOP')
                log_message(log_file, "Main Process sent STOP signal to Process A.")
                break
            input_queue.put(msg)
            log_message(log_file, f"Main Process received message: {msg}")
            log_message(log_file, f"Main Process sent message to Process A: {msg}")
    except KeyboardInterrupt:
        input_queue.put('STOP')
        log_message(log_file, "Main Process sent STOP signal to Process A due to KeyboardInterrupt.")

    proc_A.join()
    proc_B.join()

    while not main_queue.empty():
        received_msg = main_queue.get()
        log_message(log_file, f"Main Process received message from Process B: {received_msg}")
        print("Main process received:", received_msg)

if __name__ == '__main__':
    main()
