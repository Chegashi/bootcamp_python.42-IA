def text_analyzer(*texts):
    """    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if len(texts) != 1:
        print("ERROR")
    elif len(texts) == 0 and len(texts[1]) == 0:
        print("What is the text to analyse?")
    e# Exercise 04 - Elementary

|                         |                    |
| -----------------------:| ------------------ |
|   Turn-in directory:    |  ex04              |
|   Files to turn in:     |  operations.py     |
|   Forbidden functions:  |  None              |
|   Remarks:              |  n/a               |

You will have to make a program that prints the results of the four elementary mathematical operations of arithmetic (addition, subtraction, multiplication, division) and the modulo operation. This should be accomplished by writing a function that takes 2 numbers as parameters and returns 5 values, as formatted in the console output below.

**Example:**

```console
> python operations.py 10 3
Sum:         13
Difference:  7
Product:     30
Quotient:    3.3333333333333335
Remainder:   1
>
> python operations.py 42 10
Sum:         52
Difference:  32
Product:     420
Quotient:    4.2
Remainder:   2
>
> python operations.py 1 0
Sum:         1
Difference:  1
Product:     0
Quotient:    ERROR (div by zero)
Remainder:   ERROR (modulo by zero)
>
> python operations.py
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
>
> python operations.py 12 10 5
InputError: too many arguments

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
>
> python operations.py "one" "two"
InputError: only numbers

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
>
> python operations.py "512" "63.1"
InputError: only numbers

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
```
lse:
        nbr_upper = 0
        nbr_lower = 0
        nbr_space = 0
        nbr_ponctuation = 0
        for c in texts[0]:
            if c.isupper():
                nbr_upper += 1
            elif c.islower():
                nbr_lower += 1
            elif c.isspace():
                nbr_space += 1
            elif not c.isdigit():
                nbr_ponctuation += 1
        print('The text contains characters:', len(texts[0]))
        print("- ", nbr_upper, " upper letters")
        print("- ", nbr_lower, " lower letters")
        print("- ", nbr_ponctuation," punctuation marks")
        print("- ", nbr_space," spaces")
