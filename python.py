print("Simple Calculator Program!")


# Here calculator Simple Program

# Calculator Extra Function

user = int(input("Enter first number: "))
user1 = int(input("Enter second number: "))
operators = input("Choose Symbol + - * / // % **: ")

if operators == "+":
    print(user + user1)

elif operators == "-":
    print(user - user1)

elif operators == "*":
    print(user * user1)

elif operators == "/":
    print(user / user1)

elif operators == "//":
    print(user // user1)

elif operators == "%":
    print(user % user1)

elif operators == "**":
    print(user ** user1)

else:
    print("Invalid Symbol!")