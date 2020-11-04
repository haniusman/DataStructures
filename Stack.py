class Stack:
    def __init__ (self):
        self.stack = []
        
    def push(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False
            
    def pop(self):
    
        if len(self.stack) <= 0:
           print("Stack Empty") 
        else:
           self.stack.pop()
        
s = Stack()
s.push(3)
s.push(4)
s.pop()
        
