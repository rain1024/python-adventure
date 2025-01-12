import threading 
import time

def infinite_task():
    counter = 0
    while True:
        counter += 1
        print(f"Daemon Thread is running {counter}...")
        time.sleep(1)

def main():
    print("Main thread started")
    daemon_thread = threading.Thread(target=infinite_task)
    daemon_thread.daemon = True
    daemon_thread.start()
    time.sleep(3)
    print("Main thread finished")

if __name__ == "__main__":
    main()