def display(self):
    values = []
    temp = self.head
    while temp:
        values.append(str(temp.data))
        temp = temp.next
    print(" -> ".join(values))