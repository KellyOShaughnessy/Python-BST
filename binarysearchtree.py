#binarysearchtree.py

class Node(object):
	def __init__(self, val=None):
		"""Initializer: A new node representing an item of a binary search tree.

		Instance variables:
		val: value assigned to this node

		left: the left child (node) of this node
		right: the right child (node) of this node
		"""
		self.left = None
		self.right = None
		self.value = val

class BST(object):
	def __init__(self, root=None):
		"""Initializer: A new instance of a binary search tree with a root
		and a size. 

		Preconditions: size variable only remains accurate if nodes are added to
		the tree using the insert method.
		"""
		self.root = root
		if root == None:
			self.size = 0
		else:
			self.size = 1

	def insert(self,val):
		"""Inserts unique value val into tree. No duplicate node values."""
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
					left_tree = BST(root.left)
					left_tree.insert(val)
			elif val > root.value: 
				if root.right is None:
					root.right = Node(val)
				else:
					right_tree = BST(root.right)
					right_tree.insert(val)
		#update size of tree t
		if root.value != val:
			self.size += 1

	def insert_list(self,val_list):
		"""Inserts a list of unique values into tree."""
		for val in val_list:
			self.insert(val)

	def get_left(self,n):
		"""Returns: left child of node n."""
		return n.left

	def get_right(self,n):
		"""Returns: right child of node n."""
		return n.right

	def print_init_message(self, traversal):
		"""Prints out information about the tree: which traversal is being
		performeed, the root value of the tree, and the size of the tree.
		"""
		print "\nPrinting the %s traversal for the following tree:" % traversal
		print "    Root of tree: %s" % self.root.value
		print "    Size of tree %d" % self.size 

	def preorder_print(self,root):
		"""Prints out the preorder traversal of the tree with root root."""
		if self.root == root:
			self.print_init_message("preorder")
		if root is not None:
			print root.value
			self.preorder_print(root.left)
			self.preorder_print(root.right)
	
	def inorder_print(self,root):
		"""Prints out the inorder traversal of the tree with root root."""
		if self.root == root:
			self.print_init_message("inorder")
		if root is not None:
			self.inorder_print(root.left)
			print root.value
			self.inorder_print(root.right)

	def postorder_print(self,root):
		"""Prints out the postorder traversal of the tree with root root"""
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




