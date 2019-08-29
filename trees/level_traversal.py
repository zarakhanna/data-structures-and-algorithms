class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def extract_val_and_children(level):
    values, new_level = [], []
    for node in level:
        values.append(node.val)
        if node.left:
            new_level.append(node.left)
        if node.right:
            new_level.append(node.right)
    return values, new_level

def level_order_jon(root):
    '''Given the root node, returns a list of lists of values'''
    output = [] # containing inner levels
    if root == None: return output    
    curr_level = [root]
    while len(curr_level) > 0:
        values, next_level = extract_val_and_children(curr_level)
        curr_level = next_level
        output.append(values)
    return output

def level_order(root):
    '''Given the root node, returns a list of lists of values'''
    q = []
    rr = []
    if root == None:
        return []
    q.append([root])
    while len(q[0]) > 0:
        coolo = []
        for i in q[0]:
            if i.left != None:
                coolo.append(i.left)
            if i.right != None:
                coolo.append(i.right)
        q.append(coolo)
        t = q.pop(0)
        rra = []
        for i in t:
            rra.append(i.val)
        rr.append(rra)
    return rr



my_root = TreeNode(3)
my_root.left = TreeNode(9)
my_root.right = TreeNode(20)
my_root.right.left = TreeNode(15)
my_root.right.right = TreeNode(7)

print(level_order(my_root))
print([
  [3],
  [9,20],
  [15,7]
])