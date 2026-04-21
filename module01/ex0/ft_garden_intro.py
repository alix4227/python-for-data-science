import sys


def main(args):

    try:
        if (args.len() != 4):
            raise Exception

        name: str = args[1]
        height: int = int(args[2])
        age: int = int(args[3])
        print("=== Welcome to My Garden ===")
        print(f'Plant: {name}')
        print(f'Height: {height}cm')
        print(f'Age: {age} days')
        print()
        print("=== End of Program ===")

    except Exception:
        print("Wrong number of arguments")
    except ValueError:
        print("Wrong number of arguments")


if __name__ == "__main__":
    main(sys.argv)
