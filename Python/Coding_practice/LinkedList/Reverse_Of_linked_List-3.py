

class node:
	def __init__(self,data):

		self.data = data
		self.nexct = None


class linkedList:
	def __init__(self):
		self.head= None

	def insert(self, itm):
		new_node = node(itm)
		new_node.next = self.head
		self.head = new_node

	def display(self):

		if self.head is None:
			print("Empty linkedList")

		current = self.head

		while True:
			if current is None:
				break

			print(current.data, end="->")
			current = current.next

	def reverse_node(self):

		pre = None 
		current = self.head

		while(current is not None):
			next = current.next
			current.next = pre
			pre = current
			current = next
		self.head = pre
		


			


lst=linkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
print("Before  reverse operation ")
lst.display()

print("\nAfter reverser operation ")
lst.reverse_node()
lst.display()



			
























