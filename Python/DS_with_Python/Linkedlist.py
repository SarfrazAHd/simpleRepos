
class node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def get_next(self):
        return self.next

    def set_next(self, data):
        self.next = data


    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data=data



class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0


    def get_size(self):
        return self.size


    def insert(self, itm):
        new_node=node(itm)
        new_node.next = self.head
        self.head=new_node
        self.size +=1


    def delete(self,itm):

        pre = None
        curr = self.head

        while curr:
            if curr.get_data() == itm:
                if pre:
                    pre.set_next(curr.get_next())

                else:
                    self.head = curr.get_next()
                self.size -= 1
                return "Element Removed"
            pre = curr
            curr = curr.get_next()
        return False


    def search(self,itm):

        curr = self.head

        while curr: 
            if curr.get_data() == itm:
                return "Element " + str(itm) + " found in LinkedList "
            curr = curr.get_next()
        return "element not found in LinkedList"




    def display(self):

        if self.head is None:
            print("Empty LinkedList")
        current= self.head

        while True:
            if current is None:
                break

            print(current.data, end=" <- ")
            current = current.next


    def get_middle(self):

        fast_ptr= self.head
        slow_ptr= self.head


        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("\nMidlle element is ", slow_ptr.data)



lst=LinkedList()

lst.insert(10)
lst.insert(11)
lst.insert(21)
lst.insert(10)
lst.insert(12)
lst.insert(42)
lst.insert(31)
lst.insert(22)
lst.insert(100)
lst.insert(19)
lst.insert(10)
lst.insert(1000)


lst.display()
print("\n", lst.get_size())










