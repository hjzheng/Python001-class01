def chain(num):
    for i in range(num):
        yield i


y = chain(5)

next(y)  # 0
next(y)  # 1
list(y)  # [2, 3, 4]
next(y)  # expection: StopIteration
