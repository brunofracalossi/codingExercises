class node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right

def printTree(tree, side=None, father_value=None):
	node = tree
	if side != None:
		print str(node.value) + " " + side + " of node " + str(father_value)
	else:
		print str(node.value)
	
	if node.left != None:
		printTree(node.left, "Left", node.value)
	
	if node.right != None:
		printTree(node.right, "Right", node.value)

def mirrorTree(tree):
	if tree == None:
		return
	
	mirrorTree(tree.left)
	mirrorTree(tree.right)

	#store and the exchange left with right
	left  = tree.left
	right = tree.right
	
	tree.left  = right
	tree.right = left 

# setting the new tree
tree = node(1, node(2, node(4), node(5, None, node(7))), node(3, node(6)))

print "Original Tree"
printTree(tree)

# generate mirrored tree
new_tree = mirrorTree(tree)
print "==================\nMirrored Tree"
printTree(tree)
