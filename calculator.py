num1 = int(input("Enter the value of A: "))
num2 = int(input("Enter the value of B: "))

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Enter the values again")
    print("6. Exit")
    
    k = int(input("Enter your choice: "))
    
    match k:
        case 1:
            result = num1 + num2
            print("Addition: ", result)
        
        case 2:
            result2 = num1 - num2
            print("Subtraction: ", result2)
        
        case 3:
            result3 = num1 * num2
            print("Multiplication: ", result3)
        
        case 4:
            if num2 != 0:
                result4 = num1 / num2
                print("Division: ", result4)
            else:
                print("Error! Division by zero is not allowed.")
        case 5:
            num1 = int(input("Enter the value of A: "))
            num2 = int(input("Enter the value of B: "))
        case 6:
            print("Exiting the program")
            break
        
        case _:
            print("Invalid choice")
