class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        disp = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            disp.append(cur.data)
        print(disp)


l = LinkedList()
l.add(1)
l.add(15)
l.add(7)
l.add(6)
l.display()