from Crypto.Util.number import *


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


def crt(am: tuple[int, int]):
    """Chinese Remainder Theorem with input pair of remainder a and its modulo m (a,m)"""
    m = 1
    for _, mi in am:
        m *= mi

    result = 0
    for ai, mi in am:
        mi_ = m // mi
        result += ai * mi_ * pow(mi_, -1, mi)

    return result % m


def find_mod_sqrt(n, p):
    """Find the square root of n modulo p"""
    # Check n is quadratic residue modulo p
    res = pow(n, (p - 1) // 2, p)
    if res == p-1:
        return None

    # If p devides n then its square root is 0
    if res == 0:
        return (0, 0)

    # If p = 3 mod 4
    if p % 4 == 3:
        res = pow(n, (p + 1) // 4, p)
        return (res, p - res)

    # Then, run tonelli-shanks algorithm
    return tonelli_shanks(n, p)


def tonelli_shanks(n, p):
    """Tonelli-Shanks algorithm to find the square root of n modulo p. Assume n is a quadratic residue modulo p."""
    # Source: https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
    # Find p - 1 = q * 2^s
    q = p - 1
    s = 0

    while q % 2 == 0:
        q >>= 1
        s += 1

    # Find a quadratic non-residue z
    z = 0
    for i in range(2, p):
        z = i
        if (p - 1) == pow(z, (p - 1) // 2, p):
            break

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 1:
        h = 0
        for i in range(1, m):
            h = i
            if pow(t, 2 ** i, p) == 1:
                break

        b = pow(c, 2 ** (m - h - 1), p)
        m = h
        c = pow(b, 2, p)
        t = (t * pow(b, 2, p)) % p
        r = (r * b) % p

    return (p-r, r)


def bezout_identity(a, b):
    """Bezout's Identity to find x and y such that ax + by = gcd(a,b)"""
    x, y = 1, 0
    prev_x, prev_y = 0, 1

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, prev_x = prev_x - quotient * x, x
        y, prev_y = prev_y - quotient * y, y

    return prev_y, prev_x, a


def is_has_root_mod(x, p):
    return pow(x, (p - 1) // 2, p) == 1
