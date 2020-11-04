class Queue:
    def __init__ (self):
        self.queue = []
        
    def enqueue(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            print(self.queue)
            return True
        else:
            return False
            
    def dequeue(self):
    
        if len(self.queue) <= 0:
           print("Queue Empty") 
        else:
           self.queue.pop()
           print(self.queue)
        
s = Queue()
s.enqueue(3)
s.enqueue(4)
s.dequeue()
s.enqueue(8)
s.dequeue()
s.dequeue()
