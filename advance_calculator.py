#---------------PYTHON CALCULATOR BY DEEPAK PRAJAPATI----------------


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

def floor_division(a,b):
    return a // b

def history(transactions):
    length = len(transactions)
    print(f"============== HISTORY ({length}) ===============")
    if length == 0:
        print("No calculations have been performed yet.")
        
    else:
        for transaction in transactions:
            print(transaction)
        
        
transactions = []  

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
7. Floor Division
8. History
9. Exit
=========================================
        """)
    
    choice = input("Enter your choice: ")
    
    if choice == "9":
        print("Thank you for using this calculator")
        break
    
    elif int(choice) < 1 or int(choice) > 9:
        print("Please choose correct choice !")
        continue
    
    elif choice == "8":
        history(transactions)
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
               
            case "7":
                result = floor_division(num1,num2)
                
        
        operators = ("+","-","*","/","%","**","//")
       
        transaction = "{} {} {} = {}".format(str(num1),operators[int(choice)-1],str(num2),str(result))
        transactions.append(transaction)
        
        print("Result = ", result)
    
    except ValueError:
        print("Please enter valid numbers.")
    
    except ZeroDivisionError:
        print("Can't divide by zero.")
        

                

