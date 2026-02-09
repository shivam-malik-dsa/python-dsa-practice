class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return "under flow"
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items)==0


def is_balance(expression):
    stack=Stack()
    pair={")":"(","]":"[","}":"{"}

    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty():
                return False

            top=stack.pop()
            if pair[ch]!=top:
                return False    
        
    return stack.is_empty()
