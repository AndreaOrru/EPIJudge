from test_framework import generic_test


def power_brute_force(x: float, y: int) -> float:
    result = 1.0
    if y < 0:
        y = -y
        x = 1.0 / x

    while y:
        result *= x
        y -= 1

    return result


def power_rec(x: float, y: int) -> float:
    if y == 0:
        return 1.0
    elif y < 0:
        y = -y
        x = 1.0 / x

    if y & 1:
        return x * power_rec(x, y - 1)
    else:
        return power_rec(x * x, y >> 1)


def power(x: float, y: int) -> float:
    result = 1.0
    # Reconduce y < 0 case to base case.
    if y < 0:
        y = -y
        x = 1.0 / x

    while y:
        # Reconduce odd exponents to even ones.
        if y & 1:
            result *= x
        y >>= 1  # Divide exponent by 2.
        x *= x   # Square the number.

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
