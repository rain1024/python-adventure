import threading
import time

def worker():
    print(f"Thread {threading.current_thread().name} starting")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()