class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("none")        