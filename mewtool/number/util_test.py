from mewtool.number.util import *


def test_square_root():
    assert find_mod_sqrt(4, 13) == (2, 11)
    assert find_mod_sqrt(5, 41) == (13, 28)
    assert find_mod_sqrt(6, 13) == None
    assert find_mod_sqrt(9, 19) == (16, 3)


def test_bezout_identity():
    x, y, gcd = bezout_identity(240, 46)
    assert x * 240 + y * 46 == gcd
    assert gcd == 2

    x, y, gcd = bezout_identity(178, 29)
    assert x * 178 + y * 29 == gcd
    assert gcd == 1

    x, y, gcd = bezout_identity(588, 113)
    assert x * 588 + y * 113 == gcd
    assert gcd == 1


def test_gcd():
    assert gcd(2 * 71, 2*91, 2*8) == 2
    assert gcd(2 * 71, 2*91) == 2
    assert gcd(*[2 * 71, 2*91, 2*8]) == 2
