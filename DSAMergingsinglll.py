class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

def List(head):
    curr = head
    while(curr):
        print(curr.data,"->",end=" ")
        curr = curr.next
    print("None")

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
print("!st List")
List(n1)

m1 = Node(9)
m2 = Node(8)
m3 = Node(7)
m4 = Node(6)
m5 = Node(5)
m6 = Node(4)
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6
print("2nd List")
List(m1)

# def Merge(head1,head2):
#     if not head1:
#         return head2
#     curr = head1
#     while curr.next:
#         curr = curr.next
#     curr.next = head2
#     return head1

def Merge(l1,l2):
    dummy = Node(0)
    tail = dummy
    while l1 or l2:
        for _ in range(1):
            if l1:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

        for _ in range(2):
            if l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
    return dummy.next

    
Merged = Merge(n1,m1)
List(Merged)