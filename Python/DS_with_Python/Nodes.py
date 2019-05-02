class Node:
	def __init__(self, data):
		self.data=data
		self.next =None
		
class LinkList:
	def __init__(self):
		self.head=None
		self.size=0


	def get_size(self):
		return self.size

	def insert(self, new_data):

		if self.head is None:
			self.head=new_data

		else:
			lastnode=self.head

			while True: 
				if lastnode.next is None:
					break

				lastnode=lastnode.next
			lastnode.next=new_data
		self.size +=1

	def show(self):
		if self.head is None:
			print("Empty linked list ")

		current = self.head
		while True: 
			if current is None:
				break

			print(current.data, end= "--> ")
			current=current.next

fnode=Node("First node")
snode=Node("seceond node")

lst=LinkList()
lst.insert(snode)
lst.insert(fnode)
lst.insert(Node(3))
lst.insert(Node(4))
lst.insert(Node(5))
lst.insert(Node(" This is 3rd node"))
lst.show()

print("\n",lst.get_size())
