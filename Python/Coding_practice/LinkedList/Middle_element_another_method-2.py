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
    
        temp = self.head
        count = 0
        while self.head:
            if (count & 1 ):
                temp = temp.next

            self.head = self.head.next

            count += 1
        print("\nMiddle element is ", temp.data)

    def display(self):

        if self.head is None:
            print("Empty LinkedList")

        current = self.head

        while True:
            if current is None:
                break

            print(current.data, end="<-",)
            current = current.next


lst = LinkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)
lst.insert(60)

lst.display()
lst.printMidle()
