class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # i. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ii. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # iii. Delete a node by key
    def delete_node(self, key):
        current = self.head

        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Key not found

        prev.next = current.next
        current = None

    # iv. Display the linked list
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
