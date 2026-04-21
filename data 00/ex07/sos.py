import sys


def main(args):
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
}
    result = []
    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")
        string = args[1].upper()
        for item in string:
            if item.isspace() or item.isalnum():
                result.append(NESTED_MORSE[item])
            else:
                raise AssertionError("the arguments are bad")
        for i in range(len(result)):
            if i != len(result) - 1: 
                print(result[i], end=" ")
            else:
                print(result[i])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)