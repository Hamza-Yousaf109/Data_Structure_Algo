"""Stack with Inheriting Singly Linklist"""
from Singlylist import *
class stack(Sll):
    def __init__(self):
        super().__init__()

        self.count_item=0
        
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.count_item+=1
    def pop(self):
        if not self.is_empty():
            self.del_at_first()
            self.count_item-=1
    def peek(self):
        if not self.is_empty():

           return self.start.item  
        else:
            raise IndexError
    def size(self):
        return self.count_item
s=stack()
s.push(10)
s.push(20)
s.push(30)
print("the peek value is ",s.peek())
s.pop()
print("the peek value is ",s.peek())
print()


