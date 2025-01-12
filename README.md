# Python Adventure

## Concurrent

Lập trình đồng thời (Concurrent Programming) là khả năng của một chương trình thực hiện nhiều tác vụ song song với nhau. Trong môi trường đa nhiệm hiện đại, lập trình đồng thời giúp tận dụng tối đa tài nguyên phần cứng và cải thiện hiệu suất của ứng dụng.

Có hai cách tiếp cận chính trong lập trình đồng thời:

1. **Parallelism (Song song)**: Thực sự chạy nhiều tác vụ cùng một lúc trên các CPU khác nhau.
2. **Concurrency (Đồng thời)**: Quản lý nhiều tác vụ cùng lúc, nhưng không nhất thiết phải chạy đồng thời về mặt vật lý.

```mermaid
flowchart LR
    subgraph Parallelism
        direction TB
        A1[Task 1] --> B1[CPU 1]
        A2[Task 2] --> B2[CPU 2]
        A3[Task 3] --> B3[CPU 3]
        A4[Task 4] --> B4[CPU 4]
    end
    
    subgraph Concurrency
        direction TB
        C1[Task 1] --> D[CPU]
        C2[Task 2] --> D
        C3[Task 3] --> D
        C4[Task 4] --> D
    end

    style A1 fill:#ef4444,color:white
    style A2 fill:#f97316,color:white
    style A3 fill:#eab308,color:white
    style A4 fill:#22c55e,color:white
    
    style B1 fill:#2563eb,color:white
    style B2 fill:#2563eb,color:white
    style B3 fill:#2563eb,color:white
    style B4 fill:#2563eb,color:white
    
    style C1 fill:#ef4444,color:white
    style C2 fill:#f97316,color:white
    style C3 fill:#eab308,color:white
    style C4 fill:#22c55e,color:white
    
    style D fill:#2563eb,color:white
```

Trong Python, có một số cơ chế để thực hiện lập trình đồng thời:

- **Threading**: Sử dụng nhiều luồng trong cùng một process
- **Multiprocessing**: Sử dụng nhiều process độc lập
- **Asynchronous I/O**: Sử dụng coroutines và event loop
- **Thread Pool/Process Pool**: Quản lý và tái sử dụng một nhóm worker threads/processes

Mỗi cơ chế có ưu nhược điểm riêng và phù hợp với các loại tác vụ khác nhau:

- Threading phù hợp với I/O-bound tasks
- Multiprocessing phù hợp với CPU-bound tasks
- Async I/O phù hợp với network I/O và high-concurrency

Process (Tiến trình) và Thread (Luồng) là hai khái niệm cơ bản trong lập trình đồng thời. Process là một chương trình đang chạy trên hệ điều hành, nó có không gian bộ nhớ riêng biệt và độc lập. Mỗi process có thể chứa nhiều thread, và các thread trong cùng một process chia sẻ tài nguyên và không gian bộ nhớ với nhau.

```mermaid
flowchart TD
    subgraph Process
        direction TB
        H[Heap Memory<br>Shared between threads]
        
        subgraph T1[Thread 1]
            S1[Stack Memory]
            R1[Registers]
        end
        
        subgraph T2[Thread 2]
            S2[Stack Memory]
            R2[Registers]
        end
        
        subgraph T3[Thread 3]
            S3[Stack Memory]
            R3[Registers]
        end
        
        T1 --> H
        T2 --> H
        T3 --> H
    end
    
    style H fill:#2563eb,color:white
    style T1 fill:#ef4444,color:white
    style T2 fill:#f97316,color:white
    style T3 fill:#22c55e,color:white
    style S1 fill:#ef4444,color:white
    style S2 fill:#f97316,color:white
    style S3 fill:#22c55e,color:white
    style R1 fill:#ef4444,color:white
    style R2 fill:#f97316,color:white
    style R3 fill:#22c55e,color:white
```

Mỗi thread có vùng nhớ stack (ngăn xếp) và register (thanh ghi) riêng để lưu trữ các biến cục bộ và thông tin thực thi, trong khi tất cả các thread trong cùng một process đều chia sẻ vùng nhớ heap chung. Điều này cho phép các thread có thể dễ dàng trao đổi dữ liệu với nhau, nhưng cũng đồng thời đòi hỏi cơ chế đồng bộ hóa phù hợp để tránh xung đột khi truy cập dữ liệu đồng thời.

![Thread and Process](./thread_and_process/thread_and_process.svg)

Trong Python, việc sử dụng thread bị giới hạn bởi Global Interpreter Lock (GIL), khiến cho tại một thời điểm chỉ có một thread có thể thực thi mã Python. Vì vậy, thread trong Python thường được sử dụng cho các tác vụ I/O-bound (như đọc/ghi file, gọi API), trong khi process thường được dùng cho các tác vụ CPU-bound (như tính toán phức tạp) để tận dụng được sức mạnh của nhiều CPU.

Python cung cấp một số cách để thực hiện lập trình đồng thời (concurrent programming):

## Threading

