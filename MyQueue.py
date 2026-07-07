class MyQueue :
    def __init__ (self):
        self.Queue = []
    def enqueue(self,val):
        self.Queue.append (val)
    def dequeue(self):
        if self.Queue:
            self.Queue.pop(0)
        else:
            print('Queue is empty')
    def is_empty(self):
        return len(self.Queue) == 0
    def display(self):
        if self.Queue:
            return self.Queue
        else:
            print('no Queue to display')
    def size(self):
        return len(self.Queue)
