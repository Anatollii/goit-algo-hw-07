class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Завдання 1: Найбільше значення (права частина)
def find_max(node):
    if node is None:
        return None
    current = node
    while current.right:
        current = current.right
    return current.key

# Завдання 2: Найменше значення (ліва частина)
def find_min(node):
    if node is None:
        return None
    current = node
    while current.left:
        current = current.left
    return current.key

# Завдання 3: Сума всіх значень у дереві
def sum_tree(node):
    if node is None:
        return 0
    return node.key + sum_tree(node.left) + sum_tree(node.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)

print("Максимум:", find_max(root))
print("Мінімум:", find_min(root))
print("Сума значень:", sum_tree(root))
