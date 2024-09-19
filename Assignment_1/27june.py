class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to add a new node at the beginning of the list
def pushNode(head_ref, data_val):
    # Allocate node
    new_node = Node(data_val)
    # Link the old list of the new node
    new_node.next = head_ref
    # Move the head to point to the new node
    return new_node

# Function to find the middle of the linked list
def getMiddle(head):
    slow = head
    fast = head
    # Traverse over the entire linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

# Driver Code
head = None
for i in range(8, 0, -1):
    head = pushNode(head, i)
print("Middle Value Of Linked List is:", getMiddle(head))