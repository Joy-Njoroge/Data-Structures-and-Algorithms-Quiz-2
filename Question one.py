class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

# Creating a linked list with a cycle
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a cycle

# This should print True since there is a cycle in the linked list
print(hasCycle(node1))  
