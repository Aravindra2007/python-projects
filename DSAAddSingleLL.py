class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

n1 = Node("A")
n2 = Node("B")
n3 = Node("c")


m1 = Node("X")
m2 = Node("Y")
m3 = Node("Z")

m1.next = n1
n1.next = m2
m2.next = n2
n2.next = m3
m3.next = n3

head = m1
while(head != None):
    print(head.data,"->",end=" ")
    head = head.next
print(head)