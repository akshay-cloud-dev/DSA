class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert(self):
        if self is None:
            return None

        # Swap left and right children
        self.left, self.right = self.right, self.left

        # Recursively invert the subtrees
        if self.left:
            self.left.invert()
        if self.right:
            self.right.invert()

        return self

# Create the tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree
inverted_root = root.invert()

# Function to print the tree
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print('  ' * level + '->', node.val)
        print_tree(node.left, level + 1)

# Print the original tree
print("Original Tree:")
print_tree(root)

# Print the inverted tree
print("\nInverted Tree:")
print_tree(inverted_root)
