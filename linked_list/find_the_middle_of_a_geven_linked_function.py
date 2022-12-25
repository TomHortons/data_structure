# %%
# Q
'''
Given a singly linked list, find the middle of the linked list.
For example, if the given linked list is 1->2->3->4->5 then the output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print the second middle element.
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4.
'''

# %%
# Method1
'''
Method 1: Traverse the whole linked list and count the no. of nodes.
Now traverse the list again till count/2 and return the node at count/2.
Below is the implementation of the above approach:
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeOperation:
    def push_node(self, head_ref, data):
        new_node = Node(data)
        new_node.next = head_ref
        head_ref = new_node
        return head_ref

    def print_node(self, head):
        while (head != None):
            print('%d->' % head.data, end="")
            head = head.next
        print("NULL")

    def get_len(self, head):
        tmp = head
        length = 0

        while (tmp != None):
            length += 1
            tmp = tmp.next
        return length

    def print_middle(self, head):
        if head != None:
            length = self.get_len(head)
            tmp = head
            mid_idx = length // 2

            while mid_idx != 0:
                tmp = tmp.next
                mid_idx -= 1

            print('The middle element is [%d]' % tmp.data)


head = None
tmp = NodeOperation()
for i in range(5, 0, -1):
    print('i: [%d]' % i)
    head = tmp.push_node(head, i)
    tmp.print_node(head)
    tmp.print_middle(head)
# This code is contributed by Tapesh(tapeshdua420)

# %%
# Method 2
'''
Method 2: Traverse linked list using two-pointers.
Move one pointer by one and the other pointers by two.
When the fast pointer reaches the end, the slow pointer will reach the middle of the linked list.
'''

# Python3 program to find middle of linked list
# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    # Function that returns middle.
    def printMiddle(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head

        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # return the slow's data, which would be the middle element.
        print("The middle element is ", slow.data)


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()

 # Code is contributed by Kumar Shivam (kshivi99)

# %%
# Method 3
'''
Method 3: Initialize the mid element as head and initialize a counter as 0.
Traverse the list from the head, while traversing increment the counter and change mid to mid->next whenever the counter is odd.
So the mid will move only half of the total length of the list.
Thanks to Narendra Kangralkar for suggesting this method.
'''

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class contains a Node object


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    # Function to get the middle of
    #  the linked list
    def printMiddle(self):
        count = 0
        mid = self.head
        heads = self.head

        while (heads != None):

            # Update mid, when 'count'
            # is odd number
            if count & 1:
                mid = mid.next
            count += 1
            heads = heads.next

        # If empty list is provided
        if mid != None:
            print("The middle element is ", mid.data)


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()

# This Code is contributed by Manisha_Ediga