Python hỗ trợ đa luồng thông qua module `threading`. Threading phù hợp cho các tác vụ I/O-bound:

- **Global Interpreter Lock (GIL)**: Python có GIL, một cơ chế khóa cho phép chỉ một luồng thực thi tại một thời điểm trong interpreter. Điều này ảnh hưởng đến hiệu suất của các tác vụ CPU-bound.
- **Ưu điểm**: Dễ chia sẻ dữ liệu giữa các luồng, tiêu tốn ít tài nguyên.
- **Nhược điểm**: Không tận dụng được nhiều CPU do GIL.
- **Ứng dụng**: Phù hợp cho các tác vụ I/O như đọc/ghi file, gọi API, truy cập database.

Ví dụ cơ bản về threading:

```python
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
```

## Threading IO

Thread được tạo (fork) thông qua `threading.Thread()` và khởi động bằng `start()`, cho phép chương trình chạy nhiều tác vụ đồng thời. Mỗi thread sẽ thực thi công việc của riêng nó một cách độc lập với các thread khác. Sau khi tạo và khởi động các thread, chương trình sử dụng `join()` để đợi tất cả các thread hoàn thành trước khi tiếp tục thực thi.


```mermaid
flowchart TD
    A[Start] --> D[Create Threads]
    D --> E{For each thread}
    E --> F[Thread 1]
    E --> G[Thread 2]
    E --> H[Thread ...]
    E --> I[Thread N]
    
    F --> L1[Process]
    G --> L2[Process]
    H --> L3[Process]
    I --> L4[Process]
    
    L1 --> M[Join/Wait threads]
    L2 --> M
    L3 --> M
    L4 --> M
    
    M --> O[End]

    style A fill:#2563eb,stroke:#1d4ed8,color:#ffffff
    style D fill:#3b82f6,stroke:#2563eb,color:#ffffff
    style E fill:#60a5fa,stroke:#3b82f6,color:#1e3a8a
    style F fill:#ef4444,stroke:#dc2626,color:#ffffff
    style G fill:#f97316,stroke:#ea580c,color:#ffffff
    style H fill:#eab308,stroke:#ca8a04,color:#ffffff
    style I fill:#22c55e,stroke:#16a34a,color:#ffffff
    style L1 fill:#ef4444,stroke:#dc2626,color:#ffffff
    style L2 fill:#f97316,stroke:#ea580c,color:#ffffff
    style L3 fill:#eab308,stroke:#ca8a04,color:#ffffff
    style L4 fill:#22c55e,stroke:#16a34a,color:#ffffff
    style M fill:#3b82f6,stroke:#2563eb,color:#ffffff
    style O fill:#2563eb,stroke:#1d4ed8,color:#ffffff
```

Hoạt động của main thread và các thread con được mô tả trong sơ đồ

```mermaid
gantt
    title Timeline of Main Thread and Child Threads
    dateFormat s
    axisFormat %S
    tickInterval 1second

    %% Colors from Tailwind CSS
    %% Main Thread - Blue
    section Main Thread
    Initial State :milestone, m0, 0, 0s
    Create Threads :crit, done, a1, 0, 1s
    Wait for Threads :active, a2, after a1, 5s

    %% Thread 1 - Red
    section Thread 1
    Process :active, t1, after a1, 4s

    %% Thread 2 - Orange
    section Thread 2
    Process :active, t2, after a1, 4s

    %% Thread 3 - Yellow
    section Thread N
    Process :active, t3, after a1, 4s

    %% Styling
    %%{ init: { 
        'theme': 'base',
        'themeVariables': {
            'primaryColor': '#2563eb',
            'primaryTextColor': '#ffffff',
            'primaryBorderColor': '#1d4ed8',
            'secondaryColor': '#3b82f6',
            'secondaryTextColor': '#ffffff',
            'secondaryBorderColor': '#2563eb',
            'tertiaryColor': '#60a5fa',
            'tertiaryTextColor': '#1e3a8a',
            'tertiaryBorderColor': '#3b82f6',
            'critBorderColor': '#ef4444',
            'critBkgColor': '#dc2626',
            'activeTaskBkgColor': '#f97316',
            'activeTaskBorderColor': '#ea580c',
            'taskTextColor': '#ffffff',
            'taskTextOutsideColor': '#000000',
            'taskTextLightColor': '#ffffff',
            'taskTextDarkColor': '#1e3a8a',
            'sectionBkgColor': '#f1f5f9',
            'sectionBkgColor2': '#e2e8f0',
            'todayLineColor': '#94a3b8'
        }
    } }%%
```

## Daemon Thread

**Daemon thread** là một thread được chạy nền, nó sẽ tự động kết thúc khi main thread kết thúc. Daemon thread thường được sử dụng cho các tác vụ phụ trợ như logging, monitoring và cleanup tasks.

> **Lưu ý**: Khác với non-daemon thread, daemon thread sẽ không ngăn chương trình kết thúc khi main thread hoàn tất công việc.

### Đặc điểm chính:
- ✅ Tự động kết thúc khi main thread kết thúc
- ✅ Phù hợp cho các tác vụ background không quan trọng
- ⚠️ Không đảm bảo hoàn thành công việc trước khi kết thúc

