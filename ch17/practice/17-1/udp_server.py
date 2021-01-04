import socket
from datetime import datetime

addr = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call...')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 소켓 생성
server.bind(addr)   # 소켓 바인딩
while True:
    data, client = server.recvfrom(max_size)    # 데이터 수신
    if data == b'time':
        now = str(datetime.utcnow())
        data = now.encode('utf-8')  # 인코딩
        server.sendto(data, client) # 데이터 발신
        print('Server sent', data)
server.close()  # 소켓 닫기