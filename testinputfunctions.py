"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs a float (digits with at most one
    decimal point), using the prompt. Return the float."""
    while True:
        theString = input(prompt)

        if theString.replace('.', '', 1).isdigit():
            return float(theString)
        else:
            print("Error: the input must consist of digits or digits with one decimal point")


def main():
    n = inputInt("Please enter a number: ")
    print(n)

    f = inputFloat("Please enter a floating-point number: ")
    print("You entered float:", f)

    

if __name__ == "__main__":
    main()
