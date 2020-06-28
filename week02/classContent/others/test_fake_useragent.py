from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

print(ua.chrome)
print(ua.ie)
print(ua.random)
