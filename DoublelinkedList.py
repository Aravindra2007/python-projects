class Node:
    def __init__(self,d):
        self.data = d
        self.prev = None
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3

rev = n4
while rev != None:
    print(rev.data,end="<->")
    rev = rev.prev
print("None\n")

curr = n1
while curr != None:
    print(curr.data,end="<->")
    curr = curr.next
print("None\n")