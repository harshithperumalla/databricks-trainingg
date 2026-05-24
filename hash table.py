
table_size = 10
hash_table = [[] for _ in range(table_size)]

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    for i, item in enumerate(hash_table[index]):
        if item[0] == key:        
            hash_table[index][i] = (key, value)
            return
    hash_table[index].append((key, value))  
def search(key):
    index = hashing(key)
    for item in hash_table[index]:
        if item[0] == key:
            return item[1]
    return None

def delete(key):
    index = hashing(key)
    for i, item in enumerate(hash_table[index]):
        if item[0] == key:
            del hash_table[index][i]
            return True
    return False


def display():
    for i, items in enumerate(hash_table):
        print(i, ":", items)


insert("name", "Harshith")
insert("age", 20)
insert("city", "Hyderabad")

print("Search name:", search("name"))
print("Search age:", search("age"))     

delete("age")  
print("After deleting age:")
display()
