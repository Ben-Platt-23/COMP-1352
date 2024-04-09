class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        current = self.head
        while current:
            result += str(current.data) + " "
            current = current.next
        result = result.rstrip()
        result += "]"
        return result

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        removed_value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed_value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        if self.size == 1:
            removed_value = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            removed_value = current.next.data
            current.next = None
        self.size -= 1
        return removed_value

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.remove_first()
        current = self.head
        for _ in range(index - 1):
            current = current.next
        removed_value = current.next.data
        current.next = current.next.next
        self.size -= 1
        return removed_value

# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.add_first(1)
    linked_list.add_last(2)
    linked_list.add_last(3)
    print(linked_list)  # Output: [1 2 3]
    print(linked_list.get_size())  # Output: 3
    print(linked_list.is_empty())  # Output: False
    print(linked_list.remove_first())  # Output: 1
    print(linked_list.remove_last())  # Output: 3
    print(linked_list)  # Output: [2]
