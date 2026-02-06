class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:  
    def __init__(self):
        self.head = None

    def insert_at_position(self,data,pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return
    
        temp = self.head
        i = 0
        while temp is not None and i < pos-1:
            temp = temp.next
            i += 1
    
        if temp is None:
            print("out of range")
            return
    
        new.next = temp.next
        temp.next = new    

    def delete_at_position(self,pos):
        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        i = 0
        while temp is not None and i < pos-1:
            temp = temp.next
            i += 1

        if temp is None or temp.next is None:
            print("out of range")
            return

        temp.next = temp.next.next  

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("none")