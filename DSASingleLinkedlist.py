class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

n1 = Node("Vit")
n2 = Node("1")
n3 = Node("23")

n1.next = n2
n2.next = n3

curr = n1
while(curr != None):
    print(curr.data,"->",end=" ")
    curr = curr.next
print("None")