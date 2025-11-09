# Node class for Linked List (each node stores key and value)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash Table class
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # Each bucket stores head of linked list

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        head = self.table[index]
        
        # Check if key already exists → update
        temp = head
        while temp:
            if temp.key == key:
                temp.value = value
                print(f"Updated key {key} with new value '{value}'")
                return
            temp = temp.next
        
        # Insert new node at start of chain
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node
        print(f"Inserted ({key}, {value}) at index {index}")

    # Search key
    def search(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp:
            if temp.key == key:
                print(f"Value for key {key} is: {temp.value}")
                return temp.value
            temp = temp.next
        print(f"Key {key} not found")
        return None

    # Delete key
    def delete(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        prev = None
        
        while temp:
            if temp.key == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.table[index] = temp.next
                print(f"Deleted key {key}")
                return
            prev = temp
            temp = temp.next
        
        print(f"Key {key} not found for deletion")

    # Display hash table
    def display(self):
        print("\nHash Table State:")
        for i in range(self.size):
            print(f"{i}:", end=" ")
            temp = self.table[i]
            if not temp:
                print("None")
            else:
                chain = []
                while temp:
                    chain.append(f"({temp.key}, {temp.value})")
                    temp = temp.next
                print(" -> ".join(chain))

# ------------------------------------
# Driver Code
# ------------------------------------
ht = HashTable()

while True:
    print("\nMenu:")
    print("1. Insert key-value")
    print("2. Search key")
    print("3. Delete key")
    print("4. Display Hash Table")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        ht.search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)
    elif choice == 4:
        ht.display()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
