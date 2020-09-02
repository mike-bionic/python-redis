# Redis Cache tool setup on ubuntu/debian

> $ as a superuser:

```bash
apt install redis-server
```

> python pip package setup:

```bash
pip3 install flask-redis redis rq

# optional flask caching
pip3 install flask-cache
```

> manage redis configurations:

```bash
# open the .conf file with text editor
vim /etc/redis/redis.conf

# change the 'bind' address with local
bind 127.0.0.1

# change supervised conf to systemd because of running on ubuntu server
supervised systemd

# close the file and type commands to restart the server
systemctl restart redis-server
systemctl enable redis-server


# check that redis server is running on port 6379:
netstat -plntu

# check the Redis using the 'redis-cli' commands as below.
redis-cli ping
redis-cli ping "Hello Redis"
```

> securing redis server:

```bash
vim /etc/redis/redis.conf

# on the 'bind' section, change the IP address with internal network IP address.
bind INTERNAL-IP-ADDRESS #example: <92.49.145.1>

# password authentication:
requirepass <someCrappyPassword>

# disable dangerous commands to execute:
rename-command FLUSHALL "DELITALL"
rename-command CONFIG "MYSERVERCONF"


# restart server later on
systemctl restart redis-server
```

> authenticate redis-cli before running:

```bash
redis-cli

AUTH someCrappyPassword
```

> sample usage of Redis server with redis-cli:

```
redis-cli

SET <key> <value> [expiration EX seconds|PX milliseconds] [NX|XX]
SET message "Hello world"


Keys *

MYSERVERCONF get 


Keys *


# get configuration information
MYSERVERCONF get bind
MYSERVERCONF get requirepass

# exit redis-cli
exit
```
