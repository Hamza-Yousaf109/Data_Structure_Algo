"""singly linklist """
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Sll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start ==None 
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data,) 
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n 
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None 
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def del_at_first(self):
        if self.start is not None:
            self.start=self.start.next
    def del_at_end(self):
        """agar list kahli ha """
        if self.start is None:
            pass
        #agar sirf 1 node ha 
        elif self.next is None:
            self.start=None
            #pahly temp sy check kro kon sa last ha then del kro
        else:
             temp=self.start
             while temp.next.next is not None:
                temp=temp.next
             temp.next=None
    def del_item(self,data):
        #agar koi node nhi
        if self.start is None:
            pass
        #agar node ha tu kya item k sath data match ho raha ha ya check kro
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
                #temp sy pata kro data ka
            else:
                temp=self.start
                if temp==data:
                    self.start=temp.next
                else:    
                  while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return Slliterable
        #ist step iterable yani loop banay ka tareeqa                    
class Slliterable:
    #init fun sy 1 veriable pass kro 
    def __init__(self,start):
        self.current=start
        #iter 1 fun bnao jis ko return kr k choor do
    def __iter__(self):
        return
        #next name ka fun bnao jis me jo data hu 1 1 kr ky return krwao
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item 
        self.current= self.current.next
        return data 
        
#uper jis class ko iterable banana ha us me fun bnao iter k name ka or asy return krwao

#def __iter__(self):
        #return Slliterable






             

"""
#Driver code
mylist=Sll()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
#mylist.insert_after(mylist.search(20),25)


mylist.print_list()
#for x in mylist:
 #   print(x)
 """