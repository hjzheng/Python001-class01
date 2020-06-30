学习笔记
1. 异常捕获与处理 
   - try expect https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement
   - with https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement
   - 美化错误 https://pypi.org/project/pretty-errors

2. 使用 PyMySQL 进行数据库操作 https://pypi.org/project/PyMySQL/
3. 反爬虫:（1）模拟浏览器头部信息  https://pypi.org/project/fake-useragent/ 除了 user_agent 有些网站会验证 host, referer
4. 反爬虫:（2）cookies 验证
5. 反爬虫:（3）使用 webDriver 模拟浏览器行为 
   - https://www.selenium.dev/selenium/docs/api/py/
   - pip install selenium
   - 安装对应浏览器版本的 Driver https://sites.google.com/a/chromium.org/chromedriver/downloads  注意将这个可执行文件放入到你的 venv 中
6. 反爬虫:（4）验证码识别