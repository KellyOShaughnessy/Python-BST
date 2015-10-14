#binarysearchtree.py

class Node(object):
	"""Represents an item in a binary search tree.
	Each node has a left child, right child, and a value"""
	def __init__(self, val=None):
		"""Creates a new node."""
		self.left = None
		self.right = None
		self.value = val

	def get_left(self):
		"""Returns: left child of node n."""
		return self.left

	def get_right(self):
		"""Returns: right child of node n."""
		return self.right

	def is_leaf(self):
		"""Returns: True if node is a leaf, and False if node is not a leaf."""
		return (self.right != None and self.left !=None)

class BST(object):
	def __init__(self, root=None):
		"""Initializer: A new instance of a binary search tree with a root
		and a size. 

		Preconditions: size variable only remains accurate if nodes are added to
		the tree using the insert method.
		"""
		self.root = root
		if root is None:
			self.size = 0
		else:
			self.size = 1

	def insert(self,val):
		"""Inserts unique node with value val into tree. No duplicate nodes."""
		#accessing tree root
		root = self.root
		#adding node to tree
		if root is None:
			self.root = Node(val)
		else:	
			if val < root.value:
				left_tree = BST(root.left)
				left_tree.insert(val)
			elif val > root.value: 
				right_tree = BST(root.right)
				right_tree.insert(val)
			#update size of tree t
			if root.value != val:
				self.size += 1

	def insert_list(self,val_list):
		"""Inserts a list of unique values into tree."""
		for val in val_list:
			self.insert(val)

	def contains(self,n):
		"""Returns: True if node n is in the tree, else False"""
		if self is None or n is None:
			return False
		elif self.root.value == n.value:
			return True
		else:
			return self.right.contains(n) or self.left.contains(n)

	def print_init_message(self, traversal):
		"""Prints out information about the tree: which traversal is being
		performeed, the root value of the tree, and the size of the tree.
		"""
		print "\nPrinting the %s traversal for the following tree:" % traversal
		print "    Root of tree: %s" % self.root.value
		print "    Size of tree %d" % self.size 

	def preorder_print(self,root):
		"""Prints out the preorder traversal of the tree."""
		if self.root == root:
			self.print_init_message("preorder")
		if root is not None:
			print root.value
			self.preorder_print(root.left)
			self.preorder_print(root.right)
	
	def inorder_print(self,root):
		"""Prints out the inorder traversal of the tree."""
		if self.root == root:
			self.print_init_message("inorder")
		if root is not None:
			self.inorder_print(root.left)
			print root.value
			self.inorder_print(root.right)

	def postorder_print(self,root):
		"""Prints out the postorder traversal of the tree."""
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
    bt = BST(root)

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

