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
        if item is None:
            item = node
            return None
        while item.next is not None:
            item = item.next
        item.next = node
    
    def RemoveFirst(self) -> None:
        self.head = self.head.next


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
llist.RemoveFirst()
llist.PrintList()