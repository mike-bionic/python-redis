## Data Types in Redis

Values we store in Redis can be any of 5 data types:

+ **STRING**: Any value we create with r.set() is stored as a string type. You'll notice we set the value of timestamp to be an integer in our Python script, but it appears here as a string. This may seem obnoxiously inconvenient, there's more to Redis strings than meets the eye. For one, Redis strings are binary-safe, meaning they can be used to store the contents of nearly anything, including images or serialized objects. Strings also have several built-in functions that can manipulate strings as though they were numbers, such as incrementing with the INC command.

+ **LIST**: Redis lists are mutable arrays of strings, where each string is sorted by the order in which they first appeared. Once a list is created, new items can be appended to the end of the array with the RPUSH command, or added at the zero-index via the LPUSH command. It's also possible to limit the maximum number of items in a list using the LTRIM command. If you're the kind of nerd that likes to do things like build LRU caches, you'll likely recognize the immediate benefit of this.

+ **SET**: A set is an unordered list of strings. Like Python sets, Redis sets cannot contain duplicates. Sets have the unique ability to perform unions or intersections between other sets, which is a great way to combine or compare data quickly.

+ **ZSET**: ZSETs are sets which are ordered- they retain the same constraint of disallowing duplicates. Items in the list can have their order changed after creation, making ZSETs very useful for ranking unique items. They're somewhat similar to ordered dictionaries in Python, except with a key per value (which would be unnecessary, as all set values are unique).

+ **HASH**: Redis hashes are key/value pairs in themselves, allowing you to assign a collection of key/value pairs as the value of a key/value pair. Hashes cannot be nested, because that would be crazy.