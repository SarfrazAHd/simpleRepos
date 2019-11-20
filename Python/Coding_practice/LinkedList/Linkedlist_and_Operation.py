class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, itm):
        self.next = itm

    def get_data(self):
        return self.data

    def set_data(self, itm):
        self.data = itm


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, itm):
        new_node = Node(itm)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, itm):

        previous_node = None
        current = self.head

        while current:
            if current.get_data() == itm:
                if previous_node:
                    previous_node.set_next(current.get_next())

                else:
                    self.head = current.get_next()

                self.size -= 1
                print("item succesfully removed! ")
            previous_node = current
            current = previous_node.get_next()
        return False

    def search(self, itm):

        current = self.head
        while current:
            if itm == current.get_data():
                print("Element found in linkedlist")

            current = current.get_next()
            # print("element not exist in Linkedlist")

    def display(self):
        current = self.head
        if current is None:
            print("Empty Linked list")

        while True:
            if current is None:
                break

            print(current.data, end="->")
            current = current.next


lst = Linkedlist()

lst.insert(10)
lst.insert(120)
lst.insert(30)
lst.insert(40)
lst.display()

print("\nsize of linked list is ", lst.get_size())
itm = int(input("Enter  searching elements: "))
lst.search(itm)

lst.display()
