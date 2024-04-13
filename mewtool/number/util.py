from Crypto.Util.number import *

# Backward compatibility
from mewtool.number.modulo import crt, find_mod_sqrt, tonelli_shanks, bezout_identity, is_has_root_mod


def nth_root(x, n):
    """Calculate the nth root of x, where n is an integer."""

    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            return mid
    return mid + 1


def isqrt(x):
    return nth_root(x, 2)


def icbrt(x):
    return nth_root(x, 3)


def gcd(*arr):
    """Calculate the Greatest Common Divisor of array"""
    res = arr[0]
    for i in range(1, len(arr)):
        res = GCD(res, arr[i])

    return res


def is_perfect_square(n):
    h = n & 0xF  # last hexadecimal "digit"
    if h > 9:
        return False  # return immediately in 6 cases out of 16.
    # Take advantage of Boolean short-circuit evaluation
    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        # take square root if you must
        t = isqrt(n)
        return t * t == n
    return False
