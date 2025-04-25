"""Deque using list """

class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def del_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty  ")
        else:
            self.items.pop(0)
    def del_rear(self):
        if self.items():
            raise IndexError("Deque is empty")
        else:
            self.items.pop(-1)
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[0]
    def get_rear(self):

        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
                 
            return self.items[-1]
    def size(self):
        return len(self.items)
        
d=Deque()
d.insert_front(20)
d.insert_rear(30)
print(d.get_front(),d.get_rear())                       


