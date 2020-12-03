from functools import reduce
from itertools import combinations


def read_file(filename="numbers.txt"):
    with open(filename) as f:
        return [int(i) for i in f.read().splitlines()]


def find(number_list, n, target=2020):
    for combo in combinations(number_list, n):
        if sum(combo) == target:
            return reduce(lambda x, y: x * y, combo)


def find_using_set(number_list, target=2020):
    numbers_set = set(number_list)
    for number in number_list:
        wanted = abs(target - number)
        if wanted in numbers_set:
            return wanted * number


if __name__ == '__main__':
    numbers = read_file()
    print(find_using_set(numbers))
    print(find(numbers, 3))
