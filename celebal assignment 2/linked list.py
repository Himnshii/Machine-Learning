class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Added {data} as the head of the list.")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added {data} to the end of the list.")

    def print_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise ValueError("Index must be a positive integer.")
            if n == 1:
                deleted_value = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position 1 with value {deleted_value}")
                return
            current = self.head
            prev = None
            count = 1
            while current and count < n:
                prev = current
                current = current.next
                count += 1
            if current is None:
                raise IndexError("Index out of range. No such node to delete.")
            prev.next = current.next
            print(f"Deleted node at position {n} with value {current.data}")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    ll.print_list()

    ll.delete_nth_node(2)
    ll.print_list()

    ll.delete_nth_node(1)
    ll.print_list()

    ll.delete_nth_node(10)
