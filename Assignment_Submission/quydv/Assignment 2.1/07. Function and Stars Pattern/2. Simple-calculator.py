def calculator(x, operator, y):
    if operator == "+" or operator == "add":
        return (x+y)
    elif operator == "-" or operator == "subtract":
        return (x-y)
    elif operator == "*" or operator == "multiply":
        return (x*y)
    elif operator == "/" or operator == "divide":
        return (x/y)

ask = input("Enter a calculation using space as delimiter: ")
ask_list = [ask for ask in ask.split()]
ask_list[0] = int(ask_list[0])
ask_list[2] = int(ask_list[2])

print(calculator(ask_list[0], ask_list[1], ask_list[2]))
