


class Tree:
	def __init__(self, data):
		self.node = data
		self.left_child=None
		self.right_child=None


	def insert(self, data):
		if self.node:
			if self.node > data:
				if self.left_child: 
					self.left_child.insert(data)
					return data,"data succesfully inserted in left subtree"
				else:
					self.left_child = Tree(data)

			elif self.node < data:
				if self.right_child: 
					self.right_child.insert(data)
					return data,"data succesfully inserted in right subtree"
				else:
					self.right_child = Tree(data)

		else:
			self.node=Tree(data)


	def search(self, data):
		if self.node:
			if self.node == data:
				return "Element found at root node"

			elif self.node > data:
				if self.left_child:
					self.left_child.search(data)
					return "element found in left subtree"
				else:
					return "element not found in left subtree"

			else :
				if self.right_child:
					self.right_child.search(data)
					return "Found in right subtree"

				else:
					return "element not found in right subtree"

		else:
			return "Empty tree can't perform serach operation"

	def preorder(self):
		if self:
			print(self.node, end=" ")

			if self.left_child:
				print(self.left_child.preorder(), end=" ")

			if self.right_child:
				print(self.right_child.preorder(), end=" ")

	def inorder(self):
		if self:
			if self.left_child:
				print(self.left_child.inorder(), end=" ")

			print(self.node, end=" ")

			if self.right_child:
				print(self.right_child.inorder(), end=" ")


	def postorder(self):
		if self:
			if self.left_child:
				print(self.left_child.postorder(),end=" ")
			
			if self.right_child:
				print(self.right_child.postorder(), end=" ")

			print(self.node, end=" ")


bst = Tree(15)
bst.insert(10)
bst.insert(12)
bst.insert(17)
bst.insert(11)
print(bst.search(10))
bst.postorder()
print("preorder is", end=" ")



