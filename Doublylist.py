"""Doubly linklist"""
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Dll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None   
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n            
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next !=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp ==None:
            self.start=n
        else:
            temp.next=n      


    def search(self,data):
        temp=self.start 
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        n=Node(temp,data,temp.next)
        if temp.next is not None:
            temp.next.prev=n
        temp.next=n
    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next
    def del_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def del_last(self):
        if self.start==None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp is not None:
                temp=temp.next
            temp.prev.next=None
    def del_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start 
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                       temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.start
                    break
                temp=temp.next           

    def __iter__(self):
        return Dlliterator(self.start)
class Dlliterator:
        def __init__(self,start):
            self.current=start
        def __iter__(self):
            return
        def __next__(self):
            if not self.current:
                raise StopIteration
            
            data=self.current.item
            self.current=self.current.next
            return data
mylist=Dll()
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.print
        










