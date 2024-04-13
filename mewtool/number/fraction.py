import mewtool.number.util as lib_numbers


class Fraction:
    """Class that represent x/y"""
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: int) -> 'Fraction':
        return Fraction(self.x + other * self.y, self.y)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        if (self.y == other.y):
            return Fraction(self.x + other.x, self.y)

        return Fraction(self.x * other.y + other.x * self.y, self.y * other.y).simplify()

    def __sub__(self, other: int) -> 'Fraction':
        return Fraction(self.x - other * self.y, self.y)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        if (self.y == other.y):
            return Fraction(self.x - other.x, self.y)

        return Fraction(self.x * other.y - other.x * self.y, self.y * other.y).simplify()

    def __mul__(self, other: int) -> 'Fraction':
        return Fraction(self.x * other, self.y)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.x * other.x, self.y * other.y).simplify()

    def __truediv__(self, other: int) -> 'Fraction':
        return Fraction(self.x, self.y * other)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.x * other.y, self.y * other.x).simplify()

    def inverse(self) -> 'Fraction':
        return Fraction(self.y, self.x)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, float) and not isinstance(value, Fraction) and not isinstance(value, int):
            return False

        if isinstance(value, float):
            return self.x / self.y == value

        if isinstance(value, int):
            return self.x / self.y == value

        value = value.simplify()
        this = self.simplify()

        return this.x == value.x and this.y == value.y

    def __str__(self) -> str:
        return f"{self.x}/{self.y}"

    def __repr__(self) -> str:
        return self.__str__()

    def simplify(self) -> 'Fraction':
        """Simplify the fraction"""
        gcd = lib_numbers.gcd(self.x, self.y)
        return Fraction(self.x // gcd, self.y // gcd)


# Faster
def partial_quotiens(frac: Fraction):
    x = frac.x
    y = frac.y

    partials = []
    while x != 1:
        partials.append(x // y)
        x = x % y
        x, y = y, x

    return partials


def calculate_conv_frac(sequence):
    i = len(sequence) - 1

    if i == -1:
        return Fraction(0, 1)

    result = Fraction(sequence[i], 1)
    while i > 0:
        i -= 1

        # Skipping simplify the result
        a = (sequence[i] * result.x) + result.y
        b = result.x
        result.x = a
        result.y = b

    return result


def fraction_convergence(partial_quotients):
    for i in range(1, len(partial_quotients)):
        yield calculate_conv_frac(partial_quotients[:i])
