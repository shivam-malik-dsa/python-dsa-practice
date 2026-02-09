class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

def evaluate_postfix(expression):
    stack=Stack()

    for ch in expression:
        
        if ch.isdigit():
            stack.push(int(ch))

        else:
            b=stack.pop()
            a=stack.pop()
        
            if ch == "+":
                stack.push(a+b)
        
            elif ch == "-":
                stack.push(a-b)
        
            elif ch == "*":
                stack.push(a*b)
        
            elif ch == "/":
                stack.push((a//b))

    return stack.pop()    
