class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def check_binary_search_tree_(root):
    MAX_INT = 10 ** 10

    def is_bst(root, max_data, min_data):
        if root is None:
            return True
        if root.data <= min_data:
            return False
        if root.data >= max_data:
            return False

        if is_bst(root.left, min(max_data, root.data), min_data) and is_bst(root.right, max_data,
                                                                            max(min_data, root.data)):
            return True
        else:
            return False

    return is_bst(root, MAX_INT, -1 * MAX_INT)

tree = node(2)
tree.left = node(1)
tree.right = node(3)
tree.right.right = node(4)
tree.right.right.right = node(5)

print(check_binary_search_tree_(tree))
