class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

bst = BST()
root = None

while True:
    print("\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        root = bst.insert(root, data)
    elif choice == 2:
        key = int(input("Enter value to delete: "))
        root = bst.delete(root, key)
    elif choice == 3:
        key = int(input("Enter value to search: "))
        result = bst.search(root, key)
        if result:
            print("Node found!")
        else:
            print("Node not found!")
    elif choice == 4:
        print("BST in Inorder Traversal: ", end="")
        bst.inorder(root)
        print()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
