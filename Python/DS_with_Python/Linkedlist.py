


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, new_data):

        if self.head is None:
            self.head = new_data

        else:
            lastnode = self.head

            while True:
                if lastnode.next is None:
                    break;

                lastnode = lastnode.next
            lastnode.next = new_data
        self.size += 1


    def Display(self):

        if self.head is None:
            print("Sorry !! Empty Linkded-list")

      
        current = self.head

        while True:
            if current is None:
                break

            print(current.data, end=" -> ")
            current = current.next

    def remove(self, deleting_data):
        prev_node = None
        current = self.head


        while current:
            if current.get_data() == deleting_data:
                if prev_node:

                    prev_node.set_next(current.get_next())
                else:
                    current = current.get_next()
                self.size -= 1
                return True  # data removed
            else:
                prev_node = current
                current = current.get_next()
        return False  # data not found

    def find(self, d):
        current = self.head

        while current:
            if current.get_data() == d:
                print("Element found ")
                return d
            else:
                current = current.get_next()
        return False



lst = LinkedList()

lst.insert(Node(1))
lst.insert(Node(2))
lst.insert(Node(4))
lst.insert(Node(5))
lst.insert(Node(6))
lst.insert(Node(7))
lst.Display()

print("\n", lst.get_size())


