while True:

    print("Simple Calculator Program!")


# Here calculator Simple Program

# Calculator Extra Function

    user = int(input("Enter first number: "))
    user1 = int(input("Enter second number: "))
    operators = input("Choose Symbol + - * /: ")

    if operators == "+":
        print(user + user1)

    elif operators == "-":
        print(user - user1)

    elif operators == "*":
        print(user * user1)

    elif operators == "/":
        print(user / user1)

    else:
        print("Invalid Symbol!")

# User Voting Syestem

    print(f"{'*#######*':>20}{'User Voting System'}{'*#######*'}\n")

    user  = int(input(f"{'Enter your age: ':>30}"))

    if user >= 18:
        print(f"{'You Eligible To Vote':>33}")

    else:
        print(f"{'Not Eligible':>28}")
