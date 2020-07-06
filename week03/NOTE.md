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
