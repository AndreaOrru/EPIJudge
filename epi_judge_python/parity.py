from test_framework import generic_test


def parity_brute_force(x: int) -> int:
    result = 0

    while x:
        result ^= x & 1
        x >>= 1

    return result


def parity_and_trick(x: int) -> int:
    result = 0

    while x:
        result ^= 1
        # Drop lowest set bit of x.
        x &= x - 1

    return result


parity_table = {}

def compute_parity_table():
    global parity_table
    if parity_table:
        return

    for i in range(2 ** 16):
        parity_table[i] = parity_and_trick(i)


def parity_with_table(x: int) -> int:
    compute_parity_table()
    result = 0

    for _ in range(64 // 16):
        result ^= parity_table[x & 0xFFFF]
        x >>= 16

    return result


def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
