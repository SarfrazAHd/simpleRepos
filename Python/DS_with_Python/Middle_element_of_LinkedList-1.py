class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, itm):
        new_node = node(itm)
        new_node.next = self.head
        self.head = new_node

    def printMidle(self):
        '''
        slow_ptr = self.head
        fast_ptr = self.head


        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("middle element is", slow_ptr.data) '''


        temp = self.head
        count = 0

        while self.head:
            if (count &1 ):
                temp = temp.next

            self.head = self.head.next

            count += 1
        print("Middle element is", temp.data)







lst = LinkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)

lst.printMidle()
