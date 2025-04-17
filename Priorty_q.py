"""Priorty Queue """
class priortyQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priorty):
        index=0
        while index<len(self.items) and self.items[index][1]<=priorty:
            index+=1
        self.items.insert(index,(data,priorty))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("emoty Priorty Q")  
        
        return self.items.pop(0)[0]  
    def size(self):
        return len(self.items)   

p=priortyQueue()
p.push("hamza ",4)
p.push("hammmad",5)
p.push("huma",1)
p.push("hamasa",5)
p.push("hamza",5)
while not p.is_empty():
 print(p.pop())