```python
import threading
import time

def infinite_task():
    while True:
        print("Daemon Thread is running...")
        time.sleep(1)

def main():
    daemon_thread = threading.Thread(target=infinite_task)
    daemon_thread.daemon = True
    daemon_thread.start()
    time.sleep(3)
    print("Main thread finished")

if __name__ == "__main__":
    main()
```



## Thread Pool

Thread Pool là một mô hình quản lý thread hiệu quả, trong đó một nhóm các worker thread được tạo sẵn để xử lý các tác vụ từ một hàng đợi công việc. Thay vì tạo và hủy thread cho mỗi tác vụ, Thread Pool tái sử dụng các thread đã có, giúp:

- **Tối ưu tài nguyên**: Giảm overhead của việc tạo và hủy thread liên tục
- **Kiểm soát tốt hơn**: Giới hạn số lượng thread chạy đồng thời
- **Quản lý hiệu quả**: Tự động phân phối tác vụ cho các thread đang rảnh

Python cung cấp Thread Pool thông qua `concurrent.futures.ThreadPoolExecutor`:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def worker(n):
    print(f"Processing {n}")
    time.sleep(2)
    return n * n

# Sử dụng with để tự động cleanup
with ThreadPoolExecutor(max_workers=3) as executor:
    # Map các tác vụ cho thread pool
    results = executor.map(worker, [1, 2, 3, 4, 5])
    # Kết quả được trả về theo thứ tự của input
    for result in results:
        print(f"Result: {result}")
```

```mermaid
sequenceDiagram
    participant C as Client
    participant Q as Task Queue
    participant P as Thread Pool
    participant T1 as Thread 1
    participant T2 as Thread 2
    participant T3 as Thread 3
    
    C->>+Q: Submit Task 1
    C->>+Q: Submit Task 2
    C->>+Q: Submit Task 3
    C->>+Q: Submit Task 4
    
    Q->>+P: Task Available
    P->>+T1: Assign Task 1
    Q->>+P: Task Available
    P->>+T2: Assign Task 2
    Q->>+P: Task Available
    P->>+T3: Assign Task 3
    
    T1-->>-P: Task 1 Complete
    P->>+T1: Assign Task 4
    T2-->>-P: Task 2 Complete
    T3-->>-P: Task 3 Complete
    T1-->>-P: Task 4 Complete
    
    P-->>-C: All Tasks Complete
```

## Multiprocessing

Module `multiprocessing` cho phép tận dụng nhiều CPU bằng cách tạo các tiến trình con:

- **Ưu điểm**: Vượt qua giới hạn GIL, tận dụng được nhiều CPU.
- **Nhược điểm**: Tốn nhiều tài nguyên hơn threading, khó chia sẻ dữ liệu giữa các tiến trình.
- **Ứng dụng**: Phù hợp cho các tác vụ CPU-bound như xử lý hình ảnh, tính toán phức tạp.

Ví dụ về multiprocessing:
```python
from multiprocessing import Process, Pool

def heavy_calculation(n):
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    # Sử dụng Pool để quản lý nhiều tiến trình
    with Pool(4) as p:
        result = p.map(heavy_calculation, [1000000, 2000000, 3000000])
```

## Asyncio

`asyncio` là module cho phép lập trình bất đồng bộ với cú pháp async/await:

- **Ưu điểm**: Hiệu quả cho I/O-bound, dễ quản lý nhiều tác vụ đồng thời.
- **Nhược điểm**: Yêu cầu thư viện hỗ trợ async, không phù hợp cho CPU-bound.
- **Ứng dụng**: Web servers, networking, real-time applications.

Ví dụ về asyncio:
```python
import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)  # Giả lập I/O operation
    print('done fetching')
    return {'data': 1}

async def main():
    tasks = [fetch_data() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

## So sánh và Lựa chọn

1. **Threading**: Chọn khi cần xử lý nhiều tác vụ I/O và cần chia sẻ dữ liệu.
2. **Multiprocessing**: Chọn khi cần tận dụng nhiều CPU cho tính toán nặng.
3. **Asyncio**: Chọn khi cần xử lý nhiều I/O đồng thời với hiệu suất cao.

## Best Practices

1. Sử dụng threading cho I/O-bound tasks
2. Sử dụng multiprocessing cho CPU-bound tasks
3. Sử dụng asyncio cho modern async applications
4. Tránh over-engineering: đôi khi giải pháp tuần tự đơn giản là đủ
5. Cẩn thận với race conditions và deadlocks khi sử dụng threading

## Materials

* [Python Threading Tutorial: Basic to Advanced (Multithreading, Pool Executors, Daemon, Lock, Events)](https://www.youtube.com/watch?v=Rm9Pic2rpAQ&t=353s&ab_channel=KevinWood%7CRobotics%26AI)
* [Multithreading for Beginners](https://www.youtube.com/watch?v=gvQGKRlgop4&t=2284s&ab_channel=freeCodeCamp.org)