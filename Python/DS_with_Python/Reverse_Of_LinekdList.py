

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedLiset:
    def __init__(self):
        self.head = None

    def insert(self, itm):
        new_node = Node(itm)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):

        prev = None
        curr = self.head

        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def get_middle(self):

        fast_ptr = self.head
        slow_ptr = self.head

        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

            print("Middle element is", slow_ptr.data)




    def display(self):
        if self.head is None:
            print("Empty Linked list")


        current = self.head

        while True:
            if current is None:
                break

            print(current.data, end="<-")
            current = current.next




lst = LinkedLiset()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)
lst.display()
print("\nAfter reverse:")

lst.reverse()
lst.display()
print("")
lst.get_middle()



