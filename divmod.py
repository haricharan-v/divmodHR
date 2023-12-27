def dividedfunc(para_a, para_b):
    div_output = para_a // para_b
    mod_output = para_a % para_b
    divmod_output = divmod(para_a, para_b)

    print(f"\nThe divided result is: {div_output}")
    print(f"The remainder of the two inputs is: {mod_output}")
    print(f"The divmod result is: {divmod_output}")


input_a = int(input("Enter the first number: "))
input_b = int(input("Enter the second number: "))

dividedfunc(input_a, input_b)
