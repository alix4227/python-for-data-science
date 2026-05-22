def square(x: int | float) -> int | float:
    return(x ** 2)
def pow(x: int | float) -> int | float:
    return(x ** x)
def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return(float(x))
    return (inner)