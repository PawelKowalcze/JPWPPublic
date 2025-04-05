import multiprocessing
import os

def child_process():
    print()
    # Dodaj kod tutaj


if __name__ == "__main__":
    process = multiprocessing.Process(target=child_process)
    process.start()  # Start the new process
    print(f"Działa proces macierzysty o PID: {os.getpid()}, utworzony proces: {process.pid}")
    process.join()  # Wait for the child process to finish