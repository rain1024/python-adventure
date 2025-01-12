import queue
import threading
import time

def producer(q):
    for i in range(50):
        q.put(i)
        print(f"Produced {i}")
        time.sleep(0.1)
    print("Producer done")

def consumer(q):
    while True:
        try:
            item = q.get()
            print(f"Consumed {item}")
            time.sleep(0.2)
            q.task_done()
        except:
            break
    print("Consumer done")

def main():
    q = queue.Queue(maxsize=10)
    thread_producer = threading.Thread(target=producer, args=(q,))
    thread_consumer = threading.Thread(target=consumer, args=(q,), daemon=True)
    
    thread_producer.start()
    thread_consumer.start()
    
    # Wait for all tasks to be processed
    q.join()
    print("All tasks completed")

if __name__ == "__main__":
    main()