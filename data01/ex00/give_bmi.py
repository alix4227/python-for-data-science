import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h = np.array(height)
    w = np.array(weight)
    heigt_square = h * h
    result = w / heigt_square
    return(result.tolist())


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    arr = [item > limit for item in bmi]
    return(arr)