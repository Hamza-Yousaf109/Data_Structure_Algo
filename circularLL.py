"""circular link list"""
#node bnany ka tareeqa
class Node:

    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class cll:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None


    def insert_at_start(self,data):
        #node me data rakh dia phir us me next ko filhaal None rakaha
        n=Node(data)
        #condition 1>> Ho sakta ha new node akela hi or list empty hu
        if self.is_empty():
            #n.next jo k new node ka next ha usi ko n kr do ta k wo khud ko refer krny lag pary
            
            n.next=n
            #ab us k last me changes krni ha ta k jo list me 1 hi node ha wohi last ho jay
            self.last=n
        else:
            #agr list me already nodes hain 

            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp

            temp=temp.next
        if temp.item==data:
            return temp 
        return None  
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print(self):
        if not self.is_empty():

          temp=self.last.next
          while temp!=self.last:
              print(temp.item)
              temp=temp.next
          print(self.item)  
    def del_first(self):
        if  not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next =self.last.next.next
    def del_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    def del_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                 if self.last.next.item==data:
                     self.del_first()
                 else:   
                       temp=self.last.next
                       while temp !=self.last:
                           if temp.next== self.last:
                               if self.last.item==data:
                                 self.del_last()
                               break
                           if temp.next.item==data:
                               temp.next=temp.next.next
                               break
                           temp=temp.next

    def __iter__(self):
        if self.last==None:
           return  clliterator(None)  

        else:
            return clliterator(self.last.next)

class  clliterator:
    def __init__(self,start):
        self.current=start
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        if self.current==self.start:
            raise StopIteration

        return data
    
cll=cll()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
cll.print()
for x in cll:
    print(x)



        
        



                           
                               







                 



             




          












        



                 









