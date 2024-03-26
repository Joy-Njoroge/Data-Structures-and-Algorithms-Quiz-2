class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
printList(node1)

reversed_head = reverseList(node1)

print("\nReversed list:")
printList(reversed_head)
