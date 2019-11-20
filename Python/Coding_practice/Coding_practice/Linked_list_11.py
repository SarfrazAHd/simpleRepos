

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return  self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_data):
        self.next  = new_data


class LinkdList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert_data(self, itm):
        new_node = Node(itm)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def Display_linkedlist(self):

        if self.head is None:
            print("Empty Linked_list ")

        current = self.head
        while 1:
            if current is None:
               break
            print(current.data, end="->")
            current = current.next


    def delete_data(self, itm):
        previous = None
        current = self.head

        while current:
            if current.get_data() == itm:
                if previous:
                    previous.set_next(current.get_next())

                else:
                    self.head = current.get_next()

                self.size -=1
                print("\nItem succesfully Removed")

            previous = current
            current = previous.get_next()
        return False

    def search_data(self, itm):

        current = self.head

        while current:
            if current.get_data() == itm:
                print("element Found in linkedlist ")

            current = current.get_next()


lst = LinkdList()
lst.insert_data(10)
lst.insert_data(5)
lst.insert_data(15)
lst.Display_linkedlist()


lst.delete_data(15)

lst.search_data(11)






