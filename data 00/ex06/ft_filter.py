# import sys


def strlen(string):
    return (len(string) > 2)


def ft_filter(function, iterable):
    if function == None:
        yield from [item for item in iterable if item]
    else: 
        yield from [item for item in iterable if function(item)]


def main():
    test = [1, 10, 15, 8, 5]

    print(list(filter(None, test)))
    print(list(ft_filter(None, test)))

    print(list(filter(lambda s: s % 2 == 0, test)))
    print(list(ft_filter(lambda s: s % 2 == 0, test)))

if __name__ == "__main__":
    main()
