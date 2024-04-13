from mewtool.number.fraction import Fraction, fraction_convergence, partial_quotiens
from mewtool.number.util import *


def wiener_find_d(e, n) -> int | None:
    """Wiener's attack to find d from e and n"""
    frac = Fraction(e, n)
    for i in fraction_convergence(partial_quotiens(frac)):
        k = i.x
        d = i.y

        # Rule #1: If the denominator is even, skip it.
        if d % 2 == 0:
            continue

        # Rule #2: k should devide ed-1
        if k == 0:
            continue

        if (e * d - 1) % k != 0:
            continue

        # Rule #3: the equation x^2 - (n - phi + 1)x + n = 0 should have integer roots
        phi = (e * d - 1) // k
        b = -(n - phi + 1)

        if (b ** 2) % 4 != 0:
            continue

        # Rule #3.1: discriminant must be a perfect square
        sqr = (b ** 2 >> 2) - n

        if sqr > 0 and is_perfect_square(sqr):
            return d

    return None


def wiener_find_pq(e, n) -> tuple[int, int] | None:
    """Wiener's attack to find p and q from e and n"""
    frac = Fraction(e, n)
    for i in fraction_convergence(partial_quotiens(frac)):
        k = i.x
        d = i.y

        # Rule #1: If the denominator is even, skip it.
        if d % 2 == 0:
            continue

        # Rule #2: k should devide ed-1
        if k == 0:
            continue

        if (e * d - 1) % k != 0:
            continue

        # Rule #3: the equation x^2 - (n - phi + 1)x + n = 0 should have integer roots
        phi = (e * d - 1) // k
        b = -(n - phi + 1)

        if (b ** 2) % 4 != 0:
            continue

        # Rule #3.1: discriminant must be a perfect square
        sqr = (b ** 2 >> 2) - n

        if sqr > 0 and is_perfect_square(sqr):
            result = isqrt(sqr)
            p = (b >> 1) - result
            q = (b >> 1) + result

            return (p, q)

    return None
