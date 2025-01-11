import threading
import time
import os

NUM_FILES = 3000

def read_file(filename):
    print(f"Thread {threading.current_thread().name} starting to read {filename}")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Simulate some processing time
            time.sleep(20)
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

# Create threads for each file
threads = []
for filename in files_to_read:
    thread = threading.Thread(target=read_file, args=(filename,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Clean up sample files
for filename in files_to_read:
    os.remove(filename)

print("All files have been processed and cleaned up") 