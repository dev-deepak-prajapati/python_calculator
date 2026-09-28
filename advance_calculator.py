def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def modulus(a,b):
    return a % b

def power(a,b):
    return a ** b


while True :
    print("""

=========================================
  PYTHON CALCULATOR BY DEEPAK PRAJAPATI
=========================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit
=========================================
        """)
    
    choice = input("Enter your choice: ")
    
    if choice == "7":
        print("Thank you for using this calculator")
        break
    elif int(choice) < 1 or int(choice) > 7:
        print("Please choose correct choice !")
        continue 

    try:
        print()
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        print()
        
        match choice:
            case "1":
                result = add(num1,num2)
            
            case "2":
                result = subtract(num1,num2)
            
            case "3":
                result = multiply(num1,num2)
            
            case "4":
                result = divide(num1,num2)
            
            case "5":
                result = modulus(num1,num2)
                
            case "6":
                result = power(num1,num2)
                
            case _:
                print("Invalid choice !")
                continue
        
        print("Result = ", result)
    
    except ValueError:
        print("Please enter valid numbers.")
    
    except ZeroDivisionError:
        print("Can't divide by zero.")
        

                
