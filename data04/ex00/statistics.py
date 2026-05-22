from typing import Any


def var(args):
    total = 0
    for nb in args:
        total += nb
    mean = total / len(args)
    list_nb = [(nb - mean) ** 2 for nb in args]
    sum_list = sum(list_nb)
    var = sum_list / len(args)
    return (var)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for a, b in kwargs.items():
        total = 0
        if (not args):
            print('ERROR')
        elif b == 'mean':
            for nb in args:
                total += nb
            print(total / len(args))
        elif b == 'median':
            sorted_nb = sorted(args)
            n = len(sorted_nb)
            print(f'median: {sorted_nb[n//2]}')
        elif b == 'quartile':
            sorted_nb = sorted(args)
            n = len(sorted_nb)
            quartiles_nbs = []
            quartiles_nbs.append(float(sorted_nb[n//4]))
            quartiles_nbs.append(float(sorted_nb[n*3//4]))
            print(f'quartile: {quartiles_nbs}')
        elif b == 'var':
            print(f'var: {var(args)}')
        elif b =='std':
            std = pow(var(args), 0.5)
            print(f'std : {std}')