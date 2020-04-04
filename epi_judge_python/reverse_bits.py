from test_framework import generic_test


PRECOMPUTED_REVERSE = [
    0b0000,
    0b1000,
    0b0100,
    0b1100,
    0b0010,
    0b1010,
    0b0110,
    0b1110,
    0b0001,
    0b1001,
    0b0101,
    0b1101,
    0b0011,
    0b1011,
    0b0111,
    0b1111,
]


def reverse_bits(x: int) -> int:
    result = 0
    for _ in range(64 // 4):
        result = (result << 4) | PRECOMPUTED_REVERSE[x & 0xF]
        x >>= 4
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
