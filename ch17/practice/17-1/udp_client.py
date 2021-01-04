import socket
from datetime import datetime
from time import sleep

addr = ('localhost', 6789)  # 서버 주소
max_size = 4096

print('Starting the client at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 소켓 생성
while True:
    sleep(5)
    client.sendto(b'time', addr)                # 데이터 발신
    data, server = client.recvfrom(max_size)    # 데이터 수신
    print('Client read', data)
client.close()  # 소켓 닫기
