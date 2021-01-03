import redis

# Redis 서버 설치 필요
conn = redis.Redis()
conn.hincrby('test', 'count', 3)
conn.hget('test', 'count')