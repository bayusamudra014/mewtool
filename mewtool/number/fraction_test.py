from mewtool.number.fraction import *


def test_simple_continued_frac():
    frac = Fraction(10, 7)
    print(frac.simplify())

    assert partial_quotiens(frac) == [1, 2, 3]
    assert [i for i in (fraction_convergence(partial_quotiens(frac)))] == [
        Fraction(1, 1), Fraction(3, 2)]
