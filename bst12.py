class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    # Search for a key
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    # Delete a key
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children → find inorder successor
            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.right = self._delete_recursive(root.right, successor.key)

        return root

    # Helper → find smallest value in subtree
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Display → Inorder Traversal (Sorted Order)
    def display(self):
        print("BST in sorted order:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end=" ")
            self._inorder(root.right)


# MENU DRIVEN PROGRAM
bst = BinarySearchTree()

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display (Inorder)")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        bst.insert(key)
        print("Inserted successfully.")

    elif choice == 2:
        key = int(input("Enter value to search: "))
        result = bst.search(key)
        if result:
            print("Key found in BST.")
        else:
            print("Key not found.")

    elif choice == 3:
        key = int(input("Enter value to delete: "))
        bst.delete(key)
        print("Delete operation completed.")

    elif choice == 4:
        bst.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
