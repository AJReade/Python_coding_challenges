# Task 1
total = 0                    
for number in range(11):    #range produes a list 0-10 to iterate through     
   total += number
print(total)
#Challenge
def sum_up_to_my_number():
    total = 0
    try :
        my_number1 = int(input("Please enter your start number: "))  #user inputs
        my_number2 = int(input("Please enter your end number: "))
        for number in range(my_number1, my_number2+1):
            total += number
        return total
    except ValueError:    # prevents entry of a float
         return "Please enter integers only try again!"
   
    
#print(sum_up_to_my_number())

#2
count = 0
total_new = 0
while count <11:
    total_new = total_new + count
    count +=1
print(total_new)

# 2 - Challenge
def add_up():
    try:
        total_new = 0
        count = int(input("Enter a starting value: "))
        end = (int(input("Enter a starting value: ")) + 1)
        while count < end:
            total_new = total_new + count
            count +=1
        return total_new
    except ValueError: 
        return "Please enter integers only"

#print(add_up())

#3
def add_up_do():
    try:
        total_new = 0
        count = int(input("Enter a starting value: "))
        end = (int(input("Enter a starting value: ")) + 1)
        if count > end:
            return "Error"
        while True:
            total_new = total_new + count
            count +=1
            if count == end:
                break
        return total_new
    except ValueError: 
        return "Please enter integers only"

#print(add_up_do())

#4 - Array

array = [2,4,6,8,10,12,14,16,18,20]
new_array = []
for number in array:
    new_array.append(number)
for number in new_array:
    print(number)

#2D Array
cols,rows = (5,5) #columns and rows for 2d array defined
array_2d = []           #declarin empty variable to append to 
for i in range(1,rows+1): 
    row = []
    for j in range(1,cols+1):
        row.append(j*i)
    array_2d.append(row)
for row in array_2d:
    print(row)

#function task
def calcu():
    inpt = True
    while inpt == True:
        try:
            inpt = False
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            num3 = int(input("Chose operation: 1 for +, 2 for -, 3 for x, 4 for /: "))
            if num3 not in range(1,5):
                print("Only enter 1, 2, 3 or 4!")
                inpt = True
            elif num3 == 1:
                return num1 + num2
            elif num3 == 2:
                return num1 - num2
            elif num3 == 3:
                return num1 * num2
            else:
                return num1 / num2
        except ValueError:
            print("Only enter 1, 2, 3 or 4!")
            inpt = True

print(calcu())   

