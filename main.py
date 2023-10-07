def math_string():
    math_status = True
    user = input("What is your name?\n")
    # char_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "(", ")", "*"]
    while math_status:
        input_string = input(f"Dear {user}! Please, input your mathematical expression, \nhere: ")
        if "/0" in input_string or "/ 0" in input_string:
            result = "No_result"
            print(f"Wrong, {user}! Null division!\nresult = {result} \nTry again.")
        else:
            result = eval(input_string)
            print(result)
            new_expression = input(f"{user}, Try again? (y/n)\n")
            if new_expression != "y":
                math_status = False
                print(f"Good buy, {user}!")


if __name__ == "__main__":
    math_string()
