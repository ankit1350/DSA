class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:  # Insert only in empty slot
                self.table[new_index] = key
                print(f"Inserted {key} at index {new_index}")
                return
        
        print("Hash Table is Full! Cannot insert.")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size
            
            if self.table[new_index] is None:
                break  # Since empty means key doesn't exist
            
            if self.table[new_index] == key:
                print(f"Key {key} found at index {new_index}")
                return new_index
        
        print(f"Key {key} not found")
        return -1

    def delete(self, key):
        pos = self.search(key)  # Reuse search logic
        if pos != -1:
            self.table[pos] = None  # Simply make it empty
            print(f"Key {key} deleted successfully!")

    def display(self):
        print("\nCurrent Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


# -----------------------------
# Menu Driven Program
# -----------------------------

hash_table = HashTable()

while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        hash_table.insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        hash_table.search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)

    elif choice == 4:
        hash_table.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
