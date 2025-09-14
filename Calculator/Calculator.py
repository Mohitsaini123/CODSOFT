def Menu():
    print("Choose any one of the following optitons : \n")
    while True:

        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. exit")

        choice = int(input("Enter your choice (1-4): "))

        if(choice == 5):
            print("Thank you !")
            break
        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        

        match choice:
            case 1:
                print("Result:", a + b)
            case 2:
                print("Result:", a - b)
            case 3:
                print("Result:", a * b)
            case 4:
                if b == 0:
                    print("Error! Division by zero.")
                else:
                    print("Result:", a / b)
            case _:
                print("Invalid choice!")



Menu()