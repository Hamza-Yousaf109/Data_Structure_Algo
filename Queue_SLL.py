"""queue with singly link list"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        #agar queue kahli ha
        n=Node(data) 

        if self.is_empty():
            self.front=n
            self.rear=n
        else:
             #queue kahli nhi ha 
             #yani akhri node jo rear ha us k next me new node ka next n k baraber kr do
             self.rear.next=n
             self.rear 
             #rear me b chnges krni ha ab last yani new node ko rear k equl krna ha 
             self.rear=n 
        self.item_count+=1
    def dequeue(self):
        #queue kahli nhi ha 
        if self.is_empty():
            raise IndexError
        #agar queue me 1 hi node ha 
        elif self.front==self.rear:
            self.front=None
            self.rear=None
            #agar 1 sy zayada ha nodes ha 
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue ")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            return self.rear.item
    def size(self):
        return self.item_count()    
q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.get_front(),("  "),q.get_rear())
q.dequeue()
print(q.get_front(),("  "),q.get_rear())


           
            


              

            

        