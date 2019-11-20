class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkdList:
    def __init__(self):
        self.head = None

    def insert(self, itm):
        new_node = node(itm)
        new_node.next = self.head
        self.head = new_node

    def detectLoop(self):
        s = list()
        current = self.head

        while (current is not None):
            if current in s:
                return True
            s.append(current)
            current = current.next
        return False


             
       

lst = LinkdList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)



# Creating loop
#lst.head.next.next.next.next = lst.head


if(lst.detectLoop()):
    print("Loop found")
else:
    print("No Loop found")




