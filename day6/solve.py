from itertools import chain
from collections import Counter
from typing import List


GroupAnswers = List[List[str]]


def read_file(filename: str = 'question_answers.txt') -> GroupAnswers:
    with open(filename) as f:
        return [group.strip().split() for group in f.read().split("\n\n")]


def count_yes(group_answers: GroupAnswers) -> int:
    return sum([len(set(chain(*group))) for group in group_answers])


def all_yes(group_answers: GroupAnswers) -> int:
    return sum([Counter(list(Counter(''.join(group)).values()))[len(group)] for group in group_answers])


if __name__ == '__main__':
    answers = read_file()
    print(f"Part 1 Solution : {count_yes(answers)}")
    print(f"Part 2 Solution : {all_yes(answers)}")
