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

        s = set()
        temp = self.head

        while temp:
            if temp in s:
                return True

            s.add(temp)
            temp = temp.next
        return False

lst = LinkdList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)



# Creating loop
lst.head.next.next.next.next = lst.head


if(lst.detectLoop()):
    print("Loop found")
else:
    print("No Loop found")




