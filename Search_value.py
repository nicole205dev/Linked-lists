def search(self, value):
    temp = self.head
    index = 0
    while temp:
        if temp.data == value:
            return index
        temp = temp.next
        index += 1
    return -1


