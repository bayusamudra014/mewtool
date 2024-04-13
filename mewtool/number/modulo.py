
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
