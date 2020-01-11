from datetime import datetime
import sys
start = datetime.time(datetime.now()).minute
print(start)
for i in range(1000000000):
    print("hello")
    end = datetime.time(datetime.now()).minute
    if end - start > 0:
        sys.exit()