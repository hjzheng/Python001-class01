学习笔记

Twisted: https://pypi.org/project/Twisted/
异步 I/O: https://docs.python.org/zh-cn/3.7/library/asyncio.html

1. scrapy 参数调优

settings.py 中进行参数调优
```
# 最大默认并发数 默认是 16
CONCURRENT_REQUESTS = 32

# 下载延迟 3 秒
DOWNLOAD_DELAY = 3

scrapy 底层基于 Twisted
```

2. 多进程模型

多进程, 多线程，协程的目的都是希望尽可能的多处理任务

产生新进程的方式
os.fork() https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html#operating-system-interface
multiprocessing.Process()  https://docs.python.org/zh-cn/3.7/library/multiprocessing.html

多进程的第一个问题： 进程的父子关系

3. 进程间的通讯方式

为什么不能使用变量作为进程间共享数据了？

https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes

主要的共享方式
   - 队列
   - 管道
   - 共享内存

资源的抢占
   - 加锁机制


4. 进程池

5. 线程 https://docs.python.org/zh-cn/3.7/library/threading.html https://docs.python.org/zh-cn/3.7/library/_thread.html

  - 线程和进程的区别
  - 

6. 线程池