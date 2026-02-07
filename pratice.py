class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n1.next = n2
n2.next = n3

curr = n1
while(curr != None):
    print(curr.data,"->",end=" ")
    curr = curr.next
print("None")

m1 = Node("9")
m2 = Node("8")
m3 = Node("7")
m4 = Node("6")
m5 = Node("7")
m6 = Node("4")
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6

curr = m1
while(curr != None):
    print(curr.data,"->",end=" ")
    curr = curr.next
print("None")


print("Merging Array ")
n1.next = m1
m1.next = m2
m2.next = n2
n2.next = m3
m3.next = m4
m4.next = n3
n3.next = m5
m5.next = m6
curr = n1
while(curr != None):
    print(curr.data,"->",end=" ")
    curr = curr.next
print("None")