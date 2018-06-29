import re
from urllib.request import urlopen
import datetime

with urlopen("http://pastebin.com/raw/3UhY04HC") as stream:
    first = [line.decode('ascii') for line in stream]
with urlopen("http://pastebin.com/raw/reHwxHJF") as stream:
    second = [line.decode('ascii') for line in stream]
    
#matches = [re.match(r"^\[([0-9 ,:-]+)\](.*)$", line) for line in first]
#data = [re.match(r"^\[([0-9 ,:-]+)\](.*)$", line) for line in first]

def first_datetime(line):
    m = re.match(r"^\[([0-9 :-]+),", line)
    if m:
        timestamp = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
        return timestamp
    else:
        return None

def second_datetime(line):
    m = re.match(r"^(?:[^|]*\|){2} (.{19})", line)
    if m:
        timestamp = datetime.datetime.strptime(m.group(1), "%Y/%m/%d %H:%M:%S")
        return timestamp
    else:
        return None
    
first = [(first_datetime(line), line) for line in first]
second = [(second_datetime(line), line) for line in second]

all = [(timestamp, line) for timestamp, line in first + second if timestamp]

print(all[:10])

with open("output.log", "w") as stream:
    for timestamp, line in sorted(all):
        print(line.strip(), file=stream)