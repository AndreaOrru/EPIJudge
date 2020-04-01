from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    def compute_distance(A_idx, B_idx):
        # A is empty, so add all B characters.
        if A_idx < 0:
            return B_idx + 1
        # B is empty, so add all A characters.
        if B_idx < 0:
            return A_idx + 1
        
        result = table.get((A_idx, B_idx))
        if result is not None:
            return result

        if A[A_idx] == B[B_idx]:
            return compute_distance(A_idx - 1, B_idx - 1)

        add_last = compute_distance(A_idx, B_idx - 1)
        sub_last = compute_distance(A_idx - 1, B_idx - 1)
        del_last = compute_distance(A_idx - 1, B_idx)

        table[(A_idx, B_idx)] = result = 1 + min(add_last, sub_last, del_last)
        return result

    table = {}
    return compute_distance(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
