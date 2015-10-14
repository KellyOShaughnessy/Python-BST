"""Class Node represents a node instance with a left and a right child.
	Initialized with a value."""
class Node:
	def __init__(self, value=None):
		self.left = None
		self.right = None
		self.value = value

"""Class BinaryTree represents an instance of a binary tree with a root and
	a size. 
	Size attribute only remains accurate if nodes are added to the tree using
	the insert method. """
class BinaryTree:
	def __init__(self, root=None):
		self.root = root
		if root == None:
			self.size = 0
		else:
			self.size = 1

	"""Inserts unique value val into tree"""
	def insert(self,val):
		#accessing tree root
		root = self.root
		#adding node to tree
		if root is None:
				self.root = Node(val)
		else:	
			if val < root.value:
				if root.left is None:
					root.left = Node(val) 
				else:
					left_tree = BinaryTree(root.left)
					left_tree.insert(val)
			elif val > root.value: 
				if root.right is None:
					root.right = Node(val)
				else:
					right_tree = BinaryTree(root.right)
					right_tree.insert(val)
		#update size of tree t
		if root.value != val:
			self.size += 1

	"""Inserts a list of unique values into tree"""
	def insert_list(self,val_list):
		for val in val_list:
			self.insert(val)

	"""Returns left child of node"""
	def get_left(self,node):
		return node.left

	"""Returns right child of node"""
	def get_right(self,node):
		return node.right

	"""Prints out information about the tree"""
	def print_init_message(self, traversal):
		print "\nPrinting the %s traversal for the following tree:" % traversal
		print "    Root of tree: %s" % self.root.value
		print "    Size of tree %d" % self.size 

	"""Given the root of a tree, prints out the preorder traversal of that tree"""
	def preorder_print(self,root):
		if self.root == root:
			self.print_init_message("preorder")
		if root is not None:
			print root.value
			self.preorder_print(root.left)
			self.preorder_print(root.right)
	
	"""Given the root of a tree, prints out the inorder traversal of that tree"""
	def inorder_print(self,root):
		if self.root == root:
			self.print_init_message("inorder")
		if root is not None:
			self.inorder_print(root.left)
			print root.value
			self.inorder_print(root.right)

	"""Given the root of a tree, prints out the postorder traversal of that tree"""
	def postorder_print(self,root):
		if self.root == root:
			self.print_init_message("postorder")		
		if root is not None:
			self.preorder_print(root.right)
			self.preorder_print(root.left)
			print root.value

if __name__ == '__main__':
	#initialize root
    root = Node(10)

    #create tree
    bt = BinaryTree(root)

    #build tree
    bt.insert(5)
    bt.insert(10)
    bt.insert(6)
    bt.insert(12)
    bt.insert_list([3,8])

    #print!
    bt.preorder_print(root)
    bt.inorder_print(root)
    bt.postorder_print(root)




