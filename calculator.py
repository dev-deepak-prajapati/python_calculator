#--------------BASIC CALCULATOR------------------------

print("""
==============================
        BASIC CALCULATOR
==============================
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Exponantial/power
==============================
""")
    

try:
    
    choice = int(input("Choose option : "))
    print()
    
    flag = True
    
    if choice < 1 or choice > 5:
        print("Please choose correct option.")
        flag = False 
    else :
        
        num1 = float(input("Enter number 1:"))
        num2 = float(input("Enter number 2:"))
        print()
        
        answer = None
        opr = None
        
        match choice :
            case 1:                
                answer = num1 + num2
                opr = "+" 
            case 2:
                answer = num1 - num2
                opr = "-"
            case 3:
                answer = num1 * num2
                opr = "*"
            case 4:
                answer = num1 / num2
                opr = "/"
            case 5:
                answer = num1 ** num2
                opr = "**"
           
except ZeroDivisionError :
    print("You can't divide by zero.")
    
except ValueError:
    print("Please enter valid number.")
    
else:
    if flag:
        print(f"{num1} {opr} {num2} = {answer}")
    
    
    