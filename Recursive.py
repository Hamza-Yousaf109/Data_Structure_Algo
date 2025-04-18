"""recursive Function"""
#print First Nutural NUmbers

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')

##print First Nutural NUmbers In reverse order 
def printNreverse(n):
    if n>0:
        print(n,end=' ')
        printNreverse(n-1)

#print First odd Nutural NUmbers         

def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1,end=' ')

#print First even Nutural NUmbers     

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=' ')

##print First odd NUmbers In reverse order 

#print First odd Nutural NUmbers         

def printNoddr(n):
    if n>0:
        print(2*n-1,end=' ')
        printNoddr(n-1)
        

#print First even Nutural NUmbers     

def printNevenr(n):
    if n>0:
        print(2*n,end=' ')
        printNevenr(n-1)
       
printNoddr(10)
