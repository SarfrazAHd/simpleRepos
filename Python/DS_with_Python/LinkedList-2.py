

class Node:
    def __init__(self, data):
        self.data= data
        self.next=None

class LinkdeList:
    def __init__(self):
        self.head = None

    def insert(self, itm):
        new_node=Node(itm)
        new_node.next= self.head
        self.head = new_node

    def display(self):

        if self.head is None:
            print("Empty LinkdeList")

        current = self.head

        while True:
            if current is None:
                break

            print(current.data, end="<-")
            current=current.next

    def get_middle(self):

        temp = self.head
        count = 0

        while self.head:
            if (count &2):
                temp = temp.next
            self.head = self.head.next

            count +=1
        print("\nMiddle element is", temp.data)


lst=LinkdeList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)

lst.display()

lst.get_middle()
