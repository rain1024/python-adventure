# Python Adventure

## Concurrent

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