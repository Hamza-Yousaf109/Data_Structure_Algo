"""deque with doubly linklist"""
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.items_count=0
    def is_empty(self):
        return self.front==None
    def insert_front(self,data):
        n=Node(data,None,self.front)
        #agar koi b Node nhi ha 
        if self.is_empty():
            #tab front or rear usi node ko point kry ga
            self.front=n
            self.rear=n
        #agar nodes hain
        else:
            self.front.prev=n
            self.front=n
        self.items_count+=1    
    def insert_rear(self,data):
        n=Node(data,self.rear,None)
        if self.is_empty():
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.items_count+=1    
    def del_front(self):
        if self.is_empty():
            raise IndexError("empty ha bahi sab kya dekhty hu")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.items_count-=1  
    def del_rear(self):
        if self.is_empty():
            raise IndexError("empty ha bahi sab kya dekhty hu")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.items_count-=1 
    def get_front(self):
        if self.is_empty():
            raise IndexError("empty ha bahi sab kya dekhty hu")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("empty ha bahi sab kya dekhty hu")
        else:
            return self.rear.item
    def size(self):
        return self.items_count
q=Deque()
q.insert_front(10)
q.insert_front(20)
q.insert_rear(100)
print(q.get_front(),q.get_rear()     )
print(q.size())

    


        



                






        



