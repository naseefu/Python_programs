class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            return

        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
linked_list = LinkedList()
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(1)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)

print("Original Linked List:")
linked_list.display()

linked_list.delete(3)
print("\nLinked List after deleting 3:")
linked_list.display()

linked_list.reverse()
print("\nReversed Linked List:")
linked_list.display()
