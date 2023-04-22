import sys

result = ""

for i in sys.argv[1:]:
    result += ("&#x" + str(hex(ord(i))[2:]) + ";")

"".join(result)
print(result)
