import math

'''
    A SIMPLE CALCULATOR IN PYTHON
        # 1. ADD
        # 2. SUBTRACT 
        # 3. MULTIPLY 
        # 4. DIVIDE 
'''
while True:
    print("See below options for possible operations:")
    print("Type 1 to Add")
    print("Type 2 to Subtract")
    print("Type 3 to Multiply")
    print("Type 4 to Divide")
    print("Type 5 to Exit")

    operator = input("Enter either: (1, 2, 3, 4 or 5)")
    
    #To stop the Loop
    if operator == "5":
        print("Exiting calculator... Goodbye!")
        break  
    
    #I want users to be redirected to the right operation
    if operator not in ["1", "2", "3", "4", "5"]:
        print("Invalid operation. Please choose 1-5.")
        continue

    num1=input("Enter your first number:")
    num2=input("Enter your second number:")

    if not (num1.isnumeric() and num2.isnumeric()):
        print("Type a valid number! (1-5)")
        continue

    #converts default str to float
    num1=float(num1)
    num2=float(num2)

    #Conditional Statements 
    if operator == "1":
        result = num1 + num2
        print("The addition is:", result)
    elif operator == "2":
        result = num1 - num2
        print("The difference is:", result)
    elif operator == "3":
        result = num1 * num2
        print("The product is:", result)
    elif operator == "4":
        result = num1 / num2
        print("The result is:", result)

    


    


