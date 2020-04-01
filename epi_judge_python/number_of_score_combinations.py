from typing import List

from test_framework import generic_test


def num_combinations_for_final_score_table(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    ways = [[1] + [0] * final_score
            for _ in individual_play_scores]

    for play_idx, play in enumerate(individual_play_scores):
        for score in range(1, final_score + 1):
            without_this_play = ways[play_idx - 1][score] if play_idx >= 1 else 0
            with_this_play = ways[play_idx][score - play] if score >= play else 0
            ways[play_idx][score] = without_this_play + with_this_play

    return ways[-1][-1]


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    ways = [1] + [0] * final_score

    for play in individual_play_scores:
        for score in range(play, final_score + 1):
            ways[score] += ways[score - play]

    return ways[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
