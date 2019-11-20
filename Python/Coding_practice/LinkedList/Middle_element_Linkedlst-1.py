

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self, itm):
        new_node = node(itm)
        new_node.next = self.head
        self.head = new_node


    def display(self):

        if self.head is None:
            print("Empty linked list")
        current = self.head

        while True:
            if current is None:
                break

            print(current.data, end="->")
            current = current.next
        print("\n")

    def get_middle(self):

        fast_ptr = self.head
        slow_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("Middle element of the linked list is ", slow_ptr.data)

    def get_reverse(self):

        current = self.head
        previous = None

        while (current is not None):
            next = current.next
            current.next = previous
            previous  = current
            current = next
        self.head = current


lst = LinkedList()
lst.Push(10)
lst.Push(20)
lst.Push(30)
lst.Push(40)
lst.Push(50)
lst.Push(60)


lst.display()

lst.get_middle()

lst.get_reverse()
lst.display()



















