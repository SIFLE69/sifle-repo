n1 = input()
n2 = input()




try:
    n1 = int(n1)
except ValueError:
    print("invalid you need to enter a no. in n1")
    s = (True)

try:
    n2 = int(n2)
except ValueError:
    print("invalid you need to enter a no in n2.")
    b = (True)


if s or b ==(True):
    exit

    

if (n1>n2):
     print(n1,"is the greater no.")

elif(n1<n2):
    print(n2,"is the greater no.")

else:
     print("both are equal")





