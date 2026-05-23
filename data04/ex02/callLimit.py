
from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            if count > limit:
                return (print(f'Error: {function} call too many times'))
            return function(*args, **kwds)
        return limit_function
    return callLimiter
        