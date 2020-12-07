from itertools import chain
from collections import Counter


def read_file(filename: str = "question_answers.txt"):
    with open(filename) as f:
        return [group.strip().split() for group in f.read().split("\n\n")]


def count_yes(group_answers: [[str]]) -> int:
    return sum([len(set(chain(*group))) for group in group_answers])


def all_yes(group_answers: [[str]]) -> int:
    return sum([Counter(list(Counter("".join(group)).values()))[len(group)] for group in group_answers])


if __name__ == '__main__':
    group_answers = read_file()
    print(f"Part 1 Solution : {count_yes(group_answers)}")
    print(f"Part 2 Solution : {all_yes(group_answers)}")