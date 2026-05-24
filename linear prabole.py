table_size = 10
hash_table = [None] * table_size
DELETED = object()   # special marker

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    original_index = index

    while hash_table[index] is not None and hash_table[index] is not DELETED:
        if hash_table[index][0] == key:   # key exists, update
            hash_table[index] = (key, value)
            return
        index = (index + 1) % table_size
        if index == original_index:
            raise Exception("Hash table is full")

    hash_table[index] = (key, value)

def search(key):
    index = hashing(key)
    original_index = index

    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            return hash_table[index][1]
        index = (index + 1) % table_size
        if index == original_index:
            break
    return None

def delete(key):
    index = hashing(key)
    original_index = index

    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            hash_table[index] = DELETED
            return True
        index = (index + 1) % table_size
        if index == original_index:
            break
    return False

def display():
    for i, item in enumerate(hash_table):
        print(i, ":", item)
