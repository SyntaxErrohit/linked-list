class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        s = ""
        while self is not None:
            s += str(self.val) + " -> "
            self = self.next
        return s + "None"

def MakeListNode(l):
    node = ListNode(l.pop())
    for i in l:
        n = ListNode(i)
        n.next = node
        node = n
    return node

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode((l1.val + l2.val)%10)
        n = (l1.val + l2.val)//10
        l1, l2 = l1.next, l2.next
        node = s
        while l1 is not None or l2 is not None:
            if l1 is None:
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next

            if l2 is None:
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next

            node.next = ListNode((n1 + n2 + n)%10)
            n = (n1 + n2 + n)//10
            node = node.next
        if n:
            node.next = ListNode(n)
        return s

l1 = MakeListNode([9, 9, 9, 9, 9, 9])
l2 = MakeListNode([9, 9, 9, 9])
print(addTwoNumbers(l1, l2))