import sys

def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        yield from [item for item in iterable if item]
    else:
        yield from [item for item in iterable if function(item)]

def main(args):
    try:
        if (len(args) != 3):
            raise AssertionError("Wrong number of arguments")
        if not isinstance(args[1], str) :
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(lambda s: len(s) > int(args[2]), args[1])))
    except AssertionError as e:
        print(f'AssertionError: {e}')
    except ValueError:
        print(f'AssertionError: the arguments are bad')
    


if __name__ == "__main__":
    main(sys.argv)