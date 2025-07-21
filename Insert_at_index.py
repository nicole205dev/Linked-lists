def Node(data):
    pass


def insert_at_index(self, index, data):
    if index < 0:
        raise IndexError("Index cannot be negative")
    new_node = Node(data)
    if index == 0:
        self.insert_at_start(data)
        return
    temp = self.head
    for i in range(index - 1):
        if not temp:
            raise IndexError("Index out of range")
        temp = temp.next
    if not temp:
        raise IndexError("Index out of range")
    new_node.next = temp.next
    temp.next = new_node