# Mod Divmod

This Python script, titled "Mod Divmod," is designed to perform integer division and modulus operations on user-provided inputs.

## Usage

1. Run the script in a Python environment.
2. The program prompts the user to enter two integers (`input_a` and `input_b`).
3. The script calculates the quotient and remainder using both traditional operators and the built-in `divmod` function.
4. The results are displayed to the user through standard output.

## Code Structure

The script consists of a function named `dividedfunc` that takes two parameters (`para_a` and `para_b`). Within this function, the integer division (`//`), modulus (`%`), and `divmod` operations are performed.

```python
def dividedfunc(para_a, para_b):
    div_output = para_a // para_b
    mod_output = para_a % para_b
    divmod_output = divmod(para_a, para_b)

    print(f"\nThe divided result is: {div_output}")
    print(f"The remainder of the two inputs is: {mod_output}")
    print(f"The divmod result is: {divmod_output}")
```

The main part of the script takes user input, calls the `dividedfunc` function, and displays the results.

```python
input_a = int(input("Enter the first number: "))
input_b = int(input("Enter the second number: "))

dividedfunc(input_a, input_b)
```

## Input and Output

- **Input:** The user is prompted to enter two integers through standard input (`stdin`).
- **Output:** The script outputs the results of the integer division and modulus operations to standard output (`stdout`).

## Example

```
Enter the first number: 15
Enter the second number: 4

The divided result is: 3
The remainder of the two inputs is: 3
The divmod result is: (3, 3)
```

Feel free to explore and use this "Mod Divmod" script for your integer division and modulus calculations!
