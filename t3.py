def pr(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
    
no = int(input("enter your number"))

if pr(no) == True:
     print(no*2)
else:
     print(no/2)