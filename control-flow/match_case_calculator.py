 Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        print(f"The result is {num1+num2}.")
    case "-":
        print(f"The result is {num1-num2}.")
    case "*":
        print(f"The result is {num1*num2}.")
    case "/":
            match num2:
                case 0:
                    print("Cannot divide by  zero") 
                case _ :
                    print(f"The result is {num1/num2}.")
