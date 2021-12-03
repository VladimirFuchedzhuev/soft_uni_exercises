from collections import deque
from datetime import datetime, timedelta
from io import StringIO
import sys

input1 = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
"""
input2 = """ROB-8
7:59:59
detail
glass
wood
sock
End
"""

#sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

robots = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')


for el in range(len(robots)):
    robot = robots[el].split('-')
    robots[el] = {
        'name' : robot[0],
        'processing_time' : int(robot[1]),
        'available_at' : time
    }

products =  deque()
product = input()

while not product == "End":
    products.append(product)
    product = input()



while products:
    time = time + timedelta(seconds=1)
    next_item = products.popleft()

    for robot in robots:
        if robot['available_at'] <= time:
            robot['available_at'] = time +timedelta(seconds=robot['processing_time'])
            print(f"{robot['name']} - {next_item} [{time.time()}]")
            break
    else:
        products.append(next_item)


