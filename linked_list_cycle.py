
class Solution(object):
    def hasCycle(self, head):
        t = r = head
        while r and r.next:
            r = r.next.next
            t = t.next
            if r==t:
                return True
        return False
