from config import redis_config
from config import redis_uri
import redis

r = redis.StrictRedis(**redis_config,charset="utf-8",decode_responses=True)
# or
# r	= redis.StrictRedis(url=redis_uri,charset="utf-8",decode_responses=True)

r.mset({"Russia":"Moscow","Ukraine":"Kiev"})
# True
response = r.get("Ukraine")
print(response)
# b'Kiev'

r.set('ip_address', '0.0.0.0')
r.set('timestamp', int(time.time()))
r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)')
r.set('last_page_visited', 'account')