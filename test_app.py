import redis
from config import redis_config

r = redis.StrictRedis(**redis_config)
r.set('foo', 'bar')

print('value "foo" from Redis: {}'.format(r.get('foo')))
