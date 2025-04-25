"""Doubly Circular LL"""

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        if self.start is None:
            return None
    def insert_at_start(self,data):
        n=Node(item=data) 
        if self.is_empty():
            #agar link empty ha tu wo new node khud ko hi point kry ga
            n.next=n
            n.prev=n
            #node k andar data ,next,prev wala data rekhna
        else:
            n.next=self.start
            n.prev=self.start.prev
            #list k andr 2 ya 2 sy zyada nodes hain 
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
         n=Node(data) 
         if self.is_empty():
            #agar link empty ha tu wo new node khud ko hi point kry ga
            n.next=n
            n.prev=n
            self.start=n
            #node k andar data ,next,prev wala data rekhna
         else:
             n.next=self.start
             n.prev=self.start.prev
             #ab list me ya new node last me attach krna ha 
             n.prev.next=n
             self.start.prev=n
    def search(self,data):
        #list me loop k lia temp ko ly raha hu as a start
        temp=self.start
        #list k first node k lia alag sy search kia gya ha 
        if temp==None:
         return None
        if temp.item==data:
            return temp
        else:
            #ab temp agy agy move ho ga
            temp=temp.next

          #ab 1 loop lagy gi 
    
        while temp!=self.start:
            #agar data mila tu return kr dy ga wrna next hota jay ga or then na mila tu None return ho ga

            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            #node k andar data ,next,prev wala data rekhna
            n=Node(data)
            n.next=temp.next
            n.prev=temp
            #list k sath ab attach krna ha 
            temp.next.prev=n
            temp.next=n
    def print(self):
        temp=self.start
        if temp is not None:
            print(temp.item)
            temp=temp.next
            while temp!=self.start:
                print(temp.item)
                temp=temp.next
    def del_first(self):
        if self.start is not None:
            #agar single node ha list me 
            if self.start.next==self.Start:
                self.start=None
                #agar list me 1 sy zayada nodes hain 
            else:
                 self.start.prev.next=self.start.next
                 self.start.next.prev=self.start.prev
                 self.start=self.start.next
    def del_last(self):
        if self.start is not None:
            #agar single node ha list me 
            if self.start.next==self.Start:
                self.start=None
                #agar list me 1 sy zayada nodes hain 
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def del_item(self,data):
        #yani list me 1 sy zayada nodes hain
        if self.start is not None:
           
          temp=self.start
          if temp.item==data:
                 self.del_first()
          else:
              temp=temp.next
              while temp is not self.start:
                  if temp.item==data:
                      temp.next.prev=temp.prev
                      temp.prev.next=temp.next

mylist=CDLL()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(40)
mylist.insert_after(CDLL.search(30),35)
print()
                      
                      
                  
                    

































             
         







        
                        
    