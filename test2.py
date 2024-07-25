x = int(input("enter yoyr value"))

for i in range(2,x):
    
    if x == 1:
        print("invalid no.")
    
    if  (x % i) == 0:
        print(x*2)
    
    else:
        print(x/2)
