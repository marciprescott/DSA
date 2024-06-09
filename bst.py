class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            # Start with left side
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # Right side
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


tree_1 = BinarySearchTree()
print(tree_1.root)
tree_1.insert(10)
tree_1.insert(5)
tree_1.insert(13)

print(tree_1.root.value)
print(tree_1.root.left.value)
print(tree_1.root.right.value)
