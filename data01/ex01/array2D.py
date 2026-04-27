import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    print(f'My shape is : {arr.shape}')
    print(f'My new shape is : {arr[start:end].shape}')
    return(arr[start:end].tolist())
