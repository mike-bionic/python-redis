# Redis usage with Python
> install redis-server on your machine
```bash
sudo apt-get install redis-server
```
+ [Server setup process](/redis_setup_secuure.md)

> Access CLI 
```bash
redis-cli
# if password is set:
auth <password>
set <key> <value>
get <key>
# by default it uses database 0
# to access different database:
redis-cli -n <db number>
```
> install Redis pip package for Python
```bash
pip3 install redis
```

## Redis URI
```
redis_uri = redis://:hostname.redislabs.com@mypassword:12345/0
# [CONNECTION_METHOD]:[HOSTNAME]@[PASSWORD]:[PORT]/[DATABASE]
```

## Redis keywords:
+ SADD - Set add
+ rpush - inserts all the speci ed values at the tail of the list stored at key.
+ llen - returns the length of the list stored at key.
+ lindex - returns the element at index index in the list stored at key. The index is zero-based, so 0 means the rst element, 1 the second element and so on.

```bash
>>> r.rpush('japanese', 'ichi')
1
>>> r.rpush('japanese', 'ni')
2
>>> r.rpush('japanese', 'san')
3
>>> r.rpush('japanese', 'yon')
4
>>> r.llen('japanese')
4
>>> r.lindex('japanese', 3)
b'san'
```
## Datatype issues

+ [Data types in Redis](/redis_data_types.md)
+ [Hackersabdsackers: Redis data types](https://github.com/hackersandslackers/redis-python-tutorial)

Python's datetime format can't be accepted by redis, to avoid this issue do:
```python
import datetime
today = datetime.date.today()
stoday = today.isoformat()
# # python3.7+
# stoday = str(toay)
locations = {"12543.1245","1234.666"}
r.sadd(stoday,*locations)
```
