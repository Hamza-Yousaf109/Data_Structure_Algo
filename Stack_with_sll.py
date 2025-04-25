"""stack with singly linklist"""

from Singlylist import *
class stack:
    def __init__(self):
        self.mylist=Sll()
        self.item_count=0
    def is_empty(self):
         return self.mylist.is_empty() 
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
           self.mylist.del_at_first
           self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.item_count
s=stack()
s.push(10)
s.push(20)
s.push(30) 
print("top item is",s.peek())
s.pop()
print("top item is",s.peek())
print
