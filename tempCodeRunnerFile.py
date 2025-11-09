# Hash Table Implementation using Chaining

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]  # Each bucket is a list (chaining)

    # Hash Function : Division Method
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        # Check if key already exists → update value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value '{value}'.")
                return

        # Otherwise insert a new key-value pair
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value '{value}' at index {index}.")

    # Search key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key {key} found: Value = {pair[1]}")
                return pair[1]

        print(f"Key {key} not found.")
        return None

    # Delete key
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Key {key} deleted successfully.")
                return
        print(f"Key {key} not found. Deletion failed.")

    # Display hash table
    def display(self):
        print("\nHash Table Layout:")
        for i in range(self.size):
            print(f"Index {i} : {self.table[i]}")
