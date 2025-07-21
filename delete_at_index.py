def delete_at_index(self, index):
    if index < 0:
        raise IndexError("Index cannot be negative")
    if not self.head:
        raise IndexError("List is empty")
    if index == 0:
        self.head = self.head.next
        return
    temp = self.head
    for i in range(index - 1):
        if not temp.next:
            raise IndexError("Index out of range")
        temp = temp.next
    if not temp.next:
        raise IndexError("Index out of range")
    temp.next = temp.next.next