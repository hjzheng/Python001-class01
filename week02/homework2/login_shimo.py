from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im')
    time.sleep(1)

    login_btn = browser.find_element_by_xpath(
        '//div[@class="entries"]/a[2]')
    login_btn.click()

    time.sleep(1)

    browser.find_element_by_xpath(
        '//div[@type="mobileOrEmail"]/div/input').send_keys('15055495@qq.com')
    browser.find_element_by_xpath(
        '//div[@type="password"]/div/input').send_keys('test123test456')

    time.sleep(1)

    browser.find_element_by_xpath(
        '//button[@type="black"]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
