def reverse(self):
        p = None
        c = self.head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        self.head = p
        return p
                
