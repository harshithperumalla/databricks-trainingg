table_size = 10
hash_table = [None] * table_size
DELETED = object()

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    i = 0
    while i < table_size:
        new_index = (index + i*i) % table_size
        if hash_table[new_index] is None or hash_table[new_index] is DELETED:
            hash_table[new_index] = (key, value)
            return
        elif hash_table[new_index][0] == key:   # update if key exists
            hash_table[new_index] = (key, value)
            return
        i += 1
    raise Exception("Hash table is full")

def search(key):
    index = hashing(key)
    i = 0
    while i < table_size:
        new_index = (index + i*i) % table_size
        if hash_table[new_index] is None:
            return None
        if hash_table[new_index] is not DELETED and hash_table[new_index][0] == key:
            return hash_table[new_index][1]
        i += 1
    return None

def delete(key):
    index = hashing(key)
    i = 0
    while i < table_size:
        new_index = (index + i*i) % table_size
        if hash_table[new_index] is None:
            return False
        if hash_table[new_index] is not DELETED and hash_table[new_index][0] == key:
            hash_table[new_index] = DELETED
            return True
        i += 1
    return False

def display():
    for i, item in enumerate(hash_table):
        print(i, ":", item)
