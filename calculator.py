while True:
    user_first_input = float(input("Insert the first number: "))
    operator = input("Insert the operator (+ , -, *, /): ")
    user_second_input = float(input("Insert the second number: "))

    if operator == "+":
        print(user_first_input + user_second_input)
    elif operator == "-":
        print(user_first_input - user_second_input)
    elif operator == "*":
        print(user_first_input * user_second_input)
    elif operator == "/":
        print(user_first_input / user_second_input)
    else:
        print("Invalid operator")

    Exit = input("Do you want to exit? (Yes/No): ")
    if Exit == "Yes":
        break
