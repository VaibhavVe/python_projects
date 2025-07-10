try:
    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))

    print("What kind of operation do you want to perform.\nPress + for addition\nPress - for subtraction\nPress * for multiply\nPress / for divide")
    o = input("Enter the Operation:")

    match o:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}") 
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")   
except Exception as e:
    print("Enter a valid value...!")