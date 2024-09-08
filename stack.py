def push(a,val):
    a.append(val)
    print("value entered succesfully")
def popitem(a):
    x=a.pop()
    print(x,"popped succesfully")    
def peak(a):
    i=len(a)-1
    print("peak element=",a[i])    
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])  


a=[]

while True:
    ch=int(input(" 1--> push \n 2--> pop \n 3--> peak\n 4--> display\n 5--> exit\n o-->  "))
    
    if ch==1:
        val = int(input("enter element to push"))
        push(a,val)
        
    elif ch==2:
        if len(a)==0:
            print("stack overflow") 
        else:
            popitem(a)     
             
    elif ch==3:
        if len(a)==0:
            print("stack overflow")
        else:
            peak(a) 
                        
    elif ch==4:
        if len(a)==0:
            print("stack over") 
        else:
            display(a)
            
    else:
        break    
     
     
print(a)