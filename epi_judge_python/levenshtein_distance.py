from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    distances = [[0 for b in range(len(B) + 1)] for a in range(2)]

    for A_len in range(len(A) + 1):
        for B_len in range(len(B) + 1):
            # One of the two strings is empty.
            if A_len == 0:
                distances[A_len % 2][B_len] = B_len
            elif B_len == 0:
                distances[A_len % 2][B_len] = A_len

            # Characters are the same, distance doesn't increase.
            elif A[A_len - 1] == B[B_len - 1]:
                distances[A_len % 2][B_len] = distances[(A_len - 1) % 2][B_len - 1]

            else:
                sub_distance = distances[(A_len - 1) % 2][B_len - 1]
                add_distance = distances[A_len % 2][B_len - 1]
                del_distance = distances[(A_len - 1) % 2][B_len]
                distances[A_len % 2][B_len] = 1 + min(add_distance, del_distance, sub_distance)

    return distances[A_len % 2][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
