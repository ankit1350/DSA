# Binary Search Tree Implementation in Python

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # Search
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Delete
    def delete(self, root, key):
        if root is None:
            return root

        # Traverse to find the node
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")




if __name__ == "__main__":
    bst = BST()
    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Display (Inorder)")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            key = int(input("Enter key to insert: "))
            bst.insert(key)
        elif choice == '2':
            key = int(input("Enter key to delete: "))
            bst.delete(key)
        elif choice == '3':
            print("Inorder traversal:", end=' ')
            bst.inorder()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
