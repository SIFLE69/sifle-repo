numb= int(input("ener a no"))
summ = 1
if numb>0:

    for i in range(numb,0,-1):
         summ  = summ*i
    print(summ)
elif numb == 0:
     print("factorial is 1")

else:
     print("no factorial available")