import threading
import time
import random
def worker():
    print(f"Thread {threading.current_thread().name} starting")
    for i in range(10):
        print(f"Thread {threading.current_thread().name} is running {i}")
        time.sleep(random.uniform(0.1, 0.5))
    print(f"Thread {threading.current_thread().name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# print the end of the program
print(f"Main thread {threading.current_thread().name} finished")