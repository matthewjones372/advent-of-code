from typing import *
from itertools import zip_longest


def read_file(filename: str = 'numbers.txt') -> List[int]:
    with open(filename) as f:
        return list(map(int, f.read().splitlines()))


def take_chunk(index: int, numbers: List[int], size=25) -> (List[int], int):
    *head, next_number = next(zip_longest(fillvalue=None, *[iter(numbers[index:])] * (size + 1)))
    return head, next_number


def is_summing(numbers: List[int], target: int):
    number_set = set(numbers)
    for num in numbers:
        wanted = abs(target - num)
        if wanted in number_set and wanted != num:
            return True
    else:
        return False


def find_non_summing(all_numbers: List[int], size=25) -> int:
    for i in range(len(all_numbers[size:])):
        number_chunk, target = take_chunk(i, all_numbers, size=size)
        if not is_summing(number_chunk, target):
            return all_numbers[i + size]


def find_contiguous(all_numbers: List[int], non_summing_num: int) -> int:
    for i in range(len(all_numbers)):
        contiguous_numbers = []
        for num in all_numbers[i:]:
            contiguous_numbers.append(num)
            current_sum = sum(contiguous_numbers)
            if current_sum > non_summing_num:
                contiguous_numbers.clear()
                break

            if current_sum == non_summing_num:
                return min(contiguous_numbers) + max(contiguous_numbers)


if __name__ == '__main__':
    codes = read_file()
    target = find_non_summing(codes)
    contiguous = find_contiguous(codes, target)

    print(f"Part 1 Solution: {target}")
    print(f"Part 2 Solution: {contiguous}")
