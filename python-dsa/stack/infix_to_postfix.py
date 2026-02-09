class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items)==0
            
def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    return 0

def infix_to_postfix(expression):
    stack=Stack()
    result=""

    for ch in expression:
        if ch.isalnum():
            result+=ch

        elif ch == "(":
            stack.push(ch)

        elif ch == ")":
            while not stack.is_empty() and stack.peek() !="(":
                result+=stack.pop()
            stack.pop()

        else:
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(ch)):
                result+=stack.pop()
            stack.push(ch)                   
    
    while not stack.is_empty():
        result+=stack.pop()
    
    return result
