# import sys


def strlen(string):
    return (len(string) > 2)


def ft_filter(function, iterable):
    if function == None:
        yield from [item for item in iterable if item]
    else: 
        yield from [item for item in iterable if function(item)]


def main():
    test = ["lechat", "lechien"]
    print(ft_filter(None,test))
    # print(filter.__doc__)


if __name__ == "__main__":
    main()
