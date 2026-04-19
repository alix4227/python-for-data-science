import sys


def print_variables(nb, up, low, space, marks, text):
    print(f'The text contains {len(text)} characters:')
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{space} spaces")
    print(f"{nb} digits")


def main(args):
    """
    takes a single string argument
    and displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits, and spaces
    """
    nb = up = low = space = marks = 0
    try:
        if len(args) > 2:
            raise AssertionError("more than one argument is provided")
        if len(args) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = args[1]
        for i in range(len(text)):
            if text[i].isdigit():
                nb += 1
            elif text[i].isupper():
                up += 1
            elif text[i].islower():
                low += 1
            elif text[i].isspace():
                space += 1
            else:
                marks += 1
        print_variables(nb, up, low, space, marks, text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)
