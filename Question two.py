class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def findCycleStart(head):
    if not head or not head.next:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  


start_of_cycle = findCycleStart(node1)
if start_of_cycle:
    print("Start of cycle:", start_of_cycle.val) 
else:
    print("No cycle found")
