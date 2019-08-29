class BinaryNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = BinaryNode(5)
root.left = BinaryNode(6)
root.left.left = BinaryNode(11)
root.left.left.left = BinaryNode(7)
root.left.left.right = BinaryNode(2)
root.right = BinaryNode(8)
root.right.left = BinaryNode(13)
root.right.right = BinaryNode(4)
root.right.right.right = BinaryNode(1)

def inorder(tr):
    '''inorder returns me a list'''
    banana = []
    if tr is None or tr.val == None: return []
    banana.extend(inorder(tr.left))
    banana.append(tr.val)
    banana.extend(inorder(tr.right))
    return banana

def tree_sum(tree):
    ''' Returns the sum of the values in the tree '''
    return sum(inorder(tree)) # correct

print(tree_sum(root))

def tree_sum2(tree):
    if tree == None:
        return 0
    return tree_sum2(tree.left) + tree_sum2(tree.right) + tree.val

print(tree_sum2(root))

def tree_max(tree):
    ''' Returns the largest value in the tree '''
    return max(inorder(tree))

print(tree_max(root))

def tree_max2(tree):
    if tree == None:
        return 0
    return max([tree_max2(tree.left),tree_max2(tree.right),tree.val])

print(tree_max2(root))

def tree_min(tree):
    ''' Returns the smallest value in the tree '''
    return min(inorder(tree))

print(tree_min(root))

def tree_depth(tree):
    ''' Returns the maximum depth of the tree '''
    if tree == None:
        return 0
    return  max([tree_depth(tree.left),tree_depth(tree.right)]) +1

print(tree_depth(root))

def tree_max_path_sum(tree):
    ''' Returns the maximum path sum of the tree '''
    if tree == None:
        return 0
    return max([tree_max_path_sum(tree.left),tree_max_path_sum(tree.right)]) + tree.val

print(tree_max_path_sum(root))

def tree_min_path_sum(tree):
    ''' Returns the minimum path sum of the tree '''
    pass

def has_path_sum(tree, total):
    ''' Returns True if the tree has a path that sums up to total, else False '''
    pass

