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
            print(item.val, end=" -> ")
            item = item.next
        print("None")
    
    def AddFirst(self, node) -> None:
        node.next = self.head
        self.head = node
    
    def AddEnd(self, node) -> None:
        item = self.head
        while item.next is not None:
            item = item.next
        item.next = node
    
    def RemoveFirst(self) -> None:
        self.head = self.head.next
    
    def RemoveEnd(self) -> None:
        item = self.head
        while item.next.next is not None:
            item = item.next
        item.next = None

    def Reverse(self) -> None:
        prev = None
        item = self.head
        while item is not None:
            item.next, prev, item = prev, item, item.next
        self.head = prev
    
def summ(list1, list2):
    item1 = list1.head
    item2 = list2.head
    s = LinkedList()
    node = Node(item1.val + item2.val)
    s.head = node
    item1, item2 = item1.next, item2.next
    while item1 is not None and item2 is not None:
        node.next = Node(item1.val+item2.val)
        node = node.next
        item1, item2 = item1.next, item2.next
    s.PrintList()

"""
llist = LinkedList()
llist.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
llist.head.next = e2
e2.next = e3
e3.next = e4
llist.PrintList()
llist.AddFirst(Node(5))
llist.AddEnd(Node(6))
llist.PrintList()
llist.num()
"""

l1 = LinkedList()
l1.head = Node(2)
a2 = Node(4)
a3 = Node(3)
l1.head.next = a2
a2.next = a3

l2 = LinkedList()
l2.head = Node(5)
b2 = Node(6)
b3 = Node(4)
l2.head.next = b2
b2.next = b3

summ(l1, l2)