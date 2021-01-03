import redis

# Redis 서버 설치 필요
conn = redis.Redis()
conn.hmset('test', {'count':1 ,'name':'Fester Bestertester'})
conn.hgetall('test')