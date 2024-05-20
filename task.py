class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max_val(root):
    current = root
    while current.right:
        current = current.right
    return current.val

def find_min_val(root):
    current = root
    while current.left:
        current = current.left
    return current.val

def sum(root):
    if not root:
        return 0
    return root.val + sum(root.left) + sum(root.right)
    

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)

print(root)

print(f"max: {find_max_val(root)}")
print(f"min: {find_min_val(root)}")
print(f"sum: {sum(root)}")