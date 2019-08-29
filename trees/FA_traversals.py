class BinaryNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = BinaryNode('A')
root.left = BinaryNode('B')
root.left.left = BinaryNode('C')
root.left.left.left = BinaryNode('D')
root.left.left.right = BinaryNode('E')
root.left.left.right.left = BinaryNode('F')
root.left.left.right.right = BinaryNode('G')
root.right = BinaryNode('H')
root.right.left = BinaryNode('I')
root.right.right = BinaryNode('J')
root.right.right.left = BinaryNode('K')
root.right.right.left.right = BinaryNode('M')
root.right.right.right = BinaryNode('L')

testroot = BinaryNode(1)
testroot.left = BinaryNode(2)
testroot.right = BinaryNode(3)

def postorder(tr):
    '''postorder returns me a list'''
    # 1. make a list called banana
    banana = []
    #BASECASE!!!
    if tr is None or tr.val == None: return []
    # 2. add the left tree's postorder
    banana.extend(postorder(tr.left))
    # 3. add the right tree's postorder
    banana.extend(postorder(tr.right))
    # 4. add the root's val
    banana.append(tr.val)
    # 5. return the list
    return banana

print(postorder(testroot))
print(postorder(root))

def preorder(tr):
    '''preorder returns me a list'''
    banana = []
    if tr is None or tr.val == None: return []
    banana.append(tr.val)
    banana.extend(preorder(tr.left))
    banana.extend(preorder(tr.right))
    return banana

print(preorder(testroot))
print(preorder(root))

def inorder(tr):
    '''inorder returns me a list'''
    banana = []
    if tr is None or tr.val == None: return []
    banana.extend(inorder(tr.left))
    banana.append(tr.val)
    banana.extend(inorder(tr.right))
    return banana

print(inorder(testroot))
print(inorder(root))

test_you_now = [[[['A'], ['B'], 'C'], 'D'], [['E'], [[['F'], 'G'], ['H'], 'I'], 'J'], 'K']
test_you_before = [[[[[[[[[1]]]]]]]]]
test_you_after = [1,[2,[3,[4,[5,[6,[7,[8,[9,10]]]]]]]]]
test_you_again = [[1, 2, [3, 4, [5, 6]]],[7, 8, [9], 10]]

# Given an arbitarily nested list, return the flattened list
def flatten(l):
    rl = []
    for i in l:
        if type(i) != list:
            rl.append(i)
        else:
            rl.extend(flatten(i))
    return rl

print(flatten(test_you_now))
print(flatten(test_you_before))
print(flatten(test_you_after))
print(flatten(test_you_again))