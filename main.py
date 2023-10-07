math_status = True
while math_status:
    input_string = input("Please, input your mathematical expression, \nhere: ")
    if "/0" in input_string or "/ 0" in input_string:
        result = "No_result"
        print(f"Wrong! Null division!\nresult = {result} \nTry again.")
    else:
        result = eval(input_string)
        print(result)
        new_expression = input("Try again? (y/n)\n")
        if new_expression != "y":
            math_status = False
