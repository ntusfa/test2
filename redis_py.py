import redis

r = redis.Redis(
  host='helpful-mako-37953.upstash.io',
  port=6379,
  password='********',
  ssl=True
)

r.set('foo', 'bar')
print(r.get('foo'))