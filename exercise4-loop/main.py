 #Part 1: Multiplication table
number = int(input("Enter a number:"))
for i in range(1, 11):
    print (number, "x", i, "=", number * i) 
    
    
# Part 2: Login system
attempts = 0
while attempts < 3:
    password = input("Enter password:")
    
    if password =="python123":
        print("Access granted")
        break
    else:
        attempts += 1 

        if attempts == 3:
            print("Access denied")
        