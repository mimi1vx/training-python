
import json

with open("example.txt") as stream:
    data = json.load(stream)

for idx, item in enumerate(data):
    hostname, port = item['nodename'].split(':', 1)
    if idx != 0:
        print(", ", end='')
    print(hostname, end='')
print()
