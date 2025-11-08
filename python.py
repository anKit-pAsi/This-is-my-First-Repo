while True:

    print("\n*######*Main Menu*######*")
    print("Press 1 Go to Calculator")
    print("Press 2 Go to Voting System")
    print("Press 3 Exit")

    choice = input("Enter Your Choise 1/2/3")

    if choice == "1":
        print("\n Simple Calculator")

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operators = input("Choose Symbol | +, -, *, /: ")

        if operators == "+":
            print(a + b)

        elif operators == "-":
            print(a - b)

        elif operators == "*":
            print(a * b)

        elif operators == "/":
            print(a / b)

        else:
            print("Invalid Symbol")

        print("\n Press enter go to main menu")            

    elif choice == "2":
        # Simple Voting System

        user = int(input("Enter Your age: "))

        if user >= 18:
            print("You Eligible to Vote")

        else:
            print("Not Eligible to voting")

        input("\n Press enter to go main menu")
    
    elif choice == "3":
        print("Thanks for using the program")
        break

    else:
        print("Invalid choice! Please Try Again...")