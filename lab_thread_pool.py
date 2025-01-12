import threading
import time
import os
from concurrent.futures import ThreadPoolExecutor

NUM_FILES = 30000
MAX_WORKERS = 3000

def read_file(filename):
    print(f"Thread {threading.current_thread().name} starting to read {filename}")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Simulate some processing time
            time.sleep(0.5)
            print(f"Thread {threading.current_thread().name} finished reading {filename}")
            print(f"File {filename} has {len(content)} characters")
    except FileNotFoundError:
        print(f"File {filename} not found")

# Create some sample files
def create_sample_files():
    for i in range(NUM_FILES):
        filename = f"sample_file_{i}.txt"
        with open(filename, 'w') as f:
            f.write(f"This is sample content for file {i}\n" * 100)

# Create sample files first
create_sample_files()

# List of files to read
files_to_read = [f"sample_file_{i}.txt" for i in range(NUM_FILES)]

# Wait for all threads to complete
thread_pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)

for filename in files_to_read:
    thread_pool.submit(read_file, filename)

thread_pool.shutdown(wait=True)

# Clean up the sample files
for filename in files_to_read:
    os.remove(filename)

print("All files have been processed and cleaned up") 