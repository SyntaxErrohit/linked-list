class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def PrintList(self) -> None:
        item = self.head
        while item is not None:
            print(item.val)
            item = item.next
    

llist = LinkedList()
llist.head = Node(1)
e2 = Node(2)
e3 = Node(3)
llist.head.next = e2
e2.next = e3
llist.PrintList()