from functools import reduce
from itertools import combinations
from typing import List, Optional


def read_file(filename: str = "numbers.txt") -> List[int]:
    with open(filename) as f:
        return [int(i) for i in f.read().splitlines()]


def find_using_brute_force(number_list: List[int], n: int, target: int = 2020) -> Optional[int]:
    for combo in combinations(number_list, n):
        if sum(combo) == target:
            return reduce(lambda x, y: x * y, combo)
    else:
        return None


def find_using_set(number_list: List[int], target: int = 2020) -> Optional[int]:
    numbers_set = set(number_list)
    for number in number_list:
        wanted = abs(target - number)
        if wanted in numbers_set:
            return wanted * number
    else:
        return None


def find_using_backtracking(number_list: List[int], target: int = 2020) -> Optional[int]:
    # TODO
    pass


if __name__ == '__main__':
    numbers = read_file()
    print(find_using_set(numbers))
    print(find_using_brute_force(numbers, 3))
