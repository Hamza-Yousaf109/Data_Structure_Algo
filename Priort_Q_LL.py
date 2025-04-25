"""priorty Queue with link list"""
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class priorityQ:
    def __init__(self):
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,priority)
        #agr ll none  ha --or-- jo new ki priority wo less ha existing first node sy
        if not self.start or priority <self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            #jab tak tep k next me none nhi ha --and-- temp jis ko point kr raha us ki priorty choti ha new node sy
            while temp.next!=None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next 
            temp.next=n
        self.item_count+=1    
    def is_empty(self):
        return self.start==None 
    def pop(self):
        if self.is_empty():
            raise IndexError("p-Queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
        
    def size(self):
        return self.item_count 
           
p=priorityQ()
p.push("Hamza",1)
p.push("Moon",4)
p.push("Arslan",2)
while not p.is_empty():
    print(p.pop())        





        

