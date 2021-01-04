import redis
from datetime import datetime
from time import sleep

conn = redis.Redis()
timeout = 10
conveyor = 'chocolates'

while True:
    sleep(0.5)
    message = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if message:
        piece = message[1]
        print('Lucy got a', piece, 'at', datetime.utcnow(), ', only', remaining, 'left')