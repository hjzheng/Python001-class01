import os

os.fork()

print('just a print')

# 执行结果：
# just a print
# just a print
# fork函数一旦运行就会生出一条新的进程，2个进程一起执行导致输出了2行
